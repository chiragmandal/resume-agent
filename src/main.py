import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.config import llm
from src.chains.resume_chain import get_resume_chain
from src.chains.cover_letter_chain import get_cover_letter_chain
from src.utils.vector_store import get_vector_store, add_documents
from src.utils.export_utils import export_to_docx, export_to_pdf

st.set_page_config(page_title="Smart Resume & Cover Letter Agent", page_icon="")

st.title("Smart Resume & Cover Letter Agent")

job_desc = st.text_area("Paste the Job Description", height=250)
resume_text = st.text_area("Paste your Master Resume Text", height=250)

if st.button("Generate"):
    with st.spinner("Generating personalized resume and cover letter..."):
        resume_chain = get_resume_chain(llm)
        result = resume_chain.invoke({"job_description": job_desc, "resume_text": resume_text})
        tailored_resume = result["text"]

        cover_letter_chain = get_cover_letter_chain(llm)
        letter_result = cover_letter_chain.invoke({
            "job_description": job_desc,
            "resume_summary": tailored_resume
        })
        cover_letter = letter_result["text"]

    st.subheader("Tailored Resume Summary")
    st.markdown(tailored_resume)

    st.subheader("Cover Letter")
    st.markdown(cover_letter)

    docx_file = export_to_docx(tailored_resume, cover_letter, "application.docx")
    pdf_file = export_to_pdf(tailored_resume, cover_letter, "application.pdf")

    with open(docx_file, "rb") as f:
        st.download_button("Download DOCX", data=f, file_name="application.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", data=f, file_name="application.pdf", mime="application/pdf")