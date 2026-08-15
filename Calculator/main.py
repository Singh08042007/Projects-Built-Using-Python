import math

class AdvancedCalculator:
    def __init__(self):
        self.history = []
        self.memory = 0
        
    def display_menu(self):
        print("\n" + "="*50)
        print("       ADVANCED CALCULATOR")
        print("="*50)
        print("\n1. Basic Operations (+, -, *, /, //, %)")
        print("2. Power & Square Root (**, √)")
        print("3. Scientific Functions (sin, cos, tan, log, ln, e^x)")
        print("4. View Calculation History")
        print("5. Memory Operations (M+, M-, MR, MC)")
        print("6. Exit")
        print("="*50)
        
    def basic_operations(self):
        try:
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))
            print("\nAvailable Operations:")
            print("  +  (Addition)")
            print("  -  (Subtraction)")
            print("  *  (Multiplication)")
            print("  /  (Division)")
            print("  // (Floor Division)")
            print("  %  (Modulus)")
            
            operator = input("\nEnter operator: ").strip()
            
            result = None
            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    print("❌ Error: Division by zero is not allowed.")
                    return
                result = a / b
            elif operator == "//":
                if b == 0:
                    print("❌ Error: Division by zero is not allowed.")
                    return
                result = a // b
            elif operator == "%":
                if b == 0:
                    print("❌ Error: Modulus by zero is not allowed.")
                    return
                result = a % b
            else:
                print("❌ Invalid operator!")
                return
            
            self._display_result(a, operator, b, result)
            
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            
    def power_and_root(self):
        try:
            print("\nChoose operation:")
            print("1. Power (a^b)")
            print("2. Square Root (√a)")
            print("3. Cube Root (∛a)")
            
            choice = input("Select (1/2/3): ").strip()
            
            if choice == "1":
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                result = a ** b
                self._display_result(a, "**", b, result)
            elif choice == "2":
                a = float(input("Enter number: "))
                if a < 0:
                    print("❌ Error: Square root of negative number is not defined.")
                    return
                result = math.sqrt(a)
                print(f"\n√{a} = {result:.6f}")
                self.history.append(f"√{a} = {result:.6f}")
            elif choice == "3":
                a = float(input("Enter number: "))
                result = a ** (1/3) if a >= 0 else -(-a) ** (1/3)
                print(f"\n∛{a} = {result:.6f}")
                self.history.append(f"∛{a} = {result:.6f}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Invalid input!")
            
    def scientific_functions(self):
        try:
            print("\nScientific Functions:")
            print("1. Sine (sin)")
            print("2. Cosine (cos)")
            print("3. Tangent (tan)")
            print("4. Logarithm (log base 10)")
            print("5. Natural Logarithm (ln)")
            print("6. e^x (Exponential)")
            
            choice = input("Select (1-6): ").strip()
            a = float(input("Enter number: "))
            
            result = None
            if choice == "1":
                result = math.sin(math.radians(a))
                print(f"\nsin({a}°) = {result:.6f}")
                self.history.append(f"sin({a}°) = {result:.6f}")
            elif choice == "2":
                result = math.cos(math.radians(a))
                print(f"\ncos({a}°) = {result:.6f}")
                self.history.append(f"cos({a}°) = {result:.6f}")
            elif choice == "3":
                result = math.tan(math.radians(a))
                print(f"\ntan({a}°) = {result:.6f}")
                self.history.append(f"tan({a}°) = {result:.6f}")
            elif choice == "4":
                if a <= 0:
                    print("❌ Error: Logarithm is only defined for positive numbers.")
                    return
                result = math.log10(a)
                print(f"\nlog₁₀({a}) = {result:.6f}")
                self.history.append(f"log₁₀({a}) = {result:.6f}")
            elif choice == "5":
                if a <= 0:
                    print("❌ Error: Natural logarithm is only defined for positive numbers.")
                    return
                result = math.log(a)
                print(f"\nln({a}) = {result:.6f}")
                self.history.append(f"ln({a}) = {result:.6f}")
            elif choice == "6":
                result = math.exp(a)
                print(f"\ne^{a} = {result:.6f}")
                self.history.append(f"e^{a} = {result:.6f}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Invalid input!")
            
    def view_history(self):
        if not self.history:
            print("\n📋 No calculation history yet.")
        else:
            print("\n📋 CALCULATION HISTORY:")
            print("-" * 40)
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
            print("-" * 40)
            
    def memory_operations(self):
        print("\nMemory Operations:")
        print(f"Current Memory Value: {self.memory:.6f}")
        print("1. M+ (Add to Memory)")
        print("2. M- (Subtract from Memory)")
        print("3. MR (Memory Recall)")
        print("4. MC (Memory Clear)")
        
        choice = input("Select (1-4): ").strip()
        
        try:
            if choice == "1":
                value = float(input("Enter value to add: "))
                self.memory += value
                print(f"✓ Added {value} to memory. Memory = {self.memory:.6f}")
            elif choice == "2":
                value = float(input("Enter value to subtract: "))
                self.memory -= value
                print(f"✓ Subtracted {value} from memory. Memory = {self.memory:.6f}")
            elif choice == "3":
                print(f"✓ Memory Recall: {self.memory:.6f}")
            elif choice == "4":
                self.memory = 0
                print("✓ Memory cleared.")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Invalid input!")
            
    def _display_result(self, a, operator, b, result):
        print(f"\n{'='*40}")
        print(f"{a} {operator} {b} = {result:.6f}")
        print(f"{'='*40}")
        self.history.append(f"{a} {operator} {b} = {result:.6f}")
        
    def run(self):
        print("Welcome to Advanced Calculator!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.basic_operations()
            elif choice == "2":
                self.power_and_root()
            elif choice == "3":
                self.scientific_functions()
            elif choice == "4":
                self.view_history()
            elif choice == "5":
                self.memory_operations()
            elif choice == "6":
                print("\n👋 Thank you for using Advanced Calculator!")
                break
            else:
                print("❌ Invalid choice! Please select 1-6.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    calc = AdvancedCalculator()
    calc.run()
