import speech_recognition as sr
import pyttsx3
import os
import gradio
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
import openai
openai.api_key = OPENAI_KEY

messages = [{"role": "system", "content": "Mental Health Chatbot"}]

def CustomChatGPT(Me):
    messages.append({"role": "user", "content": Me})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        max_tokens =50,
        messages = messages
        
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs= "text" , title = "Mental-Health-Chatbot")
demo.launch(share=True)