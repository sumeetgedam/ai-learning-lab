from collections import Counter

# from feature_extractor import extract_features

# msg = "URGENT! Call 99999 now"

# print(extract_features(msg))


DATASET_PATH = 'data/SMSSpamCollection'

ham_samples = []
spam_samples = []
labels = []

with open(DATASET_PATH, "r", encoding="utf8") as file:
    for line in file:
        parts = line.strip().split("\t", 1)

        if len(parts) != 2:
            continue
        
        label, text = parts
        labels.append(label)

        if label == "ham" and len(ham_samples) < 5:
            ham_samples.append(text)

        if label == "spam" and len(spam_samples) < 5:
            spam_samples.append(text)

print("Distribution")
print(Counter(labels))

print("\nSpam Samples")
for msg in spam_samples:
    print("-", msg)

print("\nHam Samples")
for msg in ham_samples:
    print("-", msg)