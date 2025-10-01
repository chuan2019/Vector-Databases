"""
Simple BM25 Example for Single Query Analysis

This script demonstrates how to calculate BM25 scores for a single query
in the context of a small document collection.
"""

from bm25_calculator import BM25Calculator


def analyze_query_bm25():
    """
    Analyze BM25 scores for a single query in context of a document collection.
    """
    print("=== Single Query BM25 Analysis ===\n")
    
    # Create a small corpus for context
    corpus = [
        "Machine learning is a powerful subset of artificial intelligence technology",
        "Natural language processing enables computers to understand and interpret human text",
        "Deep learning neural networks use multiple layers for complex pattern recognition",
        "Data science combines statistics programming and machine learning for insights",
        "Computer vision allows machines to analyze and interpret visual information from images"
    ]
    
    # Initialize BM25 calculator
    bm25 = BM25Calculator(k1=1.2, b=0.75)
    bm25.fit(corpus)
    
    print("Document corpus:")
    for i, doc in enumerate(corpus, 1):
        print(f"{i}. {doc}")
    
    # Analyze a target query
    target_query = "machine learning for data analysis and pattern recognition"
    
    print(f"\nTarget query: '{target_query}'")
    
    # Calculate BM25 scores for each document
    print(f"\nBM25 scores for each document:")
    print("-" * 50)
    
    for i, doc in enumerate(corpus):
        score = bm25.calculate_bm25_score(target_query, i)
        print(f"Document {i+1}: {score:.6f}")
        print(f"  {doc}")
        print()
    
    # Get ranking
    ranking = bm25.rank_documents(target_query)
    
    print(f"Ranked results:")
    print("-" * 50)
    for rank, (doc_idx, document, score) in enumerate(ranking, 1):
        print(f"{rank}. [Doc {doc_idx+1}] Score: {score:.6f}")
        print(f"   {document}")
        print()
    
    # Get top keywords
    keywords = bm25.get_top_keywords(target_query, top_k=5)
    
    print(f"Top query terms (ranked by BM25 importance):")
    print("-" * 50)
    for i, (keyword, avg_score) in enumerate(keywords, 1):
        print(f"{i}. {keyword:15} | Avg Score: {avg_score:.6f}")
    
    # Detailed analysis for top result
    if ranking:
        top_doc_idx = ranking[0][0]
        analysis = bm25.get_term_analysis(target_query, top_doc_idx)
        
        print(f"\nDetailed BM25 calculation for top document (Doc {top_doc_idx + 1}):")
        print("-" * 60)
        print(f"Document: {corpus[top_doc_idx]}")
        print(f"Length: {analysis['document_length']} words")
        print(f"Length ratio (vs avg): {analysis['length_ratio']:.3f}")
        print()
        
        print(f"{'Term':<15} | {'Query TF':<8} | {'Doc TF':<6} | {'IDF':<8} | {'Term Score':<10}")
        print("-" * 60)
        
        for term_info in analysis['terms']:
            print(f"{term_info['term']:<15} | {term_info['query_count']:<8} | "
                  f"{term_info['doc_tf']:<6} | {term_info['idf']:<8.3f} | "
                  f"{term_info['weighted_score']:<10.4f}")
        
        print("-" * 60)
        print(f"{'TOTAL':<15} | {'':<8} | {'':<6} | {'':<8} | {analysis['total_score']:<10.4f}")


def parameter_impact_demo():
    """
    Demonstrate the impact of BM25 parameters on scoring.
    """
    print("\n=== BM25 Parameter Impact Demo ===\n")
    
    # Simple test documents
    docs = [
        "python programming",
        "python programming language for data science",
        "python programming language for data science and machine learning applications"
    ]
    
    query = "python programming"
    
    print(f"Query: '{query}'")
    print("Documents:")
    for i, doc in enumerate(docs, 1):
        print(f"  {i}. ({len(doc.split()):2d} words) {doc}")
    
    # Test different parameter values
    parameter_sets = [
        (1.2, 0.0, "No length normalization"),
        (1.2, 0.75, "Standard parameters"), 
        (1.2, 1.0, "Full length normalization"),
        (2.0, 0.75, "Higher k1 (more TF weight)")
    ]
    
    print(f"\nParameter impact on BM25 scores:")
    print(f"{'Parameters':<25} | {'Doc 1':<8} | {'Doc 2':<8} | {'Doc 3':<8}")
    print("-" * 60)
    
    for k1, b, description in parameter_sets:
        bm25 = BM25Calculator(k1=k1, b=b)
        bm25.fit(docs)
        
        scores = [bm25.calculate_bm25_score(query, i) for i in range(len(docs))]
        
        param_label = f"k1={k1}, b={b}"
        print(f"{param_label:<25} | {scores[0]:<8.3f} | {scores[1]:<8.3f} | {scores[2]:<8.3f}")
        print(f"{description:<25} |")
        print()


if __name__ == "__main__":
    analyze_query_bm25()
    parameter_impact_demo()