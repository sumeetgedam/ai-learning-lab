
from feature_extractor import extract_features

DATASET_PATH = "data/SMSSpamCollection"

rows = []
classification_ham = []
classification_spam = []


with open(DATASET_PATH, "r", encoding="utf8") as file:
    for line in file:
        parts = line.strip().split("\t", 1)

        if len(parts) != 2:
            continue
        
        label, text = parts
        features = extract_features(text)
        
        features["label"] = 1 if label == "spam" else 0


        if label == "spam":
            classification_spam.append(text)
            print(label, features)

        rows.append(features)


print("Total rows : ", len(rows))
print("\n First 5 rows")
for row in rows[:5]:
    print(row)

