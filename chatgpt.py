import gradio as gr
import openai

openai.api_key = 'anything'
openai.base_url = "http://localhost:3040/v1/"

def generate_response(user_input):
    messages = [
        {"role": "user", "content": user_input},
    ]
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    response = completion.choices[0].message.content
    return response



def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = generate_response(message)

    partial_message = ""
    for chunk in response:
        partial_message += chunk
        yield partial_message

gr.ChatInterface(predict).launch()