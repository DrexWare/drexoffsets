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


def extract_offset_names(cpp_input):
    # Extract offset names from the input C++ definitions
    return [line.split(' ')[2].split('=')[0] for line in cpp_input.splitlines() if line]


def generate_cpp_offsets(cpp_input):
    offsets, client_dll, buttons = get_all_offsets()
    offset_names = extract_offset_names(cpp_input)

    cpp_code = [r"#include <cstddef>",'namespace offsets {']
    class_definitions = {}

    # Check offsets.json
    for dll_name, dll_offsets in offsets.items():
        for offset_name, offset_value in dll_offsets.items():
            if offset_name in offset_names:
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
            if field_name in offset_names:
                hex_offset = hex(offset)
                if class_name not in class_definitions:
                    class_definitions[class_name] = []
                class_definitions[class_name].append(f'        constexpr std::ptrdiff_t {field_name} = {hex_offset}; // {class_name}')

    # Check buttons.json
    for button_name, button_value in buttons['client.dll'].items():
        if button_name in offset_names:
            hex_value = hex(button_value)
            if 'Buttons' not in class_definitions:
                class_definitions['Buttons'] = []
            class_definitions['Buttons'].append(f'        constexpr std::ptrdiff_t {button_name} = {hex_value};// {class_name}')

    # Generate C++ classes
    for class_name, class_content in class_definitions.items():
     
        cpp_code.extend(class_content)
 
    cpp_code.append('} // namespace offsets\n')

    # Add the C++ version of the Entity class
   

    return '\n'.join(cpp_code)



# Example C++ input
cpp_input = """
constexpr std::ptrdiff_t dwCSGOInput = 0x1a8c460; 
constexpr std::ptrdiff_t dwBoneMatrix = 0x170; 
constexpr std::ptrdiff_t m_sSanitizedPlayerName = 0x770;
constexpr std::ptrdiff_t m_pCameraServices = 0x11E0;
constexpr std::ptrdiff_t m_iFOV = 0x210;
constexpr std::ptrdiff_t m_bIsScoped = 0x23E8;
constexpr std::ptrdiff_t m_vOldOrigin = 0x1324; 
constexpr std::ptrdiff_t dwEntityList = 0x1a176c8; 
constexpr std::ptrdiff_t dwGameEntitySystem = 0x1b3af68; 
constexpr std::ptrdiff_t dwGameEntitySystem_highestEntityIndex = 0x20f0; 
constexpr std::ptrdiff_t dwGameRules = 0x1a7e048; 
constexpr std::ptrdiff_t dwGlobalVars = 0x185fab8; 
constexpr std::ptrdiff_t dwGlowManager = 0x1a7d790; 
constexpr std::ptrdiff_t dwLocalPlayerController = 0x1a680d0; 
constexpr std::ptrdiff_t dwLocalPlayerPawn = 0x186bdf8; 
constexpr std::ptrdiff_t dwPlantedC4 = 0x1a86b10; 
constexpr std::ptrdiff_t dwPrediction = 0x186bc90; 
constexpr std::ptrdiff_t dwSensitivity = 0x1a7ed68; 
constexpr std::ptrdiff_t dwSensitivity_sensitivity = 0x40; 
constexpr std::ptrdiff_t dwViewAngles = 0x1a8c830; 
constexpr std::ptrdiff_t dwViewMatrix = 0x1a82740; 
constexpr std::ptrdiff_t dwViewRender = 0x1a830b8; 
constexpr std::ptrdiff_t dwWeaponC4 = 0x1a1a950; 
constexpr std::ptrdiff_t dwBuildNumber = 0x53abd4; 
constexpr std::ptrdiff_t dwNetworkGameClient = 0x539ce0; 
constexpr std::ptrdiff_t dwNetworkGameClient_clientTickCount = 0x368; 
constexpr std::ptrdiff_t dwNetworkGameClient_deltaTick = 0x27c; 
constexpr std::ptrdiff_t dwNetworkGameClient_isBackgroundMap = 0x281447; 
constexpr std::ptrdiff_t m_iszPlayerName = 0x660; 
constexpr std::ptrdiff_t m_hPlayerPawn = 0x80c; 
constexpr std::ptrdiff_t m_pInGameMoneyServices = 0x720; 
constexpr std::ptrdiff_t m_iAccount = 0x40; 
constexpr std::ptrdiff_t m_modelState = 0x170;
constexpr std::ptrdiff_t m_iHealth = 0x344; 
constexpr std::ptrdiff_t m_iTeamNum = 0x3e3;
constexpr std::ptrdiff_t m_pGameSceneNode = 0x328;
constexpr std::ptrdiff_t m_vecViewOffset = 0xcb0; 
constexpr std::ptrdiff_t m_iBoneIndex = 0xfb8; 
constexpr std::ptrdiff_t m_aimPunchAngle = 0x1584; 
constexpr std::ptrdiff_t m_entitySpottedState = 0x23d0; 
constexpr std::ptrdiff_t m_iShotsFired = 0x23fc;
constexpr std::ptrdiff_t m_flFlashDuration = 0x140c;
constexpr std::ptrdiff_t m_iIDEntIndex = 0x1458; 

"""

# Generate the C++ code for the specified offsets in a namespace and with the Entity class
cpp_output = generate_cpp_offsets(cpp_input)

# Generate Memory class code


# Print or save the output
print(cpp_output)

# Optionally, save offsets to a file
with open('offsets.cpp', 'w', encoding='utf-8') as file:
    file.write(cpp_output)
