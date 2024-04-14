import keyboard
import openai



openai.api_key = 'YOUR_OPENAI_API_KEY'
openai.base_url = "http://localhost:3040/v1/"

def fetch_autocomplete(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "you are a autocomplete agent, which suggest the few next words based on the context.", "content": text},
        ],
    )
    return completion.choices[0].message.content[len(text):].strip()

print(fetch_autocomplete("mango is a sweet fruit, it comes in the season of "))