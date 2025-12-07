from duty import duty

@duty
def run():
    """Run the Streamlit app."""
    import os
    os.system("streamlit run src/main.py")
