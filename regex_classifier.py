import re
import pandas as pd

#malicious_pattern = r'[^\w\s]|itemid|Itemid|fontstyle|=component'
'''
def classify_url(url):
    if re.search(r"[^\w\s]|itemid|Itemid|fontstyle|=component", url, re.IGNORECASE):
        return "Malicious"
    else:
        return "Benign"
'''
malicious_keywords = ["itemid", "fontstyle", "=component"]
def classify_url(url):
    for keyword in malicious_keywords:
        if keyword in url.lower():
            return "Malicious"
    
    # Check for non-standard characters in the URL
    if re.search(r'[^\x00-\x7F]', url):
        return "Malicious"

    return "Benign"

dataset = pd.read_csv("combined_dataset.csv")
#dataset = dataset.head(5)
correctly_classified = 0
misclassified_urls = []

# Open a text file to store misclassified URLs
with open("misclassified_urls.txt", "w") as misclassified_file:
    for index, row in dataset.iterrows():
        url = row['URL']  # Use 'URL' as the column name
        actual_label = row['Type']  # Use 'Type' as the column name
        predicted_label = classify_url(url)

        if predicted_label == actual_label:
            correctly_classified += 1
        else:
            misclassified_urls.append((url, actual_label, predicted_label))
            misclassified_file.write(f"URL: {url}, Actual: {actual_label}, Predicted: {predicted_label}\n")

accuracy = correctly_classified / len(dataset) * 100

print(f"Accuracy: {accuracy:.2f}%")

# Close the misclassified file
misclassified_file.close()
'''
malicious_pattern = r'[^\w\s]|itemid|Itemid|fontstyle|=component'
url = "http://huamuxtitlan.com/index.php?option=com_k2&view=item&id=54:huamuxtitlรกn-recibe-las-reliquias-del-papa-juan-pablo-ii&Itemid=106"
if re.search(malicious_pattern, url):
    print("malicious")
else:
    print("benign")
'''