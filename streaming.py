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

messages = []

add_user_message(messages, "Write a 1 sentence description of a fake database")

# Esta forma es sin el SDK, usando directamente la API de streaming de Anthropic

# stream = client.messages.create(
#     model=model,
#     max_tokens=1000,
#     messages=messages,
#     stream=True
# )

# # Itero sobre el stream de respuestas y las imprimo a medida que llegan
# for event in stream:
#     print(event)


# with en Python ≈ try-with-resources en Java
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        # print(text, end="", flush=True)
        pass

finalMessageResponse = stream.get_final_message()

print(finalMessageResponse.content[0].text)
