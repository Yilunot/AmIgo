import os
import openai
import gradio as gr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

if not OPENAI_KEY:
    raise ValueError("OpenAI API key is missing. Please set it in the .env file.")

# Set the OpenAI API key
openai.api_key = OPENAI_KEY 

# Initialize messages with system context and an introductory message
messages = [
    {"role": "system", "content": "Mental Health Chatbot"},
    {"role": "assistant", "content": "Hello! I am Dr. GPT, your mental health assistant. For legal reasons, I must claim that I am not a certified doctor. How can I help you today?"}
]

# Initialize chat history with the introductory message
initial_chat = [("", "Hello! I am your Dr. Gpt, your mental health assistant. For legal reasons, I must claim that I am not a certified doctor. How can I help you today?")]

def CustomChatGPT(user_input, chat_history):
    # Append the user's message to the messages
    messages.append({"role": "user", "content": user_input})
    
    # Call the OpenAI API for a response
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        max_tokens = 50,
        messages = messages
    )
    
    # Get the response from the assistant
    assistant_reply = response["choices"][0]["message"]["content"]
    
    # Append the assistant's message to the messages and chat history
    messages.append({"role": "assistant", "content": assistant_reply})
    chat_history.append((user_input, assistant_reply))
    
    return chat_history, ""

# Gradio interface using Blocks to structure the layout
with gr.Blocks() as demo:
    gr.Markdown("# Mental Health Chatbot")
    
    # Chatbot component for displaying chat history
    chatbot = gr.Chatbot(label="Chat History")
    
    # Input box where the user types their message
    user_input = gr.Textbox(label="Your Input", placeholder="Type your message here...", lines=4)
    
    # Button to submit the message
    submit_button = gr.Button("Submit")
    
    # Define how the button links the input and output
    submit_button.click(fn=CustomChatGPT, inputs=[user_input, chatbot], outputs=[chatbot, user_input])
    
    # Set up submission with Enter key
    user_input.submit(fn=CustomChatGPT, inputs=[user_input, chatbot], outputs=[chatbot, user_input])
    
# Launch the interface with the 'share' option enabled
demo.launch(share=True)
