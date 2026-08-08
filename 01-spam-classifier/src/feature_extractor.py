
SPAM_KEYWORDS = { "win", "free", "claim", "prize", "cash", "reward", "urgent"}
CONTACT_WORDS = { "call", "txt", "text", "reply", "sms"}


def extract_features(text):
    text_lower = text.lower()

    contains_spam_keyword = any(word in text_lower for word in SPAM_KEYWORDS)
    
    contains_contact_request = any(word in text_lower for word in CONTACT_WORDS)
    
    uppercase_word_count = sum(
        1 for word in text.split()
        if len(word) > 1 and word.upper()
    )

    digit_count = sum(
        1 for ch in text
        if ch.isdigit()
    )

    exclamation_count = text.count("!")

    contains_link = int(
        "http" in text_lower
        or "www" in text_lower
    )
    return{
        "contains_spam_keyword" : int(contains_spam_keyword),
        "contains_contact_request": int(contains_contact_request),
        "contains_link" : contains_link,
        "message_length" : len(text),
        "uppercase_word_count" : uppercase_word_count,
        "digit_count" : digit_count,
        "exclamation_count" : exclamation_count
    }
    
    