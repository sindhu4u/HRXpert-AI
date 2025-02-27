import fitz  # PyMuPDF

def extract_text_and_hyperlinks_from_pdf(pdf_path):
    text = ""
    hyperlinks = []

    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Extract text
        text += page.get_text()

        # Extract hyperlinks
        links = page.get_links()
        for link in links:
            if link.get("uri"):  # Check if it's a URI (hyperlink)
                hyperlinks.append(link["uri"])

    return text, hyperlinks


