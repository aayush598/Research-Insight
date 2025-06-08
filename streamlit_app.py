# streamlit_app.py

import streamlit as st
from fetch.arxiv_scraper import fetch_arxiv_papers, download_pdf
from fetch.pdf_reader import extract_text_from_pdf
from fetch.gemini_analyzer import analyze_papers_with_gemini
from fetch.db_manager import (
    init_db,
    save_paper,
    save_analysis,
    get_papers_by_topic,
    get_analysis_by_topic,
)

init_db()  # Initialize SQLite DB on app start

st.set_page_config(page_title="Research Insight", layout="wide")
st.title("📚 Research Insight Tool")
st.markdown("Get full research papers and detailed Gemini AI analysis based on your topic.")

topic = st.text_input("🔍 Enter a research topic")
submit = st.button("🚀 Submit")

if submit and topic.strip():
    # Check if data already exists
    existing_papers = get_papers_by_topic(topic)
    existing_analysis = get_analysis_by_topic(topic)

    if existing_papers and existing_analysis:
        st.success("🔁 Loaded from local database.")
        for i, (title, content) in enumerate(existing_papers):
            st.markdown(f"### 📄 Paper {i+1}: {title}")
            with st.expander("🔎 View Full Paper"):
                st.markdown(content)

        st.subheader("📊 Gemini AI Analysis")
        st.markdown(existing_analysis)

    else:
        with st.spinner("⏳ Fetching papers and analyzing with Gemini..."):
            papers = fetch_arxiv_papers(topic, max_results=3)

            if not papers:
                st.error("❌ No research papers found for this topic.")
            else:
                paper_texts = []
                for paper in papers:
                    title = paper["title"]
                    pdf_url = paper["pdf_link"]
                    pdf_path = download_pdf(pdf_url)
                    full_text = extract_text_from_pdf(pdf_path)

                    # Store paper
                    save_paper(topic, title, pdf_url, full_text)

                    # Show paper content
                    st.markdown(f"### 📄 {title}")
                    with st.expander("🔎 View Full Paper"):
                        st.markdown(full_text)

                    paper_texts.append(full_text)

                # Get Gemini analysis
                gemini_response = analyze_papers_with_gemini(paper_texts)
                save_analysis(topic, gemini_response)

                st.subheader("📊 Gemini AI Analysis")
                st.markdown(gemini_response)
