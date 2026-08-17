# Project 01 - Spam Classifier

## Objective

Build a Spam classifier from scratch while learning the fundamental concepts behind Machine Learning

This project focuses on understanding :

- Data Exploration
- Feature Engineering
- Logistic Regression
- Model Training
- Feature Importance
- Manual vs Automatic Feature Generation

---

## Learning Journey

This project follows the evolution of a typical Machine Learning workflow :

```text
                    Raw SMS Text
                        |
                        v
                Data Exploration
                        |
                        v
                Feature Engineering
                        |
                        v
                Logistic Regression
                        |
                        v
                Model Evaluation
                        |
                        v
            TF-IDF Feature Generation
                        |
                        v
            Feature Importance Analysis
```

---

## Dataset

Dataset used :
- SMS Spam Collection Dataset (UCI Machine Learning Repository)

Dataset Statistics :
- Total Messages : 5574
- Ham Messages : 4827
- Spam Messages : 747

Observations : 
- Dataset is highly imbalanced
- Approximately 87% Ham
- Approximately 13% Spam

This demonstrat why accuracy alone is not always a good metric.

---

## Phase 1 - Understanding the Data

Before writing any ML Code, the dataset was manually inspected.

Observed spam pattern included :
- Free offers
- Prize claims
- Urgent requests
- Call/Text instructions
- Mobile numbers
- Promotional links

Examples : 
```text
FREE entry....
URGENT!....
Claim your prize...
Reply Stop....
```

---

## Phase 2 - Manual Feature Engineering

Instead of letting model learn directly from text, manually designed features were created.

Features : 

- contains_spam_keyword
- contains_contact_request
- contains_link
- message_length
- uppercase_word_count
- digit_count
- exclamation_count

Example :
```text
Input :
URGENT! Call 99999 now

Features :
{
    contains_spam_keyword : 1,
    contains_contact_request : 1,
    contains_link : 0,
    message_length : 22,
    uppercase_word_count : 1,
    digit_count : 5,
    exclamation_count : 1
}
```

Learning: 
- Feature Engineering require domain understanding.
- No single feature is sufficient to classify spam.

---

## Phase 3 - Logistic Regression

The manually generated features were then used to train Logistic regression model.

Pipeline : 
```text
                    Raw Message
                        |
                        v
                Feature Extraction
                        |
                        v
                Feature Matrix (X)
                        |
                        v
                Logistic Regression
                        |
                        v
                    Prediction
```

Accuracy : 
```text
97.77%
```

Learned Feature Weights :
```text
contains_link               3.2233
contains_spam_keyword       2.3346
contains_contact_request    1.6769
digit_count                 0.5009
exclamation_count           0.4475
uppercase_word_count        -0.0227
message_length              0.0040
```

Key Insight :

The Model autmatically learned feature importance.

Intresting finding
```text
contains_link
```
was a stronger spam indicator than manually expected.

---

## Phase 4 - TF-IDF Feature Generation

Instead of manually creating feature Tf-IDF was used.

Pipeline : 
```text
                        Raw Message
                            |
                            v
                    TF-IDF Vectorizer
                            |
                            v
            8713 Automatic Generated Features
                            |
                            v
                    Logistic Regression
                            |
                            v
                        Prediction
```

Number of Features : 
```text
8713
```

Accuracy : 
```text
96.23%
```

---

## Why TF-IDF

Manual Features : 
```text
contains_link
contains_spam_keyword
contains_contact_request
```

TF-IDF Features : 
```text
free
claim
txt
call
mobile
prize
win
...
```

Advantages : 
- No manual feature engineering
- Captures thousands of signals automatically

Drawbacks : 

Words are treated independently.

Example : 
```text
win
winner
winning
won
```
became seperate features.

---

## Most Important Spam indicators found by TF-IDF

Examples :
```text
txt 
call 
stop 
text 
free 
www  
claim 
mobile 
uk  
to  
reply 
150p  
or 
50  
from  
your  
won  
service 
win  
prize 
```

Learning  :
The model discovered dpam related words that were never manually engineered.

---
## Key Takeaways
### What this prject taught
- Raw data must be understood before modelling
- Feature engineering directly impacts model quality
- Logistic Regression learns feature importance through weights
- More features donot automatically improve performance
- TF-IDF automates feature generation
- Automic feature generation is one of the reason ML evolved beyng manual feature engineering.

---
## Connection to bigger Journey

This project represents first stage in the evolution of AI systems
```text
                        Manual Features
                                |
                                v
                              TF-IDF
                                |
                                v
                            Embeddings
                                |
                                v
                        Semantic Search
                                |
                                v
                               RAG
                                |
                                v
                              Agents
```

This project covers the foundation needed before moving to :

Project 02 - Semantic Search using Embeddings


