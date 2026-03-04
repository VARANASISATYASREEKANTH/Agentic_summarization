from pypdf import PdfReader
from google.adk.tools import FunctionTool

def extract_pdf_text(file_path: str) -> str:
    """Extract text from a PDF file given its path."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


# Wrap function directly (NO name=, NO description=)
extract_pdf_tool = FunctionTool(extract_pdf_text)