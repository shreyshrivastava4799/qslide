import os 
import sys
import pdftotext


import re
import nltk
import pickle
import nltk.data

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

from query import find_prefix
from search.boolean import boolRet


# stopwords = code for downloading stop words through nltk
stopword = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# Input: 'global path' 
# text should be repeatedly input and associated text should be output

if __name__ == "__main__":
    
    f_path = sys.argv[1]
    print(f'The input path provided is : {f_path}')


    # create inverted positional index for all the slides in the folder
    InvPosIdx = dict()    
    for s_no, filename in enumerate(os.listdir(f_path)):
        
        if '.pdf' in filename:
            
            with open(f_path+'/'+filename, "rb") as f:
                pdf = pdftotext.PDF(f)

            for pg_no, page in enumerate(pdf):
                tokens = []
                page = re.sub(r'[^\w\s]', ' ', page)
                for sentences in re.split("\n", page):
                    curr_tokens = word_tokenize(sentences, language='english')
                    tokens.extend([lemmatizer.lemmatize(token.lower()) for token in curr_tokens if token not in stopword and token.isalnum()])

                for token in set(tokens):
                    if token not in InvPosIdx.keys():
                        InvPosIdx[token] = set()
                    
                    InvPosIdx[token].add((s_no, pg_no))


    searcher =  boolRet(InvPosIdx)

    # read query from terminal 
    filename_list = os.listdir(f_path)
    while(True):

        print(f'Enter your query:')
        q_words = str(input()).split() 

        search_result = searcher.simpleIntersection(q_words)
        if search_result == None:
            print(f'No results found.')
            continue
        for s_no, pg_no in search_result:
            with open(f_path+'/'+filename_list[s_no], "rb") as f:
                pdf = pdftotext.PDF(f)
            print(f'\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
            print(f'Results from slide: {filename_list[s_no]} and page no. {pg_no}\n')
            print(pdf[pg_no])



