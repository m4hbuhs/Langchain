from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


model = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

parser=JsonOutputParser()

template = PromptTemplate(
    template='Give me the name ,age and cty of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
## without chain

# Prompt = template.format()
# result = model.invoke(Prompt)
# final_parser = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({})
print(result)
#cons:  cant enforce schema in json output parser