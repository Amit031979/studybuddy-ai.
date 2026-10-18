import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="StudyBuddy AI", page_icon="📘", layout="centered")
st.title("📘 StudyBuddy AI")
st.caption("A simple Generative AI study assistant")
st.info("AI responses can contain mistakes. Verify important facts with your course material.")

mode = st.selectbox("What would you like to create?", ["Explain a topic", "Revision notes", "Practice quiz"])
topic = st.text_area("Enter your subject or topic", placeholder="Example: DBMS primary keys", height=120)
level = st.selectbox("Explanation level", ["Beginner", "First-year engineering", "Intermediate"])
count = st.slider("Number of quiz questions (used in Practice quiz mode)", 3, 10, 5)

def build_prompt(topic_text, selected_mode, selected_level, number):
    if selected_mode == "Explain a topic":
        task = "Explain the topic clearly with a definition, key points, a simple example, and a short recap."
    elif selected_mode == "Revision notes":
        task = "Create concise revision notes with headings, bullet points, key terms, and one example."
    else:
        task = f"Create {number} practice questions about the topic. Include multiple-choice options, mark the correct answer, and give a one-sentence explanation."
    return (
        f"You are a helpful study assistant. Audience level: {selected_level}. "
        f"Use simple, accurate language. If a topic is ambiguous, state your assumption. "
        f"Do not invent citations. Task: {task}\nTopic: {topic_text}"
    )

if st.button("Generate study material", type="primary", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("API key not found. Set OPENAI_API_KEY in your environment or configure Streamlit secrets.")
            st.code('OPENAI_API_KEY="your_api_key_here"', language="bash")
        else:
            try:
                client = OpenAI(api_key=api_key)
                with st.spinner("Generating your study material..."):
                    response = client.responses.create(
                        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                        input=build_prompt(topic.strip(), mode, level, count)
                    )
                st.subheader("Your study material")
                st.markdown(response.output_text)
                st.download_button(
                    "Download response as text",
                    data=response.output_text,
                    file_name="studybuddy_notes.txt",
                    mime="text/plain"
                )
            except Exception as exc:
                st.error("The request could not be completed. Check your API key, model access, internet connection, and API usage limits.")
                st.caption(f"Technical detail: {exc}")

with st.expander("How to use this app"):
    st.markdown("1. Enter a topic.\\n2. Choose Explain, Revision notes, or Practice quiz.\\n3. Select your learning level.\\n4. Click **Generate study material**.\\n5. Review the answer and verify important facts.")
