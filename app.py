from dotenv import load_dotenv
import streamlit as st
import Poem_RAG_generator.chain as chain
load_dotenv()
def poem_generator_app():
    '''
    Poem generator app
    '''
    with st.form("poem_generator"):
         topic = st.text_input("Enter topic for the poem")
         submitted = st.form_submit_button("Sumbit")

         if(submitted):
            response = chain.generate_poem(topic)
            st.info(response)

poem_generator_app()