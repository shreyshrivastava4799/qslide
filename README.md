# qslide
This repository contains an implementation for querying text in slides stored in a folder. 

## Dependency

https://pypi.org/project/pdftotext/

(Link)[https://stackoverflow.com/questions/45912641/unable-to-install-pdftotext-on-python-3-6-missing-poppler]
sudo apt-get update
sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev

In case of error : ImportError: libiconv.so.2: cannot open shared object file: No such file or directory.
conda install -c r libiconv

pip install pdftotext

## Usage

1. Find the global path to your directory which contains all the pdf files.
2. Run the command from terminal: `python main.py <global-path>`
3. The system would take 2-5 minutes for building an internal dictionary depending upon size and number of slides. 
4. Enter the relevant query as text input in the terminal.

Result: The output on the terminal shows the page in the slide with possible relevant information along with words that matched in the page. I know describe the algorithm in brief so that you can make better queries and thus better results. 

## Example 

1. Directory structure of folder and the associated path. 