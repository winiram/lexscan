import pdfplumber

MAX_PAGES = 100


def extract_text(file) -> str:
    """Extract text from a PDF file object (BytesIO or file-like).

    Returns the extracted text, or raises ValueError for scanned/encrypted PDFs.
    """
    try:
        with pdfplumber.open(file) as pdf:
            if pdf.metadata.get("Encrypted"):
                raise ValueError("This PDF is encrypted and cannot be read.")

            if len(pdf.pages) > MAX_PAGES:
                raise ValueError(
                    f"This PDF has more than {MAX_PAGES} pages. "
                    "Please upload a shorter document or paste the relevant section."
                )

            pages_text = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    pages_text.append(text)

            if not pages_text:
                raise ValueError(
                    "No text could be extracted from this PDF. "
                    "It may be a scanned image — try copying the text manually."
                )

            return "\n\n".join(pages_text)
    except ValueError:
        raise
    except Exception:
        raise ValueError("Failed to parse PDF. The file may be corrupted or in an unsupported format.")
