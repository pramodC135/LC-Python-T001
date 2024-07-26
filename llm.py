from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    #max_tokens=1000,
    #verbose=True
)

#response = llm.invoke("Hello, How are you?")
#response = llm.batch(["Hello, How are you?", "Write a poem about AI"])
response = llm.stream("Write a poem about AI")

#print(response)
for chunk in response:
    print(chunk.content, end="", flush=True)
