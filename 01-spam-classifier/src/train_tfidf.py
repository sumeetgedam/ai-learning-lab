from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

DATASET_PATH = "data/SMSSpamCollection"

texts = []
labels = []

with open(DATASET_PATH, "r", encoding="utf8") as file:
    for line in file:
        parts = line.strip().split("\t", 1)

        if len(parts) != 2:
            continue

        label, text = parts

        texts.append(text)
        labels.append(1 if label == "spam" else 0)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy : ",accuracy)

print("\nNumber of features : ", len(vectorizer.get_feature_names_out()))


print("\n", X.shape)

feature_names = vectorizer.get_feature_names_out()

weights = model.coef_[0]

top_features = sorted(
    zip(feature_names, weights),
    key= lambda x:x[1],
    reverse=True
)

print("\nTop 20 spam words")
for word, weight in top_features[:20]:
    print(word, round(weight, 4))