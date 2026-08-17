from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from feature_extractor import extract_features

DATASET_PATH = "data/SMSSpamCollection"

X = []
y = []

with open(DATASET_PATH, "r", encoding="utf8") as file:
    for line in file:

        parts = line.strip().split("\t", 1)
        if len(parts) != 2:
            continue

        label, text = parts

        features = extract_features(text)

        X.append(
            [
                features["contains_spam_keyword"],
                features["contains_contact_request"],
                features["contains_link"],
                features["message_length"],
                features["uppercase_word_count"],
                features["digit_count"],
                features["exclamation_count"]
            ]
        )

        y.append(1 if label == "spam" else 0)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy : {accuracy:.4f}")

feature_names = [
    "contains_spam_keyword",
    "contains_contact_request",
    "contains_link",
    "message_length",
    "uppercase_word_count",
    "digit_count",
    "exclamation_count"
]

print("\nLearned Weights : ")

for name, weight in zip(feature_names, model.coef_[0]):
    print(f"{name} : {weight:.4f}")


print("\n", sorted(
    zip(feature_names, model.coef_[0]),
    key = lambda x : abs(x[1]),
    reverse=True
))

