import pandas as pd

df = pd.read_csv("phishing_dataset/malicious_phish.csv")

print(df.shape)
print(df.head())