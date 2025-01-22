import io
import nbformat

# Get the contents of a text file as a string
def read_txtfile(file_obj):
    # Read the contents of a text file as a string
    stringio = io.StringIO(file_obj.getvalue().decode("utf-8"))
    text = stringio.read()
    return text

# A function to get the contents (nbformat) of a file with the extension ipynb
def read_ipynb(file_obj):
    # Read the contents from the object directly into memory
    file_content = file_obj.read().decode("utf-8")
    # Read the file contents with nbformat
    notebook = nbformat.reads(file_content, as_version=4)
    return notebook

# A function that separates the contents of a file with the extension ipynb into comments and code and obtains them as strings.
def extract_code_and_comments(notebook):
    text = ""
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Processing code cells
            text += "\n# Code start\n"
            text += "\n".join(cell['source'])  # Add code as text
            text += "\n# Code end\n"
        
        elif cell['cell_type'] == 'markdown':
            # Comment (Markdown cell) processing
            text += "\n# Markdown start\n"
            text += "\n".join(cell['source'])  # Add comment as is
            text += "\n# Markdown end\n"
    
    return text


