import json
import requests

def get_all_offsets():
    # Fetch all relevant JSON files
    with open("dumped/json/offsets.json", "r") as file:
        offsets = json.load(file)
    with open("dumped/json/client_dll.json") as file:
        client_dll = json.load(file)
    with open("dumped/json/buttons.json") as file:
        buttons = json.load(file)

    return offsets, client_dll, buttons

def generate_cpp_offsets():
    offsets, client_dll, buttons = get_all_offsets()
    
    cpp_code = [r"#include <cstddef>", 'namespace offsets {']
    class_definitions = {}
    
    file1 = [r"#include <cstddef>", "namespace offsets {"]  # C++ code for offsets.json
    file2 = [r"#include <cstddef>", "namespace client_dll {"]  # C++ code for client_dll.json
    file3 = [r"#include <cstddef>", "namespace buttons {"] # C++ code for buttons.json

    # Check offsets.json
    for dll_name, dll_offsets in offsets.items():
        for offset_name, offset_value in dll_offsets.items():
            hex_offset = hex(offset_value)
            class_name = dll_name.replace('.', '_')  # Replace '.' with '_'
            if class_name not in class_definitions:
                class_definitions[class_name] = []
            class_definitions[class_name].append(f'\t\tconstexpr std::ptrdiff_t {offset_name} = {hex_offset}; // {class_name}')
            file1.append(f'\t\tconstexpr std::ptrdiff_t {offset_name} = {hex_offset}; // {class_name}')

    # Check client_dll.json
    for class_name, class_content in client_dll['client.dll']['classes'].items():
        fields = class_content.get('fields', {})
        class_name = class_name.replace('.', '_')  # Replace '.' with '_'
        if len(fields.items()) >= 1:
            file2.append(f"\t\tnamespace {class_name} "+ "{")
        for field_name, offset in fields.items():
            hex_offset = hex(offset)
            if class_name not in class_definitions:
                class_definitions[class_name] = []
            class_definitions[class_name].append(f'\t\tconstexpr std::ptrdiff_t {field_name} = {hex_offset}; // {class_name}')
            file2.append(f'\t\t\tconstexpr std::ptrdiff_t {field_name} = {hex_offset}; // {class_name}')
        if len(fields.items()) >= 1:
            file2.append("\t\t}")
    # Check buttons.json
    for button_name, button_value in buttons['client.dll'].items():
        hex_value = hex(button_value)
        if 'Buttons' not in class_definitions:
            class_definitions['Buttons'] = []

        class_definitions['Buttons'].append(f'\t\tconstexpr std::ptrdiff_t {button_name} = {hex_value}; // Buttons')
        file3.append(f'\t\tconstexpr std::ptrdiff_t {button_name} = {hex_value}; // Buttons')

    # Generate C++ classes
    for class_name, class_content in class_definitions.items():
        cpp_code.append(f"\tnamespace {class_name} {{")
        cpp_code.extend(class_content)
        cpp_code.append("\t}")  # Closing the namespace

    cpp_code.append('} // namespace offsets\n')

    # Write to file1
    with open("dumped/cpp/offsets.cpp", "w") as file:
        for line in file1:
            file.write(line + "\n")
        file.write("}")


    # Write to file2
    with open("dumped/cpp/client_dll.cpp", "w") as file:
        for line in file2:
            file.write(line + "\n")
        file.write("}")


    # Write to file3
    with open("dumped/cpp/buttons.cpp", "w") as file:
        for line in file3:
            file.write(line + "\n")
        file.write("}")

    return '\n'.join(cpp_code)

# Generate the C++ code for the specified offsets in a namespace
cpp_output = generate_cpp_offsets()

# Optionally, save the complete offsets to a file
with open('offsets.cpp', 'w', encoding='utf-8') as file:
    file.write(cpp_output)