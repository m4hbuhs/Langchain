from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature =0.5)

message = [
    SystemMessage(content = 'you are a helpful assistant'),
    HumanMessage(content = 'what is langchain')
]
result = model.invoke(message)
message.append(AIMessage(content=result.content))

print(message)