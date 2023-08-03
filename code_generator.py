# Sample code templates
code_templates = {
    "declare_variable": "{data_type} {variable_name} = {initial_value}",
    "for_loop": "for {variable} in range({start}, {end}):",
    "print_statement": "print('{message}')",
}

# Function to generate code based on the command
def generate_code(command, params):
    if command in code_templates:
        return code_templates[command].format(**params)
    else:
        return "Invalid command."

# Test the code generation
if __name__ == "__main__":
    print("Available commands:")
    for command in code_templates.keys():
        print(f"- {command}")

    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        command_parts = user_input.split(" ")
        command = command_parts[0]
        parameters = {f"param{i+1}": param for i, param in enumerate(command_parts[1:])}

        generated_code = generate_code(command, parameters)
        print("Generated code:")
        print(generated_code)
