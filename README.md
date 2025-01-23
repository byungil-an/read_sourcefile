# Library for reading source files

## Description
This library can convert txt (.txt, .py) and notebook (.ipynb) files containing python source code into strings.

## Functions of this library
- read_ipynb(file_obj)
  - Input:file_obj⇒Objects such as file objects and io.BytesIO.
  - Return:notebook⇒Python dictionary type object representing the contents of Jupyter Notebook 
- extract_code_and_comments(notebook)
  - Input:notebook⇒Python dictionary type object representing the contents of Jupyter Notebook 
  - Return:text⇒character string
- read_txtfile(file_obj)
  - Input:file_obj⇒Objects such as file objects and io.BytesIO.
  - Return:text⇒character string

