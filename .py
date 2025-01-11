import re

def parse_text_to_array():
    # Step 1: Ask the user to paste the text and press Enter
    print("Please paste the text (end with Enter):")
    user_input = input()

    # Step 2: Ask the user for the name of the array
    array_name = input("What would you like to name the array? ")

    # Step 3: Use regex to find all words and characters
    parsed_array = re.findall(r'\w+|[\W]', user_input)

    # Prepare the output
    output = f"{array_name} = {parsed_array}\n"

    # Print the result to the terminal
    print(output)

    # Step 4: Ask if the user wants to append to the output file
    append_choice = input("Do you want to add this to the output file? (yes/no): ").strip().lower()

    # Step 5: Dynamically name the output text file based on the array name
    file_name = f"{array_name.strip()}.txt"

    # Step 6: Write or append the output to the file
    if append_choice == 'yes':
        with open(file_name, "a") as file:
            file.write(output)
        print(f"Output appended to {file_name}")
    else:
        with open(file_name, "w") as file:
            file.write(output)
        print(f"Output written to {file_name}")

# Call the function
parse_text_to_array()
