
# 📚 Research Insight

A powerful research assistance tool that fetches, stores, and analyzes full-text research papers from **arXiv** based on any topic, powered by **Gemini AI**. It helps researchers quickly understand innovations, methodologies, and trends in selected domains — all via an interactive **Streamlit UI**.



## 🚀 Features

- 🔍 **Topic-Based Search**: Enter any research topic to fetch top 3 recent papers from arXiv.
- 📄 **Full-Text Extraction**: Automatically downloads and extracts the complete content from PDF.
- 📊 **Gemini AI Analysis**: Generates professional summaries, methodologies, comparisons, uniqueness factors, and insights.
- 💾 **SQLite Storage**: Stores paper content and Gemini analysis for future access.
- 🔁 **Reusability**: Automatically loads cached content to reduce redundant API calls and scraping.
- 🌐 **Streamlit UI**: Easy-to-use web interface for researchers and developers.

---

## 🧠 Tech Stack

- 🐍 **Python 3.8+**
- 🌐 **Streamlit** – Interactive frontend
- 📑 **arXiv API + PDF Scraping**
- 🧠 **Gemini API** – AI-powered analysis
- 🗃️ **SQLite** – Persistent storage
- 🔐 **dotenv** – Secure API key management

---

## 📦 Folder Structure

```

research-insight/
│
├── streamlit_app.py              # Main Streamlit UI
├── .env                          # API Key stored securely
├── requirements.txt              # Python dependencies
├── research_insight.db           # SQLite database
└── fetch/
├── arxiv\_scraper.py          # arXiv search and PDF download
├── pdf\_reader.py             # Extracts text from PDFs
├── gemini\_analyzer.py        # Gemini AI API integration
└── db\_manager.py             # SQLite database handler

```


## 🛠️ Setup Instructions

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/research-insight.git
cd research-insight
````

### 2. 🐍 Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 4. 🔑 Set Your Gemini API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

Go to `http://localhost:8501` in your browser.

---

## 🧪 Example Usage

1. Enter a topic like: `AI in Healthcare`
2. Click `Submit`
3. View:

   * Full research paper content
   * Gemini-generated deep analysis:

     * Methodologies
     * Results
     * Comparisons
     * Innovations
     * Literature Summary
     * Uniqueness & Differentiability

---

## 📌 Future Improvements

* Export Gemini report to **PDF**
* Add **filtering and search** for saved papers
* Support for other databases like **IEEE**, **Springer**, or **ACM**
* Display keyword clouds and citation graphs

---

## 🤝 Contribution

Pull requests and issues are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit and push
4. Open a PR 🚀

---

## 📜 License

MIT License – feel free to use, modify, and share with attribution.

---

## 📫 Contact

**Aayush Gid** – [LinkedIn](https://www.linkedin.com/in/aayush-gid-3767a2221/) | [Email](mailto:aayushgid598@gmail.com)

---
