"""
BM25 Document Ranking for Information Retrieval Systems

This script demonstrates how to use BM25 to rank documents 
based on their relevance to a query in retrieval systems.
"""

import math
from bm25_calculator import BM25Calculator
from typing import List, Tuple, Dict


class BM25DocumentRanker:
    """
    Document ranking system using BM25 relevance scores.
    
    This class provides a complete document ranking solution using the BM25
    algorithm for keyword-based information retrieval.
    """
    
    def __init__(self, k1: float = 1.2, b: float = 0.75):
        """
        Initialize the BM25 document ranker.
        
        Args:
            k1 (float): BM25 parameter controlling term frequency scaling
            b (float): BM25 parameter controlling document length normalization
        """
        self.bm25_calc = BM25Calculator(k1=k1, b=b)
        self.documents = []
        self.fitted = False
    
    def fit(self, documents: List[str]):
        """
        Fit the ranker with a collection of documents.
        
        Args:
            documents (List[str]): List of document strings
        """
        self.documents = documents
        self.bm25_calc.fit(documents)
        self.fitted = True
    
    def search(self, query: str, top_k: int = 10) -> List[Tuple[int, str, float]]:
        """
        Search for relevant documents using BM25 ranking.
        
        Args:
            query (str): Search query
            top_k (int): Number of top results to return
            
        Returns:
            List[Tuple[int, str, float]]: List of (index, document, score) tuples
        """
        if not self.fitted:
            raise ValueError("Ranker must be fitted before searching")
        
        return self.bm25_calc.rank_documents(query, top_k=top_k)
    
    def explain_ranking(self, query: str, doc_idx: int) -> Dict:
        """
        Explain how the BM25 score was calculated for a specific document.
        
        Args:
            query (str): Search query
            doc_idx (int): Document index to explain
            
        Returns:
            Dict: Detailed explanation of the BM25 calculation
        """
        if not self.fitted:
            raise ValueError("Ranker must be fitted before explaining")
        
        return self.bm25_calc.get_term_analysis(query, doc_idx)
    
    def get_corpus_statistics(self) -> Dict:
        """
        Get statistics about the document corpus.
        
        Returns:
            Dict: Corpus statistics including vocabulary size, document count, etc.
        """
        if not self.fitted:
            raise ValueError("Ranker must be fitted to get statistics")
        
        return {
            'num_documents': len(self.documents),
            'vocabulary_size': len(self.bm25_calc.vocabulary),
            'avg_document_length': self.bm25_calc.avg_doc_length,
            'total_terms': sum(self.bm25_calc.doc_lengths),
            'min_doc_length': min(self.bm25_calc.doc_lengths),
            'max_doc_length': max(self.bm25_calc.doc_lengths),
            'parameters': {
                'k1': self.bm25_calc.k1,
                'b': self.bm25_calc.b
            }
        }


