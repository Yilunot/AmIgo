import speech_recognition as sr
import pyttsx3
import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

if not OPENAI_KEY:
    raise ValueError("OpenAI API key is missing. Please set it in the .env file.")

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

# Modify Gradio interface using Blocks to structure the layout
with gr.Blocks() as demo:
    gr.Markdown("# Mental Health Chatbot")
    
    # Input box where the user types their message
    user_input = gr.Textbox(label="Your Input", placeholder="Type your message here...", lines=4)
    
    # Output box where the chatbot response will be displayed
    chatbot_output = gr.Textbox(label="Chat-bot Response", placeholder="Chat-bot response will appear here...", lines=4)
    
    # Button to submit the message
    submit_button = gr.Button("Submit")
    
    # Define how the button links the input and output
    submit_button.click(fn=CustomChatGPT, inputs=user_input, outputs=chatbot_output)

# Launch the interface with the 'share' option enabled
demo.launch(share=True)
