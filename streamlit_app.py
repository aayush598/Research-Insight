# streamlit_app.py

import streamlit as st
from fetch.arxiv_scraper import fetch_arxiv_papers, download_pdf
from fetch.pdf_reader import extract_text_from_pdf
from fetch.gemini_analyzer import analyze_papers_with_gemini

st.set_page_config(page_title="AI Research Analyzer", layout="wide")

st.title("🧠 AI-Powered Research Paper Analyzer")
st.markdown("Enter a topic to analyze 3 recent arXiv papers using Gemini AI.")

topic = st.text_input("🔍 Enter research topic")

if topic.strip():
    with st.spinner("🔍 Fetching papers..."):
        papers = fetch_arxiv_papers(topic, max_results=3)

        if not papers:
            st.error("No papers found.")
        else:
            paper_texts = []
            for i, paper in enumerate(papers):
                st.markdown(f"### Paper {i+1}: {paper['title']}")
                st.markdown(f"[📄 Open PDF]({paper['pdf_link']})")

                pdf_path = download_pdf(paper["pdf_link"])
                full_text = extract_text_from_pdf(pdf_path)
                paper_texts.append(full_text)

    with st.spinner("🤖 Generating Gemini analysis..."):
        gemini_response = analyze_papers_with_gemini(paper_texts)

    st.subheader("📊 Gemini Analysis")
    st.markdown(gemini_response)
else:
    st.info("⏳ Please enter a topic to get started.")
