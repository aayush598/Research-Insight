# fetch/arxiv_scraper.py

import requests
import xml.etree.ElementTree as ET
import os

def fetch_arxiv_papers(topic, max_results=5):
    """
    Fetch research papers from arXiv related to the given topic.
    """
    base_url = "http://export.arxiv.org/api/query?"
    query = f"search_query=all:{topic}&start=0&max_results={max_results}"
    response = requests.get(base_url + query)

    if response.status_code != 200:
        raise Exception("Failed to fetch data from arXiv.")

    root = ET.fromstring(response.content)
    ns = {'arxiv': 'http://www.w3.org/2005/Atom'}

    papers = []

    for entry in root.findall('arxiv:entry', ns):
        title = entry.find('arxiv:title', ns).text.strip().replace("\n", " ")
        summary = entry.find('arxiv:summary', ns).text.strip().replace("\n", " ")
        authors = [author.find('arxiv:name', ns).text for author in entry.findall('arxiv:author', ns)]
        id_link = entry.find('arxiv:id', ns).text
        pdf_link = id_link.replace('abs', 'pdf') + ".pdf"

        papers.append({
            "title": title,
            "summary": summary,
            "authors": authors,
            "link": id_link,
            "pdf_link": pdf_link
        })

    return papers

def download_pdf(pdf_url, save_dir="data/pdfs"):
    """
    Downloads a PDF from arXiv and saves it locally.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    filename = pdf_url.split('/')[-1]
    path = os.path.join(save_dir, filename)

    response = requests.get(pdf_url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        return path
    else:
        raise Exception("Failed to download PDF.")
