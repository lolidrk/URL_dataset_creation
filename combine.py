import pandas as pd
import random

benign_df = pd.read_csv('ISCXURL2016/FinalDataset/URL/Benign_list_big_final.csv', names=['URL'], header=None)
malicious_df = pd.read_csv('filtered_malicious_urls.csv', names=['URL'], header=None)

num_samples = min(len(benign_df), len(malicious_df))
benign_samples = benign_df.sample(n=num_samples, random_state=42)
malicious_samples = malicious_df.sample(n=num_samples, random_state=42)

benign_samples['Type'] = 'Benign'
malicious_samples['Type'] = 'Malicious'

combined_df = pd.concat([benign_samples, malicious_samples], ignore_index=True)
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)


combined_df.to_csv('combined_dataset.csv', index=False)