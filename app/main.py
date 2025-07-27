import os
import json
import fitz  # PyMuPDF
import re

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def is_junk(text):
    junk_keywords = ['copyright', 'isbn', 'www.', 'http', 'harpercollins', 'oceanofpdf', 'all rights reserved']
    return any(kw.lower() in text.lower() for kw in junk_keywords)

def is_title_case(text):
    if text.isupper():
        return True
    words = text.split()
    if not words:
        return False
    capitalized = [w[0].isupper() for w in words if w[0].isalpha()]
    return sum(capitalized) >= len(words) * 0.8

def extract_blocks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks_on_page = page.get_text("dict")["blocks"]

        for block in blocks_on_page:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = ""
                    font_sizes = []
                    is_bold = False

                    for span in line["spans"]:
                        line_text += span["text"]
                        font_sizes.append(span["size"])
                        if "bold" in span["font"].lower():
                            is_bold = True

                    if line_text.strip():
                        avg_font_size = sum(font_sizes) / len(font_sizes)
                        blocks.append({
                            "text": line_text.strip(),
                            "size": avg_font_size,
                            "bold": is_bold,
                            "page": page_num + 1
                        })
    return blocks

def classify_headings(blocks):
    headings = []

    for block in blocks:
        text = block["text"].strip()
        if not text or is_junk(text):
            continue
        if len(text.split()) > 10:
            continue
        if any(p in text for p in [".", ",", "?", "\"", "”", "“", "'"]):
            continue
        if not is_title_case(text):
            continue
        if re.match(r"^\d+$", text):
            continue

        size = block["size"]
        page = block["page"]

        if size >= 17:
            level = "H1"
        elif size >= 15:
            level = "H2"
        elif size >= 13:
            level = "H3"
        else:
            continue

        headings.append({
            "level": level,
            "text": text,
            "page": page
        })

    return headings

def extract_title(blocks):
    filtered = [b for b in blocks if not is_junk(b["text"]) and len(b["text"].split()) <= 10]
    if not filtered:
        return "Untitled"
    top = max(filtered, key=lambda b: b["size"])
    return top["text"]

def process_pdf(pdf_path, output_path):
    blocks = extract_blocks_from_pdf(pdf_path)
    headings = classify_headings(blocks)
    title = extract_title(blocks)

    output = {
        "title": title,
        "outline": headings
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Processed: {os.path.basename(pdf_path)}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            process_pdf(pdf_path, output_path)

if __name__ == "__main__":
    main()