def demo_bm25_ranking():
    """
    Demonstrate BM25 document ranking with a sample corpus.
    """
    print("=== BM25 Document Ranking Demo ===\n")
    
    # Sample knowledge base for demonstration
    knowledge_base = [
        "Machine learning algorithms enable computers to learn patterns from data automatically without explicit programming.",
        "Deep learning neural networks use multiple layers to model complex patterns in large datasets for prediction tasks.",
        "Natural language processing combines computational linguistics with machine learning to help computers understand human language.",
        "Computer vision systems analyze and interpret visual information from images and videos using deep learning techniques.",
        "Data science integrates statistics programming and domain expertise to extract meaningful insights from complex datasets.",
        "Artificial intelligence encompasses machine learning deep learning and symbolic reasoning to simulate human intelligence.",
        "Python programming language provides extensive libraries for data science machine learning and scientific computing applications.",
        "Statistical analysis methods help researchers identify patterns relationships and significance in experimental and observational data.",
        "Database management systems efficiently store organize and retrieve structured and unstructured data for applications.",
        "Web development frameworks enable rapid creation of dynamic interactive applications using modern programming languages and tools."
    ]
    
    # Initialize BM25 document ranker
    ranker = BM25DocumentRanker(k1=1.2, b=0.75)
    ranker.fit(knowledge_base)
    
    print("Knowledge Base (10 documents):")
    for i, doc in enumerate(knowledge_base, 1):
        print(f"{i:2d}. {doc}")
    
    # Show corpus statistics
    stats = ranker.get_corpus_statistics()
    print(f"\nCorpus Statistics:")
    print(f"  Documents: {stats['num_documents']}")
    print(f"  Vocabulary: {stats['vocabulary_size']} unique terms")
    print(f"  Average document length: {stats['avg_document_length']:.1f} words")
    print(f"  Document length range: {stats['min_doc_length']}-{stats['max_doc_length']} words")
    print(f"  BM25 parameters: k1={stats['parameters']['k1']}, b={stats['parameters']['b']}")
    
    # Test queries
    queries = [
        "How to use machine learning algorithms for data analysis?",
        "What is deep learning and neural networks?",
        "Python programming for data science applications",
        "Statistical methods for analyzing experimental data"
    ]
    
    for query in queries:
        print(f"\n{'='*70}")
        print(f"Query: '{query}'")
        print(f"{'='*70}")
        
        # Get top results
        results = ranker.search(query, top_k=3)
        
        print(f"\nTop 3 BM25 Results:")
        for rank, (doc_idx, document, score) in enumerate(results, 1):
            print(f"\n{rank}. [Document {doc_idx + 1}] BM25 Score: {score:.4f}")
            print(f"   {document}")
        
        # Explain top result
        if results:
            top_doc_idx = results[0][0]
            explanation = ranker.explain_ranking(query, top_doc_idx)
            
            print(f"\nDetailed Analysis for Top Result (Document {top_doc_idx + 1}):")
            print(f"Document length: {explanation['document_length']} words (ratio: {explanation['length_ratio']:.2f})")
            print(f"Term contributions:")
            
            for term_info in explanation['terms']:
                print(f"  '{term_info['term']}': "
                      f"TF={term_info['doc_tf']}, "
                      f"IDF={term_info['idf']:.3f}, "
                      f"Score={term_info['weighted_score']:.4f}")
            
            print(f"Total BM25 Score: {explanation['total_score']:.4f}")


def compare_bm25_parameters():
    """
    Compare BM25 performance with different parameter settings.
    """
    print("\n=== BM25 Parameter Comparison ===\n")
    
    # Sample documents with varying lengths
    test_docs = [
        "Machine learning",  # Short
        "Machine learning algorithms for data analysis",  # Medium
        "Machine learning algorithms are computational methods that enable computers to learn patterns from data automatically",  # Long
    ]
    
    query = "machine learning algorithms"
    
    # Test different parameter combinations
    param_combinations = [
        (1.2, 0.0),   # No length normalization
        (1.2, 0.5),   # Moderate length normalization
        (1.2, 0.75),  # Standard parameters
        (1.2, 1.0),   # Full length normalization
        (2.0, 0.75),  # Higher k1 value
    ]
    
    print(f"Query: '{query}'")
    print(f"Documents:")
    for i, doc in enumerate(test_docs, 1):
        print(f"  {i}. ({len(doc.split()):2d} words) {doc}")
    
    print(f"\n{'k1':<4} | {'b':<4} | {'Doc 1':<8} | {'Doc 2':<8} | {'Doc 3':<8} | {'Description':<25}")
    print("-" * 75)
    
    for k1, b in param_combinations:
        ranker = BM25DocumentRanker(k1=k1, b=b)
        ranker.fit(test_docs)
        
        scores = []
        for i in range(len(test_docs)):
            score = ranker.bm25_calc.calculate_bm25_score(query, i)
            scores.append(score)
        
        if b == 0.0:
            desc = "No length penalty"
        elif b == 1.0:
            desc = "Full length penalty"
        elif k1 == 2.0:
            desc = "Higher TF scaling"
        else:
            desc = f"Standard (b={b})"
        
        print(f"{k1:<4} | {b:<4} | {scores[0]:<8.3f} | {scores[1]:<8.3f} | {scores[2]:<8.3f} | {desc:<25}")
    
    print(f"\nObservations:")
    print(f"  - b=0.0: Longer documents may score higher (no length penalty)")
    print(f"  - b=1.0: Shorter documents preferred (full length penalty)")
    print(f"  - Higher k1: More weight to term frequency")
    print(f"  - Standard k1=1.2, b=0.75 provides balanced results")


if __name__ == "__main__":
    demo_bm25_ranking()
    compare_bm25_parameters()