import json
import os
import urllib.error
import urllib.request


# Requested fallback key for quick local use. Prefer environment variables in production.
HARDCODED_GEMINI_API_KEY = "AQ.Ab8RN6IgcNSwIdvOGI9ZWrVNldGlKEd4X-YLwL0YwUuv0CAtiw"

MODEL_CANDIDATES = [
	"gemini-3.1-flash-lite",
	"gemini-2.5-flash-lite",
	"gemini-2.5-flash",
	"gemini-3-flash-preview",
]

API_URL_TEMPLATE = (
	"https://generativelanguage.googleapis.com/v1beta/models/"
	"{model}:generateContent"
)

HISTORY_FILE = "chat_history.json"
MAX_HISTORY_MESSAGES = 40


def load_history(file_path: str) -> list:
	"""Load saved chat history from disk."""
	if not os.path.exists(file_path):
		return []

	try:
		with open(file_path, "r", encoding="utf-8") as file:
			data = json.load(file)
	except (OSError, json.JSONDecodeError):
		return []

	if not isinstance(data, list):
		return []

	clean_history = []
	for item in data:
		if not isinstance(item, dict):
			continue
		role = item.get("role")
		text = item.get("text")
		if role in {"user", "model"} and isinstance(text, str):
			clean_history.append({"role": role, "text": text})

	return clean_history[-MAX_HISTORY_MESSAGES:]


def save_history(file_path: str, history: list) -> None:
	"""Persist chat history to disk."""
	with open(file_path, "w", encoding="utf-8") as file:
		json.dump(history[-MAX_HISTORY_MESSAGES:], file, ensure_ascii=False, indent=2)


def generate_reply(user_message: str, api_key: str, history: list) -> str:
	"""Send a prompt to Gemini and return the model reply text."""
	contents = [
		{"role": item["role"], "parts": [{"text": item["text"]}]}
		for item in history[-MAX_HISTORY_MESSAGES:]
	]
	contents.append({"role": "user", "parts": [{"text": user_message}]})

	payload = {
		"contents": contents
	}

	request_body = json.dumps(payload).encode("utf-8")
	http_errors = []

	for model in MODEL_CANDIDATES:
		url = API_URL_TEMPLATE.format(model=model)
		request = urllib.request.Request(
			url=url,
			data=request_body,
			headers={
				"Content-Type": "application/json",
				"x-goog-api-key": api_key,
			},
			method="POST",
		)

		try:
			with urllib.request.urlopen(request, timeout=60) as response:
				response_data = response.read().decode("utf-8")
		except urllib.error.HTTPError as error:
			error_message = error.read().decode("utf-8", errors="ignore")
			http_errors.append((model, error.code, error_message))
			if error.code == 404:
				continue
			raise

		data = json.loads(response_data)

		candidates = data.get("candidates", [])
		if not candidates:
			return "I could not generate a response right now."

		parts = candidates[0].get("content", {}).get("parts", [])
		text_chunks = [part.get("text", "") for part in parts if isinstance(part, dict)]
		reply = "\n".join(chunk for chunk in text_chunks if chunk).strip()
		return reply or "I could not generate a response right now."

	error_details = "; ".join(
		f"{model} -> HTTP {code}" for model, code, _ in http_errors
	)
	raise RuntimeError(
		"No compatible Gemini model was available for this key/project. "
		f"Tried: {error_details or 'no models'}"
	)


def main() -> None:
	api_key = (
		os.getenv("GEMINI_API_KEY", "").strip()
		or os.getenv("CHATBOT_API_KEY", "").strip()
		or HARDCODED_GEMINI_API_KEY
	)
	if not api_key:
		print("Error: API key is not set.")
		print("Set it first in PowerShell:")
		print('$env:GEMINI_API_KEY = "your_api_key"')
		return

	print("Gemini Chatbot is ready.")
	print("Type 'exit' to quit.\n")
	history = load_history(HISTORY_FILE)
	if history:
		print(f"Loaded {len(history)} past messages from {HISTORY_FILE}.\n")

	while True:
		user_input = input("You: ").strip()

		if not user_input:
			continue

		if user_input.lower() in {"exit", "quit"}:
			print("Bot: Goodbye!")
			break

		if user_input.lower() == "clear":
			history = []
			save_history(HISTORY_FILE, history)
			print("Bot: History cleared.\n")
			continue

		try:
			bot_reply = generate_reply(user_input, api_key, history)
			history.append({"role": "user", "text": user_input})
			history.append({"role": "model", "text": bot_reply})
			history = history[-MAX_HISTORY_MESSAGES:]
			save_history(HISTORY_FILE, history)
			print(f"Bot: {bot_reply}\n")
		except urllib.error.HTTPError as error:
			error_message = error.read().decode("utf-8", errors="ignore")
			print(f"Bot: API error ({error.code}): {error_message}\n")
		except urllib.error.URLError as error:
			print(f"Bot: Network error: {error.reason}\n")
		except json.JSONDecodeError:
			print("Bot: Failed to parse API response.\n")
		except Exception as error:
			print(f"Bot: Unexpected error: {error}\n")


if __name__ == "__main__":
	main()