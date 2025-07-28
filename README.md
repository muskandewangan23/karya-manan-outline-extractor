# 🧠 PDF Outline Extractor — Karya-Manan Team

This project extracts a **structured outline** from any PDF, focusing on:

- 📘 **Title**
- 🧩 **Headings** (H1, H2, H3) with their level and page number

---

## 🚀 Problem Statement: *Understand Your Document*

PDFs are rich in content but poor in structure. Our goal is to **convert unstructured PDFs into structured outlines** — enabling smarter **search, summarization, and navigation** across diverse PDF types such as:

- Government forms  
- Academic certifications or syllabi  
- Informational brochures  
- Event flyers and visual leaflets  
- And more...

---

## 🛠️ Approach

### 🔍 PDF Parsing with `PyMuPDF` (`fitz`)

- Lightweight and fast
- Extracts font, size, position, boldness, and page number
- Capable of handling diverse formatting and layouts

### 🧩 Heading Detection Strategy

1. Extract every text span from the PDF
2. **Filter** only meaningful lines (ignoring noise, links, copyright, etc.)
3. Identify top N font sizes
4. Assign heading levels based on font size ranking (e.g., largest = H1, next = H2...)

### 🏷️ Title Detection

- Extracted from the **boldest and largest text** found on the first 2 pages
- Falls back to `"Untitled"` if no valid match is found

---

## ✅ Output Format (JSON)

```json
{
  "title": "Sample Title",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    ...
  ]
}
