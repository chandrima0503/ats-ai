import pdfplumber
from io import BytesIO
import re
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_name(text: str) -> str:
    # Split text into lines and strip whitespace
    lines = [line.strip() for line in text.strip().split("\n") if line.strip()]

    # 1. Try first line: if it looks like a name (two words, both capitalized)
    if lines:
        first_line = lines[0]
        if re.match(r'^[A-Z][a-zA-Z\-]+ [A-Z][a-zA-Z\-]+$', first_line):
            return first_line

    # 2. Try spaCy PERSON entities (with at least two words)
    doc = nlp(text)
    people = [ent.text.strip() for ent in doc.ents if ent.label_ == "PERSON" and len(ent.text.split()) >= 2]
    if people:
        return people[0]

    # 3. Fallback: search first 5 lines for a likely name
    for line in lines[:5]:
        if re.match(r'^[A-Z][a-zA-Z\-]+ [A-Z][a-zA-Z\-]+$', line):
            return line

    return "Unknown"

async def extract_text(file):
    content = await file.read()
    text = ""

    if file.filename.endswith(".pdf"):
        with pdfplumber.open(BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    return text

def extract_skills(text: str) -> list[str]:
    skills_keywords = ["Python", "Java", "JavaScript", "React", "ML", "SQL", "Docker", "Kubernetes"]
    return [skill for skill in skills_keywords if skill.lower() in text.lower()]

def extract_metadata(text):
    return {
        "name": extract_name(text),
        "skills": extract_skills(text),
        "summary": text[:500]
    }
