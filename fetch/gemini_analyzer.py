# fetch/gemini_analyzer.py

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)  # Replace with your actual key

def analyze_papers_with_gemini(papers_text):
    """
    Takes a list of strings (each string = full content of one paper),
    and generates analysis using Gemini.
    """
    try:
        combined_content = "\n\n---\n\n".join(papers_text)
        prompt = f"""
                You are a professional research analyst and technical reviewer. Given the full texts of three research papers below, perform an expert-level comparative and analytical study. Provide the following details in a structured report:

        1. **Title Identification**: Identify the title and brief summary of each paper.
        2. **Key Innovations**: Describe the unique contributions and novel approaches used in each paper.
        3. **Comparative Analysis**:
        - What are the methodological and conceptual similarities and differences?
        - How do the experimental results compare?
        - Which paper offers more practical or scalable solutions?
        4. **Differentiating Factors**: Highlight what sets each paper apart in terms of approach, application, or impact.
        5. **Critical Review**: 
        - Strengths and weaknesses of each work
        - Any observed gaps or limitations
        6. **Trends and Research Gaps**: What patterns can be derived from these papers, and what research problems are still unexplored?
        7. **Recommendations**:
        - Future work suggestions
        - Potential improvements
        - Ideas for extension

        Text:
        {combined_content}
        """

        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini Analysis Error: {e}"
