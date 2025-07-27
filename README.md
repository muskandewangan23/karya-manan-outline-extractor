# Karya-Manan Hackathon Submission

## 🔍 Problem Statement
Extract the hierarchical outline (Title, H1, H2, H3 with page numbers) from a PDF document and output a valid JSON structure. This solution is optimized for CPU-only, offline execution under 10 seconds for 50-page PDFs.

---

## 🛠️ Tech Stack
- Language: Python 3.10
- Libraries: 
  - [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)
- Platform: Docker (CPU, AMD64)
- Deployment: Colab + Docker-ready
- Input: PDF files
- Output: Structured JSON outline

---

## 🚀 How It Works

1. All PDF files in `/app/input` are automatically processed.
2. Each file is analyzed for:
   - Title (based on the largest font or first prominent heading)
   - Headings (`H1`, `H2`, `H3`) based on font size and boldness
3. Output JSON files are saved with the same name in `/app/output`.

Example Output Format:
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
