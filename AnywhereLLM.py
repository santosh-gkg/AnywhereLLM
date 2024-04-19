import openai
import keyboard
import pyperclip
from keyboard import get_typed_strings



class AnywhereLLM:
    '''
    with AnywhereLLM you can store the context of the chat history and the task you are doing and generate the content for the given task by providing the context of the chat history and the task you are doing.
    you can do this anywhere in your system by using the hotkeys.
    hotkeys:
    - alt+space : to add the content to the chat history
    - shift+space : to generate the content for the given task by providing the context of the chat history and the task you are doing
    - ctrl+shift : to clear the chat history
    To use the AnywhereLLM  you need not provide any openai api key, you can use the chatgpt reverse proxy server to generate the content.

    '''

    def __init__(self, openai_api_key='anything', openai_base_url='http://localhost:3040/v1/',add_content_hotkey='alt+space',generate_hotkey='shift+space',clear_memory_hotkey='ctrl+shift'):
        openai.api_key = openai_api_key
        openai.base_url = openai_base_url
        
        self.typed_strings = []
        self.long_term_memory = []
        self.add_content_hotkey=add_content_hotkey
        self.generate_hotkey=generate_hotkey
        self.clear_memory_hotkey=clear_memory_hotkey
    def __str__(self) -> str:
        long_term_memory = "long term memory :\n"
        for text in self.long_term_memory:
            long_term_memory += text + "\n"
        typed_strings = "typed strings :\n"
        for text in self.typed_strings:
            typed_strings += text + "\n"
        hotkeys = f"add content hotkey : {self.add_content_hotkey}\n"
        hotkeys += f"generate hotkey : {self.generate_hotkey}\n"
        hotkeys += f"clear memory hotkey : {self.clear_memory_hotkey}\n"
        return long_term_memory + typed_strings + hotkeys

        
    def summarize(self,text):
        chat_prompt = "you are a summarizer to summarize the given text for storing as a long term memory which i can pass to ai tools like chatgpt to provide them context, summarize the text below in 50 words:\n"
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
    assistant = AnywhereLLM(
        openai_api_key='YOUR_OPENAI_API_KEY',
        openai_base_url="http://localhost:3040/v1/"
    )
    assistant.run()
