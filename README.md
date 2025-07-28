# 🧠 PDF Outline Extractor — Karya-Manan Team

This project extracts a **structured outline** from any PDF, including:

- 📘 **Title**
- 🧩 **Headings**: H1, H2, and H3 (with levels and page numbers)

---

## 🚀 Problem Statement: *Understand Your Document*

PDFs are rich in content but poor in structure. Our goal is to **convert unstructured PDFs into structured outlines** — enabling smarter **search, indexing, and navigation** for use cases like:

- Government forms  
- Academic syllabi or certificates  
- Informational brochures  
- Event invitations  
- Flyers and posters

---

## 🛠️ Our Approach

### 🔍 PDF Parsing with `PyMuPDF` (`fitz`)
- Efficient, fast, and CPU-friendly
- Extracts fonts, sizes, boldness, and positions from every page
- Works in <10s even for large PDFs

### 🧩 Heading Detection Strategy
- Analyzes **font size**, **boldness**, and **structural patterns**
- Identifies **top N frequent font sizes** and maps them to:
  - H1 → Largest
  - H2 → Medium
  - H3 → Smallest
- Ignores irrelevant content like URLs, copyright notes, etc.

### 🏷️ Title Detection
- Extracts the **largest bold heading** on the first 2 pages
- Falls back to `"Untitled"` if nothing suitable is found

---

## ✅ Output Format

```json
{
  "title": "Sample Title",
  "outline": [
    { "level": "H1", "text": "Chapter 1", "page": 2 },
    { "level": "H2", "text": "Background", "page": 3 },
    ...
  ]
}

'''bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .

docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier
