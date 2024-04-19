 # AnywhereLLM

 AnywhereLLM is a versatile tool that allows you to store chat history context and generate content for tasks anywhere on your system using convenient hotkeys. With AnywhereLLM, you can seamlessly integrate context from your chat history into AI tools like ChatGPT to provide them with relevant information.


<p align="center">
  <img src="AnywhereLLM.png" alt="AnywhereLLM logo"></a>
</p>


 

 ## Table of Contents

1. [AnywhereLLM](#AnywhereLLM)
2. [Features](##features)
3. [Usage](#usage)
4. [Contributions you can make](#contributions-you-can-make)
5. [Installation](#installation)
6. [Dependencies](#dependencies)
7. [Getting Started](#getting-started)


 ## Features

 - **Contextual Content Generation**: Easily generate content for tasks by providing the context of the chat history and the task you are doing.
 - **Hotkey Integration**: Use customizable hotkeys to add content to the chat history, generate content for tasks, and clear the chat history.
 - **No API Key Required**: Utilize the ChatGPT reverse proxy server for content generation without the need for an OpenAI API key.

 ## Usage

 1. **Adding Content to Chat History**: Press `Alt+Space` to add content to the chat history.
 2. **Generating Content for Tasks**: Press `Shift+Space` to generate content for the current task using the chat history context.
 3. **Clearing Chat History**: Press `Ctrl+Shift` to clear the chat history.

 ## Contributions you can make
 - Integrate the support of images, use PIL to access copied images, an api provider AI tool for image tasks
 - Add the voice command support
 - Add the support of chat with documents simply by copying a document
 - Automating tasks using keyboard.press_and_release function 

 Pull requests are highly appreciated.
 ## Installation

 To use AnywhereLLM, simply clone the repository and run the provided script.

  To use chatgpt 3.5 turbo for free Do
 ```bash
 docker run -dp 3040:3040 pawanosman/chatgpt:latest
 ```
 We use this reverse proxy, if you want to use other models you can edit the openai base and api key
 I would like to thanks [PawanOsman](https://github.com/PawanOsman/ChatGPT/) for this amazing contribution.

 ```bash
 git clone https://github.com/santosh-gkg/anywhereLLM.git
 cd anywhereLLM
 pip install -r requirements.txt
 python main.py
 ```




 ## Dependencies

 - `openai`
 - `keyboard`
 - `pyperclip`

 Ensure these dependencies are installed before running AnywhereLLM.

 ## Getting Started

 1. Setup the installation as mentioned above.
 2. Customize hotkeys according to your preference.
 3. Use AnywhereLLM by simply running `python anywhereLLM.py`.





Feel free to raise an issue! 




