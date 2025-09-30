"""
TF-IDF Document Ranking for RAG Systems

This script demonstrates how to use TF-IDF to rank documents 
based on their relevance to a query sentence.
"""

import math
from tfidf_calculator import TFIDFCalculator
from typing import List, Tuple


class DocumentRanker:
    """
    Document ranking system using TF-IDF similarity scores.
    """
    
    def __init__(self):
        self.tfidf_calc = TFIDFCalculator()
        self.documents = []
        self.document_vectors = []
    
    def fit(self, documents: List[str]):
        """
        Fit the ranker with a collection of documents.
        
        Args:
            documents (List[str]): List of document strings
        """
        self.documents = documents
        self.tfidf_calc.fit(documents)
        
        # Pre-calculate TF-IDF vectors for all documents
        self.document_vectors = []
        for doc in documents:
            doc_vector = self.tfidf_calc.calculate_tfidf_vector(doc)
            self.document_vectors.append(doc_vector)
    
    def cosine_similarity(self, vec1: dict, vec2: dict) -> float:
        """
        Calculate cosine similarity between two TF-IDF vectors.
        
        Args:
            vec1 (dict): First TF-IDF vector
            vec2 (dict): Second TF-IDF vector
            
        Returns:
            float: Cosine similarity score (0-1)
        """
        # Get all unique terms
        all_terms = set(vec1.keys()) | set(vec2.keys())
        
        if not all_terms:
            return 0.0
        
        # Create vectors using pure Python
        v1 = [vec1.get(term, 0) for term in all_terms]
        v2 = [vec2.get(term, 0) for term in all_terms]
        
        # Calculate dot product
        dot_product = sum(a * b for a, b in zip(v1, v2))
        
        # Calculate norms
        norm_v1 = math.sqrt(sum(a * a for a in v1))
        norm_v2 = math.sqrt(sum(b * b for b in v2))
        
        if norm_v1 == 0 or norm_v2 == 0:
            return 0.0
        
        return dot_product / (norm_v1 * norm_v2)
    
    def rank_documents(self, query: str, top_k: int = None) -> List[Tuple[int, str, float]]:
        """
        Rank documents by relevance to the query using TF-IDF similarity.
        
        Args:
            query (str): Query string
            top_k (int): Number of top results to return (None for all)
            
        Returns:
            List[Tuple[int, str, float]]: List of (index, document, score) tuples
        """
        query_vector = self.tfidf_calc.calculate_tfidf_vector(query)
        
        # Calculate similarity scores
        scores = []
        for i, doc_vector in enumerate(self.document_vectors):
            similarity = self.cosine_similarity(query_vector, doc_vector)
            scores.append((i, self.documents[i], similarity))
        
        # Sort by similarity score (descending)
        scores.sort(key=lambda x: x[2], reverse=True)
        
        if top_k is not None:
            scores = scores[:top_k]
        
        return scores


def demo_document_ranking():
    """
    Demonstrate document ranking with TF-IDF.
    """
    print("=== TF-IDF Document Ranking Demo ===\n")
    
    # Sample knowledge base for a RAG system
    knowledge_base = [
        "Python is a high-level programming language known for its simplicity and readability.",
        "Machine learning algorithms can be implemented efficiently in Python using libraries like scikit-learn.",
        "Natural language processing involves computational techniques for analyzing human language.",
        "Deep learning neural networks require large amounts of data for training.",
        "Artificial intelligence encompasses machine learning, natural language processing, and computer vision.",
        "Data science combines statistics, programming, and domain expertise to extract insights from data.",
        "Web development with Python can be done using frameworks like Django and Flask.",
        "Database management systems store and organize large amounts of structured data.",
        "Cloud computing provides scalable infrastructure for hosting applications and services.",
        "Cybersecurity protects computer systems and networks from digital threats and attacks."
    ]
    
    # Initialize document ranker
    ranker = DocumentRanker()
    ranker.fit(knowledge_base)
    
    print("Knowledge Base (10 documents):")
    for i, doc in enumerate(knowledge_base, 1):
        print(f"{i:2d}. {doc}")
    
    # Test queries
    queries = [
        "How to use Python for machine learning?",
        "What is natural language processing?",
        "Tell me about web development frameworks",
        "Data analysis and statistics methods"
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"Query: '{query}'")
        print(f"{'='*60}")
        
        # Get query TF-IDF breakdown
        query_tfidf = ranker.tfidf_calc.calculate_tfidf_vector(query)
        if query_tfidf:
            print("\nQuery TF-IDF keywords:")
            sorted_terms = sorted(query_tfidf.items(), key=lambda x: x[1], reverse=True)
            for term, score in sorted_terms[:5]:  # Top 5 terms
                print(f"  {term}: {score:.4f}")
        
        # Rank documents
        ranked_docs = ranker.rank_documents(query, top_k=3)
        
        print(f"\nTop 3 most relevant documents:")
        print("-" * 50)
        for rank, (doc_idx, document, score) in enumerate(ranked_docs, 1):
            print(f"{rank}. [Score: {score:.4f}] {document}")
        
        print()


if __name__ == "__main__":
    demo_document_ranking()