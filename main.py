from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""

Hare is the conversation history: {context}

Question: {question}

Answer: 
"""

model = Ollama(model="moondream")
prompt= ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context=""
    print("Welcome to AI chatbot!")

    while True:
        user_input=input("You: ")
        if user_input.lower() =="exit":
            break

result = chain.invoke({"context":context, "question":user_input})
print("Bot: ",result)

context+= f"\nUser: {user_input}\n AI:{result}"


if __main__ == "__main__":
     handle_conversation()