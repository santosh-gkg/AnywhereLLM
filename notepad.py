import keyboard_module_test
import openai
import pyperclip

openai.api_key = 'YOUR_OPENAI_API_KEY'
openai.base_url = "http://localhost:3040/v1/"

def fetch_autocomplete(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return completion.choices[0].message.content[len(text):].strip()

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    current_word = ""
    response = fetch_autocomplete(message)
    if response:
        current_word = response

    partial_message = ""
    for chunk in response:
        partial_message += chunk
        yield partial_message

    current_word = ""
    while True:
        try:
            event = keyboard_module_test.read_event()
            if event.event_type == keyboard_module_test.KEY_DOWN:
                if event.name == 'tab':
                    if current_word:
                        response = fetch_autocomplete(current_word)
                        if response:
                            pyperclip.copy(response)
                            keyboard_module_test.press_and_release('ctrl+v')
                            current_word = ""
                elif event.name == 'space':
                    current_word = ""
                else:
                    current_word += event.name
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print("Auto-Complete Text Editor")
    print("Press 'Tab' for auto-complete suggestions.")
    print("Press 'Ctrl+C' to exit.")
    
    initial_message = ""
    keyboard_module_test.hook(lambda event: predict(initial_message, []), suppress=True)
    keyboard_module_test.wait('ctrl+shift+l')
