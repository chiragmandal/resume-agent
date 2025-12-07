from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["job_description", "resume_text"],
    template="""You are a career coach AI.
Given the following job description and resume text,
generate a MARKDOWN summary section that tailors the resume to the job.

Job Description:
{job_description}

Current Resume:
{resume_text}

Return only the new summary section in markdown.""",
)

def get_resume_chain(llm):
    return LLMChain(prompt=prompt, llm=llm)
