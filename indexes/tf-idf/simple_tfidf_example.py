"""
Simple TF-IDF Example for Single Sentence Analysis

This script demonstrates how to calculate TF-IDF for a single sentence
in the context of a small document corpus.
"""

from tfidf_calculator import TFIDFCalculator


def analyze_sentence_tfidf():
    """
    Analyze TF-IDF for a single sentence in context of a document collection.
    """
    print("=== Single Sentence TF-IDF Analysis ===\n")
    
    # Create a small corpus for context
    # In a real RAG system, this would be your knowledge base
    corpus = [
        "Machine learning is a subset of artificial intelligence",
        "Natural language processing helps computers understand text",
        "Deep learning uses neural networks with multiple layers",
        "Retrieval augmented generation combines search with language models",
        "Vector databases store embeddings for similarity search"
    ]
    
    # Initialize TF-IDF calculator
    tfidf = TFIDFCalculator()
    tfidf.fit(corpus)
    
    print("Document corpus:")
    for i, doc in enumerate(corpus, 1):
        print(f"{i}. {doc}")
    
    # Analyze a target sentence
    target_sentence = "I want to learn about machine learning and neural networks"
    
    print(f"\nTarget sentence: '{target_sentence}'")
    
    # Calculate TF-IDF scores
    tfidf_scores = tfidf.calculate_tfidf_vector(target_sentence)
    
    print(f"\nTF-IDF scores for each term:")
    print("-" * 40)
    
    if tfidf_scores:
        for term, score in sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{term:15} | {score:.6f}")
    else:
        print("No terms from the sentence found in the corpus vocabulary.")
    
    # Get top keywords
    top_keywords = tfidf.get_top_keywords(target_sentence, top_k=5)
    
    print(f"\nTop keywords (ranked by TF-IDF importance):")
    print("-" * 50)
    for i, (keyword, score) in enumerate(top_keywords, 1):
        print(f"{i}. {keyword:15} | {score:.6f}")
    
    # Show detailed calculation for one term (if available)
    if top_keywords:
        example_term = top_keywords[0][0]
        print(f"\nDetailed calculation for '{example_term}':")
        print("-" * 40)
        
        # Get term frequency
        tokens = tfidf.preprocess_text(target_sentence)
        tf = tfidf.calculate_tf(example_term, tokens)
        idf = tfidf.idf_scores.get(example_term, 0)
        
        print(f"Term: '{example_term}'")
        print(f"Term Frequency (TF): {tf:.6f}")
        print(f"Inverse Document Frequency (IDF): {idf:.6f}")
        print(f"TF-IDF Score: {tf * idf:.6f}")
        
        # Explain the calculation
        term_count = tokens.count(example_term)
        total_terms = len(tokens)
        docs_with_term = sum(1 for doc in corpus if example_term in doc.lower())
        total_docs = len(corpus)
        
        print(f"\nCalculation breakdown:")
        print(f"- Term '{example_term}' appears {term_count} times in the sentence")
        print(f"- Sentence has {total_terms} total terms")
        print(f"- TF = {term_count}/{total_terms} = {tf:.6f}")
        print(f"- Term appears in {docs_with_term} out of {total_docs} documents")
        print(f"- IDF = log({total_docs}/{docs_with_term}) = {idf:.6f}")


if __name__ == "__main__":
    analyze_sentence_tfidf()