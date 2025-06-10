# 🤖 Chatbot Automatizado con FastAPI y Hugging Face Transformers

Este proyecto es una API REST desarrollada con **FastAPI** que utiliza un modelo de lenguaje de Hugging Face (`tiiuae/falcon-7b-instruct`) para generar respuestas automatizadas, sin necesidad de conectarse a OpenAI ni pagar suscripciones. Ideal para probar y desplegar chatbots educativos, de atención o demostrativos, 100% gratuito y local.

---

## 🧠 Tecnologías utilizadas

- **FastAPI** – Framework web ligero y de alto rendimiento
- **Transformers (Hugging Face)** – Biblioteca de modelos de lenguaje
- **Python 3.8+**
- **Uvicorn** – Servidor ASGI para FastAPI

---
## 🚀 Cómo usar

### 1. Clona el repositorio

```bash
git clone https://github.com/AstarothDC/Chatbot-Automatizado-con-FastAPI-y-Hugging-Face-Transformers
cd chatbot-fastapi-huggingface
```

### 2. Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el servidor

```bash
uvicorn app.main:app --reload
```

### 5. Prueba la API en tu navegador

Abre [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Usa el endpoint `POST /chat/` para enviar mensajes.

```json
{
  "message": "Hola, ¿qué es la automatización?"
}
```

---

## 📁 Estructura del proyecto

```
chatbot-api/
├── app/
│   ├── main.py          # API principal
│   ├── chat.py          # Lógica del chatbot con Hugging Face
├── requirements.txt     # Dependencias
├── README.md            # Este archivo
```

---

## 📌 Notas

- Este proyecto **no requiere conexión a OpenAI** ni clave de API.
- El modelo `tiiuae/falcon-7b-instruct` se descarga automáticamente la primera vez.
- Puedes cambiar fácilmente a otros modelos de Hugging Face modificando `chat.py`.

---

## ✅ Próximos pasos sugeridos

- Crear una pequeña interfaz web en HTML o React.
- Agregar memoria contextual entre mensajes.
- Conectar con WhatsApp o Telegram.
- Cambiar el modelo por uno más robusto (`gpt2`, `Mistral`, etc.).

---

## 🧠 Créditos

Desarrollado por [Ing. Dilan Cabas / GitHub](https://github.com/AstarothDC)  

