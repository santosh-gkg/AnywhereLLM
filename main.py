from AnywhereLLM import AnywhereLLM

assistant = AnywhereLLM(
    openai_api_key='YOUR_OPENAI_API_KEY',# can be left like this if you are using reverse proxy 
    openai_base_url="http://localhost:3040/v1/",# can be left like this if you are using reverse proxy
    add_content_hotkey='alt+space',
    generate_hotkey='shift+space',
    clear_memory_hotkey='ctrl+shift'
)
assistant.run()