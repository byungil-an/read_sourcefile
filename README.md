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
- get_file_from_github(github_url,token)
  - Input:
	github_url⇒Source code URL on github
	token⇒User's github api token
  - Return:text⇒character string
- extract_code_and_comments_from_ipynb(ipynb_content)
  - Input:ipynb_content⇒ipynb file object in notebook format
  - Return:text⇒character string