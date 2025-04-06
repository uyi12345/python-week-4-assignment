def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"Could not read the file {filename}.")

if __name__ == "__main__":
    filename = input("Please enter the filename: ")
    read_file(filename)