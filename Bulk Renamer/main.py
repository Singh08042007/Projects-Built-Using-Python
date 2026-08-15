import os
def arrange_files(files,ext):
    pass

if __name__ == "__main__":
    files = os.listdir('.')
    ext = input("Enter the file extension to arrange: ")
    arrange_files(files, ext)