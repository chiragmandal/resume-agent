import os
from langchain_community.llms import Ollama

MODEL_NAME = os.getenv("MODEL_NAME", "llama2")

llm = Ollama(model=MODEL_NAME, temperature=0.4)
