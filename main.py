import openai
import keyboard
import pyperclip
from keyboard import get_typed_strings


class AutocompleteAssistant:
    def __init__(self, openai_api_key, openai_base_url):
        openai.api_key = openai_api_key
        openai.base_url = openai_base_url
        
        self.typed_strings = []
        self.long_term_memory = []
        self.add_content_hotkey='alt+space'
        self.generate_hotkey='shift+space'
        self.clear_memory_hotkey='ctrl+shift'
    def summarize(self,text):
        chat_prompt = "you are a summarizer to summarize the given text for storing as a long term memory which i can pass to ai tools like chatgpt to provide them context, summarize the text below :\n"
        prompt = chat_prompt + text   
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        result=completion.choices[0].message.content
        self.long_term_memory.append(result)
        print("summarized text : ",result)


    def generate(self):
        print(self.typed_strings)
        
        chat_prompt = "do the following task :\n"
        if self.long_term_memory:
            chat_prompt += "previous chat history context:\n"
            for text in self.long_term_memory:
                chat_prompt += text
        if self.typed_strings:
            task = self.typed_strings[-1]
            chat_prompt += f"task: {task}\n"
            if len(self.typed_strings)>1:
                chat_prompt += "content for the given task :\n"
                for text in self.typed_strings[:-1]:
                    chat_prompt += text
        else:
            keyboard.write("no task to do")
            return
        print(chat_prompt)

        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": chat_prompt},
            ],
        )
        result=completion.choices[0].message.content
        
        keyboard.write(result)
        self.summarize(result)
        self.typed_strings.clear()


    def run(self):
        keyboard.add_hotkey(self.add_content_hotkey, lambda:self.typed_strings.append(pyperclip.paste()))
        keyboard.add_hotkey(self.generate_hotkey, self.generate)
        keyboard.add_hotkey(self.clear_memory_hotkey, lambda:self.long_term_memory.clear())
        

        while True:
            continue
        
        


if __name__ == "__main__":
    assistant = AutocompleteAssistant(
        openai_api_key='YOUR_OPENAI_API_KEY',
        openai_base_url="http://localhost:3040/v1/"
    )
    assistant.run()
