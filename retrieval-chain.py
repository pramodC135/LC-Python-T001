from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
#from langchain.chains.combine_documents import create_stuff_documents_chain
#from langchain_community.document_loaders import WebBaseLoader

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

docA = Document(
    page_content="Generative AI is a type of artificial intelligence technology that can produce various types of content, including text, imagery, audio and synthetic data. The recent buzz around generative AI has been driven by the simplicity of new user interfaces for creating high-quality text, graphics and videos in a matter of seconds."
)

#def get_document_from_web(url):
#    loader = WebBaseLoader(url)
#    docs = loader.load()
#    return docs

#print(get_document_from_web('https://docs.smith.langchain.com/user_guide'))



#Create a prompt template
prompt = ChatPromptTemplate.from_template(""""
Answer the user's question :
Contex: {contex}
Question : {input}
""")

#create LLM chain
chain = prompt | model
#chain = create_stuff_documents_chain(
#    llm=model,
#    prompt=prompt
#)

response = chain.invoke({
    "input": "What is Generative AI",
    "contex" : [docA],
    #"contex" : []
})

print(response)
