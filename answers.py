def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content as needed
        modified_content = content.upper()  # Example modification: convert content to uppercase

        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except IOError:
        print(f"Could not read or write to file {input_filename} or {output_filename}.")

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    read_and_modify_file(input_filename, output_filename)