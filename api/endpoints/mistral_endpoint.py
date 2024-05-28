from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()


def get_response(user_prompt):
    template = """
        Question: 
            {user_prompt}
              
        ANSWER:
    """.format(user_prompt=user_prompt)

    prompt = ChatPromptTemplate.from_template(template)

    model_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceHub(
        repo_id=model_id,
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_kwargs={
            "temperature": 0.1,
            "max_new_tokens": 1024,
            "top_k": 50,
            "repetition_penalty": 1.03,
            "max_length": 3000
        }
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"user_prompt: ": user_prompt})
    return response


user_prompt = "Hai!"
result = get_response(user_prompt)
print(result)
