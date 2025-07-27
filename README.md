# 🧠 PDF Outline Extractor — Karya-Manan Team

This project extracts a structured outline from a PDF, including:
- 📘 **Title**
- 🧩 **Headings**: H1, H2, and H3 (with levels and page numbers)

---

## 🚀 Problem Statement: "Understand Your Document"
PDFs are rich in content but poor in structure. Our goal is to convert unstructured PDFs into structured outlines — enabling smarter search, indexing, and navigation.

---

## 🛠️ Our Approach

1. **PDF Parsing with PyMuPDF (fitz)**  
   Efficient, fast, and CPU-friendly — it lets us extract fonts, sizes, positions, and text in <10s even for large PDFs.

2. **Heading Detection Strategy**
   - We analyze **font size**, **boldness**, and **patterns**
   - Top N frequent font sizes are mapped to heading levels (H1 > H2 > H3)
   - Content is filtered based on structural heuristics

3. **Title Detection**
   - Title is usually the largest-sized text on the first few pages.
   - If ambiguous, we fallback to "Untitled" and let users rename it.

4. **Output**
   - A clean JSON matching the format:
   ```json
   {
     "title": "Sample Title",
     "outline": [
       { "level": "H1", "text": "Chapter 1", "page": 2 },
       ...
     ]
   }

```bash
docker build --platform linux/amd64 -t karya-manan-solution:abc123xyz .

docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  karya-manan-solution:abc123xyz
