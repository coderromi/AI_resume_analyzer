import os

from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai


# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# Read resume PDF
reader = PdfReader("resume.pdf")

resume_text = ""

for page in reader.pages:
    resume_text += page.extract_text()


print("\n==============================")
print("      AI RESUME ANALYZER")
print("==============================")

print("\nResume loaded successfully!")
print("Characters extracted:", len(resume_text))


# Analyze resume with Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"""
You are an AI resume analyzer.

Analyze the resume below.

Provide:

1. Key technical skills
2. Programming languages
3. Projects
4. Education
5. Strengths
6. Missing or potentially useful skills
7. Specific improvements to make the resume clearer and stronger

Keep the analysis concise.
Use clear headings and bullet points.

IMPORTANT:
Only make observations that can reasonably be supported
by the resume. Do not invent qualifications or experience.

Resume:
{resume_text}
"""
)


print("\n===== AI RESUME ANALYSIS =====")
print(response.text)