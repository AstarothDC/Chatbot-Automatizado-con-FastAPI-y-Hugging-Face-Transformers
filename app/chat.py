from transformers import pipeline

# Carga el modelo de lenguaje
generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

def get_chat_response(message: str) -> str:
    prompt = f"Usuario: {message}\nAsistente:"
    result = generator(prompt, max_length=100, num_return_sequences=1)
    respuesta = result[0]["generated_text"].replace(prompt, "").strip()
    return respuesta

