# from pandasai.llm.local_llm import LocalLLM
# import streamlit as st
# import pandas as pd
# from pandasai import SmartDataframe

# model = LocalLLM(
#      api_base= "http://localhost:11434",
#      model = "llama3"
#  )

# st.title("Talk to your Llama friend")
# uploaded_file = st.file_uploader("Upload your files for llama", type = ['csv'])

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.write(data.head(3))

#     df = SmartDataframe(data, config={"llm": model})
#     prompt = st.text_area("Enter your prompt:")

# if st.button("Generate"):
#         if prompt:
#             with st.spinner("typing.."):
#                 st.write(df.chat(prompt))


from langchain_community.llms import Ollama
import streamlit as st


llm = Ollama(model = "llama3")

st.title("Chat with llama")
prompt = st.text_area("Start typing:")

if st.button("Answer"):
    if prompt: 
        with st.spinner("Typing..."):
            answer = st.write(llm.invoke(prompt, stop = ['< |eot_id| >']))
#to have the answer print out in bit by bit style (stream) we can use st.write_stream and llm.stream instead

