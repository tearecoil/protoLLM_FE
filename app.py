from PyPDF2 import PdfReader

import streamlit as st 
import requests
import os

def main():
    st.title("OPENAI THEME - PROTOTYPE LLM")
    st.sidebar.title('Files Submitted')
    pdf = st.sidebar.file_uploader("UPLOAD YOUR PDF FILE", type="pdf")
    #Process if there's a file uploaded (first version only works with 1 PDF)
    if pdf:
        files = {'file': pdf}
        response = requests.post('http://127.0.0.1:8000/uploadfile/', files=files)
        print(response.json()["message"])
        #If that PDF was succesfully uploaded
        if response.json()["message"] == "Successfully uploaded":
            query = st.text_input("Ask question to PDF...")
            col1, col2, col3 = st.columns([1,1,5])
            with col1:
                submit_button = st.button("Submit")
            with col2:
                cancel_button = st.button("Cancel")
            if cancel_button:
                st.stop()
            #A query was sent
            if submit_button:
                if query: 
                    print("OK")
                    basequery = {'name': 'admin', 'data': query}
                    response = requests.post('http://127.0.0.1:8000/askquery/', json= basequery)
                    print(response.json()["message"])
                    st.write(response.json()["message"])
                    # docs = knowledgeBase.similarity_search(query)
                    # llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model = 'gpt-4o-mini')
                    # #llm = llmopenai(openai_api_key=os.getenv('OPENAI_API_KEY'))
                    # chain = load_qa_chain(llm, chain_type="stuff")

                    # with get_openai_callback() as cost:
                    #     response = chain.invoke(input={"question": query, 
                    #                                 "input_documents": docs})
                    #     print(cost)
                    #     st.write(response["output_text"])
                else:
                    print("NO QUERY YET")

        # if response["message"] == "Successfully uploaded":
        #     print("OK")
    # button = st.button("test")
    # if button:
    #     response = requests.get('http://127.0.0.1:8000/')
    #     rep = response.json()
    

if __name__ == "__main__":
    main()