# fetch/db_manager.py

import sqlite3
from datetime import datetime

DB_NAME = "research_insight.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table for papers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS research_papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            title TEXT,
            pdf_url TEXT,
            content TEXT,
            timestamp TEXT
        )
    ''')

    # Create table for Gemini analysis
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gemini_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            analysis TEXT,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_paper(topic, title, pdf_url, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO research_papers (topic, title, pdf_url, content, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (topic, title, pdf_url, content, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def save_analysis(topic, analysis):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO gemini_analysis (topic, analysis, timestamp)
        VALUES (?, ?, ?)
    ''', (topic, analysis, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_papers_by_topic(topic):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT title, content FROM research_papers WHERE topic = ?', (topic,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_analysis_by_topic(topic):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT analysis FROM gemini_analysis WHERE topic = ?', (topic,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
