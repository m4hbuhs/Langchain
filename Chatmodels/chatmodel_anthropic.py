from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model = "claude-sonnet-4-6")


result = llm.invoke("what is the capital of india")

print(result.content)