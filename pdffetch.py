import fitz  # PyMuPDF

def extract_text_from_pdfs(pdf_list, keyword):
    """
    Extracts page numbers where the keyword appears in a list of PDFs.
    
    :param pdf_list: List of PDF file paths.
    :param keyword: Keyword to search for.
    :return: Dictionary with PDF filenames as keys and list of page numbers as values.
    """
    results = {}
    
    for pdf in pdf_list:
        doc = fitz.open(pdf)
        pages = []
        
        for page_num in range(len(doc)):
            text = doc[page_num].get_text("text")
            if keyword.lower() in text.lower():
                pages.append(page_num + 1)  # Pages are 1-based
                
        results[pdf] = pages
    
    for result in results:
        print(result, results[result])


pdf_files = "Enter the name of one pdf or a list of pdfs names"
keyword_to_search = "Enter the keyword to fetch in pdf"
result = extract_text_from_pdfs(pdf_files, keyword_to_search)
print(result)
