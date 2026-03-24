from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"

def add_user_message(message, text):
    user_message = {"role": "user", "content": text}
    message.append(user_message)

def add_assistant_message(message, text):
    assistant_message = {"role": "assistant", "content": text}
    message.append(assistant_message)

def chat(messages):
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return response.content[0].text

messages = []

add_user_message(messages, "Define quantum computing in one sentence")

answer = chat(messages)

add_assistant_message(messages, answer)

add_user_message(messages, "Write another sentence")

answer = chat(messages)

print(answer)