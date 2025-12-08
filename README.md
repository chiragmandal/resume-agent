# Smart Resume & Cover-Letter Agent

An **Agentic AI app** built with **LangChain + Streamlit**, designed to automatically generate **tailored resumes and cover letters** for any job description — and export them as **PDF / DOCX** files.



## Overview

This project showcases an **end-to-end agentic AI workflow**:
- Input any job description
- Provide your master resume text
- The agent tailors your content using an LLM
- Generates a personalized **resume summary** and **cover letter**
- Exports outputs to **PDF** and **DOCX**



##  Architecture Diagram

```text
            ┌────────────────────────────────────────┐
            │           User Interface (UI)          │
            │           ───────────────────          │
            │            Streamlit Web App           │
            └────────────────────────────────────────┘
                              │
                              ▼
            ┌────────────────────────────────────────┐
            │         LangChain Agent Layer          │
            │ ───────────────────────────────────────│
            │  • Resume Tailoring Chain              │
            │  • Cover Letter Generation Chain       │
            └────────────────────────────────────────┘
                              │
                              ▼
            ┌────────────────────────────────────────┐
            │           LLM Backend Options          │
            │ ───────────────────────────────────────│
            │  • OpenAI GPT-4o (online)              │
            │  • Ollama Llama-3 (local)              │
            │  • Hugging Face Mistral (API)          │
            └────────────────────────────────────────┘
                              │
                              ▼
            ┌────────────────────────────────────────┐
            │         Output & Export Layer          │
            │ ───────────────────────────────────────│
            │  • python-docx → DOCX                  │
            │  • xhtml2pdf  → PDF                    │
            │  • Future: RAG + ChromaDB              │
            └────────────────────────────────────────┘
```


## Folder Structure

```text

resume-agent/
│
├── src/
│   ├── main.py                      # Streamlit entry point
│   ├── config.py                    # LLM setup (OpenAI / Ollama)
│   ├── chains/
│   │   ├── resume_chain.py
│   │   └── cover_letter_chain.py
│   ├── utils/
│   │   ├── export_utils.py          # PDF & DOCX generation
│   │   ├── file_utils.py
│   │   └── vector_store.py          # (for future RAG integration)
│   └── __init__.py
│
├── data/
│   ├── examples/
│   │   ├── resume_master.md
│   │   ├── cover_letter_template.md
│   │   └── job_description_sample.txt
│   └── vector_store/
│
├── docs/
│   ├── architecture.md
│   └── roadmap.md
│
├── .env.template
├── requirements.txt
├── duty.py
└── README.md

```

## Setup Guide

1. Clone the repository

```text 

git clone https://github.com/chiragmandal/resume-agent.git
cd resume-agent

```

2. Create and activate the virtual environment


```text

python3 -m venv .venv
source .venv/bin/activate     # macOS/Linux
# .venv\Scripts\activate      # Windows

```

3. Install Dependancies

```text

pip install --upgrade pip
pip install -r requirements.txt

```

4. Configure the environment

Copy the template

```text

cp .env.template .env

```

5. Choose your LLM backend

    ### a. OpenAI GPT-4o

        1. Get your API key: https://platform.openai.com/api-keys

        2. Add to .env:

            ```bash

                OPENAI_API_KEY=sk-your-key
                MODEL_NAME=gpt-4o
                BACKEND=openai

            ```

    ### b. Ollama (Free & Local)

        1. Install Ollama → https://ollama.com/download

        2. Pull a model:

            ```bash

                ollama pull llama3

            ```

        3. Set in .env:

            ```bash

                BACKEND=ollama
                MODEL_NAME=llama3

            ```

    ### c. Hugging Face (Mistral Model)

        1. Create token → https://huggingface.co/settings/tokens

        2. Add to .env:

            ```bash

                HF_API_TOKEN=hf_your_token
                BACKEND=huggingface
                MODEL_NAME=mistralai/Mistral-7B-Instruct

            ```

6. Run the app

    ```text

    python -m streamlit run src/main.py

    ```

    Then open http://localhost:8501

## Usage
1. Paste your job description
2. Paste your resume text (or use samples in data/examples/)
3. Click Generate
4. View the tailored resume + cover letter
5. Download as PDF or DOCX


## Docker Usage
```text

docker build -t resume-agent .
docker run -p 8501:8501 --env-file .env resume-agent

```



