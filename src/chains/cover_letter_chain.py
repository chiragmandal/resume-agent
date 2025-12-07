from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["job_description", "resume_summary"],
    template="""You are a professional HR assistant.
Using the job description and tailored resume summary,
draft a short, concise, and impactful MARKDOWN cover letter (max 200 words).

Job Description:
{job_description}

Tailored Resume Summary:
{resume_summary}

Output the letter in markdown.""",
)

def get_cover_letter_chain(llm):
    return LLMChain(prompt=prompt, llm=llm)
