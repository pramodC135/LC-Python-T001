from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo"
)

#Create a prompt template
#prompt = ChatPromptTemplate.from_template("tell me a joke about a {subject}")

#Create a prompt messages
prompt = ChatPromptTemplate.from_messages(
    [
        #("system", "you are an AI chef, Create a unique recipe based on the follow main ingrediaent."),
        ("system", "Generate a list of 10 synoyms for the following word. Return the results as a comma seperated list."),
        ("human", "{input}")
    ]
)

#create LLM chain
chain = prompt | llm

#response = chain.invoke({"subject":"dog"})
#response = chain.invoke({"input":"tomatoes"})
response = chain.invoke({"input":"happy"})

print(response)
#print(type(response.content))
