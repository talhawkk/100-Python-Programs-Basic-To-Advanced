from PyPDF2 import PdfReader

def extract_pdf_metadata(pdf_file):
    """Extracts metadata from a PDF file."""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        info = reader.metadata
        
    metadata = {
        "Title": info.get('/Title'),
        "Author": info.get('/Author'),
        "Subject": info.get('/Subject'),
        "Producer": info.get('/Producer'),
        "Creation Date": info.get('/CreationDate'),
        "Modification Date": info.get('/ModDate')
    }
    return metadata

# pdf_file = 'sample.pdf'  # Replace with your PDF file path
metadata = extract_pdf_metadata(pdf_file)
for key, value in metadata.items():
    print(f"{key}: {value}")
