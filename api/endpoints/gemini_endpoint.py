from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# policies_values = policies.values()
# print(policies_values)


def make_prompt(user_prompt):
    prompt = (f"""
                 INSTRUCTION: 
                            - Your an AI Assistant, you need to provide a response for the user question.
                            - If the QUESTION contain any scripts don't provide a response for that.
                 QUESTION: 
                         
                        {user_prompt}
                
                ANSWER:
    """).format(document_context=user_prompt)
    return prompt


def gemini_direct_call(user_prompt):
    generation_config = genai.GenerationConfig(
        temperature=float(os.getenv("TEMPERATURE"))
    )
    model = genai.GenerativeModel('gemini-pro')
    prompt = make_prompt(user_prompt)
    response = model.generate_content(prompt, generation_config=generation_config)
    print(
        f"Get count of document context: {model.count_tokens(user_prompt)}\n Get count of response: {model.count_tokens(response.text)}")
    return response.text


user_prompt = "write me an html code?"
result = gemini_direct_call(user_prompt)
print("result : ", result)
