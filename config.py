import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def load_model():

    api_key = os.getenv("GEMINI_API_KEY")

    genai.configure(api_key=api_key)

    system_prompt = (
        "You are a strict study assistant. Only answer questions related to Machine Learning (ML), "
        "Deep Learning (DL), Artificial Intelligence (AI), Generative AI (Gen AI), and Agentic AI. "
        "If the user asks about anything else, politely decline."
    )
    model = genai.GenerativeModel("gemini-2.5-flash", system_instruction=system_prompt)

    return model