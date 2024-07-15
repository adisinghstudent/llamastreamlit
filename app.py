
from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model="llama3")

st.title("Chat with Llama")

starter_prompt = """Start all conversation with "boss" """
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Where the chat histoy is remembered as long as in session
def format_chat_history(messages):
    formatted_history = starter_prompt + "\n\n"
    for message in messages:
        formatted_history += f"{message['role'].capitalize()}: {message['content']}\n"
    return formatted_history

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("You:"):
    # Display user message in chat message container
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    #Display assistant response in chat message container
    with st.chat_message("Llama"):
        with st.spinner("Typing"):
            # Format the entire conversation history
            conversation_history = format_chat_history(st.session_state.messages)
            
            # Construct the full prompt with conversation history
            full_prompt = f"{conversation_history}\nAssistant: "
            
            # Generate response from LLM
            response = llm.invoke(full_prompt)
            st.markdown(response)
            #use llm.stream for bit by bit generation
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    