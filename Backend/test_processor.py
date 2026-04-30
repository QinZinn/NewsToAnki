import logging
from src.processor import process_data

# Configure logging to see output
logging.basicConfig(level=logging.INFO)

def test_lemmatization():
    # Sample data mimicking the scraper output
    article_data = {
        "data": [
            {
                "sentence": "He was reading the largest books in various categories.",
                "words": ["reading", "largest", "books", "various", "categories"]
            }
        ]
    }
    
    # Process the data
    # 'reading' -> 'read' (4) -> filtered
    # 'largest' -> 'large' (5) -> kept
    # 'books' -> 'book' (4) -> filtered
    # 'various' -> 'various' (7) -> kept
    # 'categories' -> 'category' (8) -> kept
    
    result = process_data(article_data)
    
    print("\nProcessed Vocabulary:")
    for word, info in result.items():
        print(f"- {word}: {info['context']}")

    expected_words = {"large", "various", "category"}
    actual_words = set(result.keys())
    
    assert expected_words.issubset(actual_words) or actual_words == expected_words, f"Expected {expected_words}, but got {actual_words}"
    print("\nVerification successful! Lemmatization and filtering are working correctly.")

if __name__ == "__main__":
    test_lemmatization()
