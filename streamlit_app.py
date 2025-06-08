# streamlit_app.py

import streamlit as st
from fetch.arxiv_scraper import fetch_arxiv_papers, download_pdf
from fetch.pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="Research Paper Viewer", layout="wide")

st.title("📄 Full Research Paper Viewer (arXiv)")
st.markdown("Enter a topic to search and read full research paper content from arXiv.")

topic = st.text_input("🔍 Enter research topic")

if topic.strip():
    with st.spinner("Searching and processing the most relevant paper..."):
        papers = fetch_arxiv_papers(topic, max_results=1)

        if not papers:
            st.error("❌ No papers found for the topic.")
        else:
            paper = papers[0]
            st.success(f"✅ Title: {paper['title']}")
            st.markdown(f"[🔗 Open PDF in browser]({paper['pdf_link']})")

            pdf_path = download_pdf(paper["pdf_link"])
            full_text = extract_text_from_pdf(pdf_path)

            st.subheader("📝 Full Paper Content")
            st.text_area("Full Text", full_text, height=800)
else:
    st.info("⏳ Please enter a topic to get started.")
