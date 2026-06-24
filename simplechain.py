from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

prompt = PromptTemplate(
    template='Generate 5 facts about {topic} \n ',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Black hole'})
print(result)
chain.get_graph().print_ascii()