"""
TF-IDF Calculator for RAG Keyword Search

This module implements Term Frequency-Inverse Document Frequency calculation
for use in Retrieval-Augmented Generation (RAG) systems.
"""

import math
from collections import Counter
from typing import List, Dict, Tuple


class TFIDFCalculator:
    """
    A class to calculate TF-IDF scores for documents and queries.
    
    TF-IDF = TF(term, document) * IDF(term, corpus)
    
    Where:
    - TF (Term Frequency): How frequently a term appears in a document
    - IDF (Inverse Document Frequency): How rare or common a term is across all documents
    """
    
    def __init__(self):
        self.documents = []
        self.vocabulary = set()
        self.idf_scores = {}
    
    def preprocess_text(self, text: str) -> List[str]:
        """
        Preprocess text by converting to lowercase and splitting into tokens.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            List[str]: List of preprocessed tokens
        """
        # Simple preprocessing - convert to lowercase and split by spaces
        # In practice, you might want to use more sophisticated tokenization
        return text.lower().split()
    
    def calculate_tf(self, term: str, document: List[str]) -> float:
        """
        Calculate Term Frequency (TF) for a term in a document.
        
        TF = (Number of times term appears in document) / (Total number of terms in document)
        
        Args:
            term (str): The term to calculate TF for
            document (List[str]): List of tokens in the document
            
        Returns:
            float: Term frequency score
        """
        if len(document) == 0:
            return 0.0
        
        term_count = document.count(term)
        total_terms = len(document)
        
        return term_count / total_terms
    
    def calculate_idf(self, term: str, documents: List[List[str]]) -> float:
        """
        Calculate Inverse Document Frequency (IDF) for a term across all documents.
        
        IDF = log(Total number of documents / Number of documents containing the term)
        
        Args:
            term (str): The term to calculate IDF for
            documents (List[List[str]]): List of all documents (each as list of tokens)
            
        Returns:
            float: Inverse document frequency score
        """
        total_documents = len(documents)
        documents_with_term = sum(1 for doc in documents if term in doc)
        
        if documents_with_term == 0:
            return 0.0
        
        return math.log(total_documents / documents_with_term)
    
    def fit(self, documents: List[str]):
        """
        Fit the TF-IDF calculator on a corpus of documents.
        
        Args:
            documents (List[str]): List of document strings
        """
        self.documents = [self.preprocess_text(doc) for doc in documents]
        
        # Build vocabulary
        for doc in self.documents:
            self.vocabulary.update(doc)
        
        # Calculate IDF for each term in vocabulary
        for term in self.vocabulary:
            self.idf_scores[term] = self.calculate_idf(term, self.documents)
    
    def calculate_tfidf_vector(self, text: str) -> Dict[str, float]:
        """
        Calculate TF-IDF vector for a given text (query or document).
        
        Args:
            text (str): Input text to calculate TF-IDF for
            
        Returns:
            Dict[str, float]: Dictionary mapping terms to their TF-IDF scores
        """
        if not self.documents:
            raise ValueError("Must call fit() with documents before calculating TF-IDF")
        
        tokens = self.preprocess_text(text)
        tfidf_vector = {}
        
        for term in tokens:
            if term in self.vocabulary:
                tf = self.calculate_tf(term, tokens)
                idf = self.idf_scores[term]
                tfidf_vector[term] = tf * idf
        
        return tfidf_vector
    
    def get_top_keywords(self, text: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Get the top-k keywords from text based on TF-IDF scores.
        
        Args:
            text (str): Input text to extract keywords from
            top_k (int): Number of top keywords to return
            
        Returns:
            List[Tuple[str, float]]: List of (keyword, score) tuples sorted by score
        """
        tfidf_vector = self.calculate_tfidf_vector(text)
        
        # Sort by TF-IDF score in descending order
        sorted_terms = sorted(tfidf_vector.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_terms[:top_k]


def demo_tfidf_calculation():
    """
    Demonstrate TF-IDF calculation with sample documents.
    """
    print("=== TF-IDF Calculator Demo ===\n")
    
    # Sample corpus of documents
    documents = [
        "The cat sat on the mat",
        "The dog ran in the park",
        "Cats and dogs are pets",
        "I love my pet cat very much",
        "The park has many trees and flowers"
    ]
    
    # Initialize and fit the TF-IDF calculator
    tfidf_calc = TFIDFCalculator()
    tfidf_calc.fit(documents)
    
    print("Corpus of documents:")
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc}")
    
    print(f"\nVocabulary size: {len(tfidf_calc.vocabulary)}")
    print(f"Vocabulary: {sorted(tfidf_calc.vocabulary)}")
    
    # Test with a query sentence
    query = "I want to find information about cats in the park"
    print(f"\nQuery: '{query}'")
    
    # Calculate TF-IDF vector for the query
    tfidf_vector = tfidf_calc.calculate_tfidf_vector(query)
    print(f"\nTF-IDF vector for query:")
    for term, score in sorted(tfidf_vector.items(), key=lambda x: x[1], reverse=True):
        print(f"  {term}: {score:.4f}")
    
    # Get top keywords
    top_keywords = tfidf_calc.get_top_keywords(query, top_k=3)
    print(f"\nTop 3 keywords from query:")
    for i, (keyword, score) in enumerate(top_keywords, 1):
        print(f"  {i}. {keyword}: {score:.4f}")
    
    # Demonstrate with individual documents
    print(f"\n=== TF-IDF Analysis for Each Document ===")
    for i, doc in enumerate(documents, 1):
        print(f"\nDocument {i}: '{doc}'")
        doc_tfidf = tfidf_calc.calculate_tfidf_vector(doc)
        top_terms = sorted(doc_tfidf.items(), key=lambda x: x[1], reverse=True)[:3]
        print("Top 3 terms:")
        for term, score in top_terms:
            print(f"  {term}: {score:.4f}")


if __name__ == "__main__":
    demo_tfidf_calculation()