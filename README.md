# 🧠 PDF Outline Extractor — Karya-Manan Team
This project extracts a **structured outline** from any PDF, including:
- 📘 **Title**
- 🧩 **Headings**: H1, H2, and H3 (with levels and page numbers)
---
## 🚀 Problem Statement: *Understand Your Document*
PDFs are rich in content but poor in structure. Our goal is to **convert unstructured PDFs into structured outlines**, enabling smarter **search, indexing, and navigation** for:
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
  - `H1` → Largest  
  - `H2` → Medium  
  - `H3` → Smallest
- Ignores irrelevant content (e.g., URLs, copyright)
### 🏷️ Title Detection
- Extracts the **largest bold heading** from the first 2 pages
- Falls back to `"Untitled"` if none found
---
## ✅ Output Format Example
Each PDF in `/app/input` generates a corresponding `.json` in `/app/output`.
Sample output for `sample.pdf` → `sample.json`:
```json
{
  "title": "Sample Title",
  "outline": [
    { "level": "H1", "text": "Chapter 1", "page": 2 },
    { "level": "H2", "text": "Background", "page": 3 }
  ]
}
```
---
## 🐳 Docker Instructions
### 📦 Build the Docker Image
```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

### ▶️ Run the Docker Container
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  mysolutionname:somerandomidentifier
```

**Note:** 
- Place your PDF files in the `input/` directory before running
- Processed JSON files will appear in the `output/` directory
- The container runs with `--network none` for security isolation
