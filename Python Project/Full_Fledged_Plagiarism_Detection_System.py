import re
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text

def calculate_cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

def main():
    # Load existing sources into a database (list of strings)
    database = [
        "This is an example source document.",
        "Another example document for the database.",
        # Add more documents to the database
    ]
    
    input_text = input("Enter the text to check for plagiarism: ")
    
    # Preprocess input and database documents
    preprocessed_input = preprocess_text(input_text)
    preprocessed_database = [preprocess_text(doc) for doc in database]
    
    # Combine input and database documents for vectorization
    all_documents = [preprocessed_input] + preprocessed_database
    
    # Vectorize documents using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_documents)
    
    # Calculate cosine similarity between input and database documents
    input_vector = tfidf_matrix[0]
    database_vectors = tfidf_matrix[1:]
    
    similarities = []
    for doc_vector in database_vectors:
        similarity = calculate_cosine_similarity(input_vector.toarray(), doc_vector.toarray())
        similarities.append(similarity)
    
    # Find the most similar document in the database
    most_similar_index = np.argmax(similarities)
    most_similar_document = database[most_similar_index]
    highest_similarity = similarities[most_similar_index]
    
    print("Input text:")
    print(input_text)
    print("\nMost similar document in the database:")
    print(most_similar_document)
    print("\nSimilarity score:", highest_similarity)

if __name__ == "__main__":
    main()
