import keyboard_module_test
import subprocess

def launch_llm():
    subprocess.Popen(['python', 'chatgpt.py'])  # Replace 'path_to_llm_script.py' with the actual path to your LLM script

keyboard_module_test.add_hotkey('ctrl+shift+l', launch_llm)  # Set the shortcut key to Ctrl+Shift+L

keyboard_module_test.wait('esc')  # Wait for the 'Esc' key to be pressed to stop the script
