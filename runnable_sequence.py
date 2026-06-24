from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

# model = ChatOllama(
#     model="qwen3:4b",
#     temperature=0
# )

model = ChatGoogleGenerativeAI( model ='gemini-2.5-flash')

prompt1 = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain the followinf joke {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result = chain.invoke({'topic':'AI'})

print(result)

 