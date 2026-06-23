from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


model = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

schema =[
    ResponseSchema(name = 'fact_1' ,description = 'Fact 1 about the topic' ),
    ResponseSchema(name = 'fact_1' ,description = 'Fact 1 about the topic' ),
    ResponseSchema(name = 'fact_1' ,description = 'Fact 1 about the topic' ),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 Facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)
# helps structure json data from llm based on the predefined field schema
# we cant do data validation in structured output parser