import sys
import argparse
import fitz # PyMuPDF

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
    return results



def extract_pdfs_name(path):
    '''
    PDFs name list are in .txt file. This fuction will extract that
    and return as list from the text file in the path
    '''

    with open(path, 'r') as file:
        pdf_names = file.readlines()
        
    return [name.strip() for name in pdf_names]



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python fetchinpdf.py -f <fileName> -s <keyword>")
        sys.exit(1)
    
    parser = argparse.ArgumentParser(description="PDF content page fetcher")

    parser.add_argument('-f', '--file', type=str) 
    parser.add_argument('-s', '--search', type=str)

    args = parser.parse_args()

    pdfs = extract_pdfs_name(args.file) # PDFs names are extracted and stored as list
    result = extract_text_from_pdfs(pdfs, args.search) # output is stored as dictionary


    # Print the final output

    for res in result:
        print("-+"*5)
        print(res, result[res])
