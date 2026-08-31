from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
ChatModel=OpenAI(model="gpt-4")
result=ChatModel.invoke("What is the capital of India?")
print(result.content)
  