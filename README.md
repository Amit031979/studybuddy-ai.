# StudyBuddy AI — Generative AI Assignment

**Assignment:** Exploring Generative AI and AI Fundamentals  
**Project:** StudyBuddy AI: A Generative AI Study Assistant  
**Author:** Amit Kushwaha

## Overview
StudyBuddy AI is a small Streamlit web app that uses an OpenAI GPT model to generate topic explanations, revision notes, and practice quizzes.

## Features
- Three study modes: explain, revision notes, and quiz
- Adjustable audience level
- Quiz question count selector
- Download generated material as a text file
- Basic input validation and API error handling
- API key kept outside the source code

## Requirements
- Python 3.10 or newer
- An OpenAI API key with API access and available usage/billing
- Internet connection

## Run locally
1. Extract this project folder.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set the API key as an environment variable.

   **Windows PowerShell**
   ```powershell
   $env:OPENAI_API_KEY="your_api_key_here"
   $env:OPENAI_MODEL="gpt-4.1-mini"
   ```

   **macOS/Linux**
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   export OPENAI_MODEL="gpt-4.1-mini"
   ```
6. Start the app:
   ```bash
   streamlit run app.py
   ```

The app opens in your browser. Never commit your API key to GitHub. You can change `OPENAI_MODEL` to a model available to your account.

## Suggested GitHub repository description
A beginner-friendly Generative AI study assistant built with Python, Streamlit, and the OpenAI API. It generates explanations, revision notes, and practice quizzes.

## Limitations and responsible use
Model outputs may be inaccurate or incomplete. Verify important information with trusted learning materials. Do not enter sensitive or confidential information. API usage may incur charges.

## Assignment report
See `Generative_AI_Assignment_Report_Amit_Kushwaha.docx` if you include the report in your repository.
