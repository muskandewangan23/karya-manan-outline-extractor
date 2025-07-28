import fitz  # PyMuPDF
import os
import json
import re
from collections import Counter

# ---------- Helper Functions ----------

def is_valid_heading(text):
    text = text.strip()
    if not text:
        return False
    if len(text.split()) <= 1:
        return False
    if re.search(r'https?://|www\.', text):
        return False
    if any(word.lower() in text.lower() for word in ["copyright", "isbn", "@", "harpercollins", "oceanofpdf"]):
        return False
    return True

# ---------- Step 1: Extract Font Info from PDF ----------

def extract_font_data(pdf_path):
    doc = fitz.open(pdf_path)
    lines = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")['blocks']
        for b in blocks:
            if 'lines' in b:
                for l in b['lines']:
                    for span in l['spans']:
                        if not is_valid_heading(span['text']):
                            continue
                        line = {
                            'text': span['text'].strip(),
                            'size': span['size'],
                            'bold': 'bold' in span['font'].lower(),
                            'font': span['font'],
                            'page': page_num + 1
                        }
                        lines.append(line)
    doc.close()
    return lines

# ---------- Step 2: Determine Top Font Sizes ----------

def get_top_font_sizes(lines, top_n=3):
    size_counts = Counter(line['size'] for line in lines)
    top_sizes = [s for s, _ in size_counts.most_common(top_n)]
    return sorted(top_sizes, reverse=True)  # descending order

# ---------- Step 3: Assign Levels to Headings ----------

def assign_heading_levels(lines, top_sizes):
    outline = []
    for line in lines:
        if line['size'] in top_sizes:
            level_index = top_sizes.index(line['size'])
            level = f"H{level_index + 1}"
            outline.append({
                "level": level,
                "text": line['text'],
                "page": line['page']
            })
    return outline

# ---------- Step 4: Detect Title ----------

def detect_title(lines):
    candidates = [line for line in lines if line['bold'] and len(line['text']) > 4 and line['page'] <= 2]
    if not candidates:
        return "Untitled"
    sorted_by_size = sorted(candidates, key=lambda x: x['size'], reverse=True)
    for line in sorted_by_size:
        if is_valid_heading(line['text']):
            return line['text']
    return "Untitled"

# ---------- Step 5: Generate JSON ----------

def generate_outline_json(pdf_path, output_path):
    lines = extract_font_data(pdf_path)
    top_sizes = get_top_font_sizes(lines, top_n=3)
    outline = assign_heading_levels(lines, top_sizes)
    title = detect_title(lines)

    data = {
        "title": title,
        "outline": outline
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON saved to: {output_path}")

# ---------- Step 6: Run Locally or in Colab ----------

if __name__ == "__main__":
    # Example usage — replace with any PDF path
    test_pdf = "input"  # Replace with uploaded file path
    output_json = "output"
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    generate_outline_json(test_pdf, output_json)
