# 🔥 LLM **B**ring **Y**our **O**wn **D**ata

### QA Chat with your PDF using LangChain, Faiss, Streamlit and ChatGPT API

PDF sample data    

<img src="https://github.com/domainio/llm-byod/blob/main/assets/pdf_sample_data.png" width="500" />

    
🤔 Ask questions and 🤖 get concise answers based on your own data context   

<img src="https://github.com/domainio/llm-byod/blob/main/assets/app_qa.png" width="500" />
  

## Setup Guide
1. Create a Python virtual env
```
python -m venv .venv
source .venv/bin/activate
```
2. Install the required dependencies
```
pip install -r requirements.txt
```
  
4. Create an OpenAI API key and put it in the `.env` file as `OPENAI_API_KEY=<your API key>`

5. Run the app
```
streamlit run main.py
```



  
> [!IMPORTANT]
> You must have an active OpenAI API key which may involve costs.
> For instance:
> 
> <img src="https://github.com/domainio/llm-byod/blob/main/assets/cost.png" width="200" />




## Next steps
1. Enhance the prompts engineering for better accurate QA.
3. Add a history element to the chat with LLM.
