

API_KEY = ""

from langchain.chat_models import init_chat_model

model = init_chat_model(model="gemini-3-flash-preview"
                        ,model_provider="google-genai"
                        ,api_key=API_KEY)


with open('data.txt') as file:
    data = file.read()

response= model.invoke(f"Which of these is best for ai: {data}")
print(response.content[0]['text'])
