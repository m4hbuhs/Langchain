from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model ="gpt-5-mini" )


result = llm.invoke("what is the capital of india")

print(result.content)