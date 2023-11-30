import streamlit as st
from langchain.agents import creat_csv_agent
from langchain.llm import OpenAI
from dotenv import load_dotenv


def main ():
  load_dotenv ()

  st.set_page_config (page_title = ("Ask me a question: ")
  st.header ("Ask me a question: ")

  user_csv = st.file_uploader ("Upload your CSV file ", type= "csv")

  if user_csv is not None:
    user_question = st.text_input ("Ask me a question about your CSV file: ")

    llm = OpenAI (temperature=0)
    agent= create_csv-agent (llm, user_csv, verbose= True)


    if user_question is not None and user_question != "":
      response = agent.run(user_question)
      st.write (response)

if__name__ == "__main__":
    main()

    
