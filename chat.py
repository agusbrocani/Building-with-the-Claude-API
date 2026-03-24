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

def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system

    response = client.messages.create(**params)
    return response.content[0].text

mensajes = []
systemPrompt = "Sos un asistente de matematica, " \
"que se va comportar como un profesor, por lo tanto, vas a tener que tener" \
"paciencia y explicar todo de manera clara y detallada"

while True:
    print("------------------------------")
    mensaje = input("Escribi algo (# para salir): ")

    if mensaje == "#":
        print("------------------------------")
        print("Fin del programa")
        break
    
    print("\nUsuario:", mensaje)
    add_user_message(mensajes, mensaje)

    respuesta = chat(mensajes, systemPrompt)
    print("\nAsistente:", respuesta)

    # temperature = 0.0
    # respuesta = chat(mensajes, systemPrompt, temperature)
    # print("\nAsistente temperatura baja:", respuesta)

    # temperature = 1.0
    # respuesta = chat(mensajes, systemPrompt, temperature)
    # print("\nAsistente temperatura alta:", respuesta)
    
    add_assistant_message(mensajes, respuesta)
