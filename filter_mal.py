import pandas as pd
from urllib.parse import urlparse

malicious_df = pd.read_csv('ISCXURL2016/FinalDataset/URL/DefacementSitesURLFiltered.csv')
'''
From 
The malicious urls have been elect 2500 URLs provided by Zone-H [28]and extend 
the lists by adding URLs of pages reached by crawling the compro-mised sites up
to the third level. 
'''
def filter_to_useful_urls (url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    domain = parsed_url.netloc
    if not path or path == '/index.html' or domain.replace('.', '', 1).isdigit():
        return False
    return True

malicious_df = malicious_df[malicious_df['URL'].apply(filter_to_useful_urls)]
malicious_df.to_csv('filtered_malicious_urls.csv', index=False)