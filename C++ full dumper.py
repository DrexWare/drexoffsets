import json
import requests

def get_all_offsets():
    # Fetch all relevant JSON files
    offsets_url = 'https://raw.githubusercontent.com/DrexWare/drexoffsets/main/dumped/json/offsets.json'
    client_dll_url = 'https://raw.githubusercontent.com/DrexWare/drexoffsets/main/dumped/json/client_dll.json'
    buttons_url = 'https://raw.githubusercontent.com/DrexWare/drexoffsets/main/dumped/json/buttons.json'
    
    offsets = requests.get(offsets_url).json()
    client_dll = requests.get(client_dll_url).json()
    buttons = requests.get(buttons_url).json()

    return offsets, client_dll, buttons



def generate_cpp_offsets():
    offsets, client_dll, buttons = get_all_offsets()
    
    cpp_code = [r"#include <cstddef>",'namespace offsets {']
    class_definitions = {}

    # Check offsets.json
    for dll_name, dll_offsets in offsets.items():
        for offset_name, offset_value in dll_offsets.items():
            
                hex_offset = hex(offset_value)
                class_name = dll_name.replace('.', '_')  # Replace '.' with '_'
                if class_name not in class_definitions:
                    class_definitions[class_name] = []
                class_definitions[class_name].append(f'        constexpr std::ptrdiff_t {offset_name} = {hex_offset};// {class_name}')

    # Check client_dll.json
    for class_name, class_content in client_dll['client.dll']['classes'].items():
        fields = class_content.get('fields', {})
        class_name = class_name.replace('.', '_')  # Replace '.' with '_'
        for field_name, offset in fields.items():
        
                hex_offset = hex(offset)
                if class_name not in class_definitions:
                    class_definitions[class_name] = []
                class_definitions[class_name].append(f'        constexpr std::ptrdiff_t {field_name} = {hex_offset}; // {class_name}')
    class_definitions[class_name].append("}")
    # Check buttons.json
    for button_name, button_value in buttons['client.dll'].items():
        
            hex_value = hex(button_value)
            if 'Buttons' not in class_definitions:
                class_definitions['Buttons'] = []
            class_definitions['Buttons'].append(f'        constexpr std::ptrdiff_t {button_name} = {hex_value};// {class_name}')

    # Generate C++ classes
    for class_name, class_content in class_definitions.items():
        cpp_code.append("\tnamespace "+class_name+"{")
        cpp_code.extend(class_content)
        cpp_code.extend("\t}")
    
    cpp_code.append('} // namespace offsets\n')

    # Add the C++ version of the Entity class
   

    return '\n'.join(cpp_code)



# Example C++ input


# Generate the C++ code for the specified offsets in a namespace and with the Entity class
cpp_output = generate_cpp_offsets()

# Optionally, save offsets to a file
with open('offsets.cpp', 'w', encoding='utf-8') as file:
    file.write(cpp_output)
