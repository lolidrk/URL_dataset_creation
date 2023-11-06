import pandas as pd
from urllib.parse import urlparse

malicious_df = pd.read_csv('ISCXURL2016/FinalDataset/URL/DefacementSitesURLFiltered.csv', names=['URL'])
'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

The malicious urls have been elect 2500 URLs provided by Zone-H [28]and extend 
the lists by adding URLs of pages reached by crawling the compro-mised sites up
to the third level.

 So,gonna filter out urls whose path is empty or equal to index.html
and urls whose domain is IP address
'''
def filter_to_useful_urls (url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    domain = parsed_url.netloc
    if not path or path == '/index.html' or domain.replace('.', '', 1).isdigit():
        return False
    return True

malicious_df = malicious_df[malicious_df['URL'].apply(filter_to_useful_urls)]
#taking out same same urls
malicious_df = malicious_df.drop_duplicates(subset=['URL'])

malicious_df.to_csv('filtered_malicious_urls.csv', index=False)