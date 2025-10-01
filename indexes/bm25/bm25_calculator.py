"""
BM25 Calculator for Information Retrieval

This module implements the BM25 (Best Matching 25) ranking function
for use in information retrieval and search systems.
"""

import math
from collections import Counter
from typing import List, Dict, Tuple


class BM25Calculator:
    """
    BM25 ranking function implementation for information retrieval.
    
    BM25 is a probabilistic ranking function that estimates the relevance
    of documents to a given search query based on query terms appearing in the documents.
    
    The BM25 score for a document D and query Q is calculated as:
    
    BM25(D,Q) = Σ IDF(qi) * (f(qi,D) * (k1 + 1)) / (f(qi,D) + k1 * (1 - b + b * |D|/avgdl))
    
    Where:
    - qi: query terms
    - f(qi,D): term frequency of qi in document D
    - |D|: length of document D in words
    - avgdl: average document length in the corpus
    - k1: controls term frequency scaling (typically 1.2 to 2.0)
    - b: controls length normalization (typically 0.75)
    - IDF(qi): inverse document frequency
    """
    
    def __init__(self, k1: float = 1.2, b: float = 0.75):
        """
        Initialize BM25 calculator with tuning parameters.
        
        Args:
            k1 (float): Controls term frequency scaling. Higher values give more weight
                       to term frequency. Typical range: 1.2 to 2.0
            b (float): Controls document length normalization. 0 = no normalization,
                      1 = full normalization. Typical value: 0.75
        """
        self.k1 = k1
        self.b = b
        self.documents = []
        self.doc_lengths = []
        self.avg_doc_length = 0.0
        self.vocabulary = set()
        self.doc_term_freqs = []
        self.idf_scores = {}
        self.N = 0  # Total number of documents
    
    def preprocess_text(self, text: str) -> List[str]:
        """
        Preprocess text by converting to lowercase and splitting into tokens.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            List[str]: List of preprocessed tokens
        """
        # Simple preprocessing - in practice, you might want stemming, stop word removal, etc.
        return text.lower().split()
    
    def fit(self, documents: List[str]):
        """
        Fit the BM25 calculator on a corpus of documents.
        
        Args:
            documents (List[str]): List of document strings
        """
        self.documents = documents
        self.N = len(documents)
        
        # Preprocess all documents
        processed_docs = []
        self.doc_lengths = []
        
        for doc in documents:
            tokens = self.preprocess_text(doc)
            processed_docs.append(tokens)
            self.doc_lengths.append(len(tokens))
            self.vocabulary.update(tokens)
        
        # Calculate average document length
        self.avg_doc_length = sum(self.doc_lengths) / len(self.doc_lengths)
        
        # Calculate term frequencies for each document
        self.doc_term_freqs = []
        for tokens in processed_docs:
            term_freq = Counter(tokens)
            self.doc_term_freqs.append(term_freq)
        
        # Calculate IDF scores
        self._calculate_idf_scores(processed_docs)
    
    def _calculate_idf_scores(self, processed_docs: List[List[str]]):
        """
        Calculate IDF scores for all terms in the vocabulary.
        
        Args:
            processed_docs (List[List[str]]): List of tokenized documents
        """
        for term in self.vocabulary:
            # Count documents containing the term
            doc_count = sum(1 for doc in processed_docs if term in doc)
            
            # BM25 IDF formula with smoothing
            idf = math.log((self.N - doc_count + 0.5) / (doc_count + 0.5))
            self.idf_scores[term] = idf
    
    def calculate_bm25_score(self, query: str, doc_idx: int) -> float:
        """
        Calculate BM25 score for a query-document pair.
        
        Args:
            query (str): Query string
            doc_idx (int): Document index
            
        Returns:
            float: BM25 score
        """
        query_terms = self.preprocess_text(query)
        doc_term_freq = self.doc_term_freqs[doc_idx]
        doc_length = self.doc_lengths[doc_idx]
        
        score = 0.0
        
        for term in query_terms:
            if term not in self.vocabulary:
                continue
                
            # Term frequency in document
            tf = doc_term_freq.get(term, 0)
            
            # IDF score
            idf = self.idf_scores[term]
            
            # Length normalization component
            length_norm = 1 - self.b + self.b * (doc_length / self.avg_doc_length)
            
            # BM25 term score
            term_score = idf * (tf * (self.k1 + 1)) / (tf + self.k1 * length_norm)
            
            score += term_score
        
        return score
    
    def rank_documents(self, query: str, top_k: int = None) -> List[Tuple[int, str, float]]:
        """
        Rank documents by BM25 relevance to the query.
        
        Args:
            query (str): Query string
            top_k (int): Number of top results to return (None for all)
            
        Returns:
            List[Tuple[int, str, float]]: List of (index, document, score) tuples
        """
        scores = []
        
        for i in range(len(self.documents)):
            score = self.calculate_bm25_score(query, i)
            scores.append((i, self.documents[i], score))
        
        # Sort by BM25 score (descending)
        scores.sort(key=lambda x: x[2], reverse=True)
        
        if top_k is not None:
            scores = scores[:top_k]
        
        return scores
    
    def get_term_analysis(self, query: str, doc_idx: int) -> Dict:
        """
        Get detailed analysis of how each query term contributes to the BM25 score.
        
        Args:
            query (str): Query string
            doc_idx (int): Document index
            
        Returns:
            Dict: Detailed term analysis
        """
        query_terms = self.preprocess_text(query)
        doc_term_freq = self.doc_term_freqs[doc_idx]
        doc_length = self.doc_lengths[doc_idx]
        
        analysis = {
            'document_index': doc_idx,
            'document_length': doc_length,
            'avg_doc_length': self.avg_doc_length,
            'length_ratio': doc_length / self.avg_doc_length,
            'terms': []
        }
        
        total_score = 0.0
        
        for term in set(query_terms):  # Unique terms only
            if term not in self.vocabulary:
                continue
                
            tf = doc_term_freq.get(term, 0)
            idf = self.idf_scores[term]
            length_norm = 1 - self.b + self.b * (doc_length / self.avg_doc_length)
            term_score = idf * (tf * (self.k1 + 1)) / (tf + self.k1 * length_norm)
            
            # Count occurrences in query for weighting
            query_count = query_terms.count(term)
            weighted_score = term_score * query_count
            total_score += weighted_score
            
            analysis['terms'].append({
                'term': term,
                'query_count': query_count,
                'doc_tf': tf,
                'idf': idf,
                'length_norm': length_norm,
                'term_score': term_score,
                'weighted_score': weighted_score
            })
        
        analysis['total_score'] = total_score
        return analysis
    
    def get_top_keywords(self, query: str, top_k: int = 10) -> List[Tuple[str, float]]:
        """
        Get top keywords from query ranked by their average BM25 contribution.
        
        Args:
            query (str): Query string
            top_k (int): Number of top keywords to return
            
        Returns:
            List[Tuple[str, float]]: List of (term, avg_score) tuples
        """
        query_terms = self.preprocess_text(query)
        term_scores = {}
        
        for term in set(query_terms):
            if term not in self.vocabulary:
                continue
                
            # Calculate average term contribution across all documents
            total_contribution = 0.0
            doc_count = 0
            
            for doc_idx in range(len(self.documents)):
                tf = self.doc_term_freqs[doc_idx].get(term, 0)
                if tf > 0:
                    idf = self.idf_scores[term]
                    doc_length = self.doc_lengths[doc_idx]
                    length_norm = 1 - self.b + self.b * (doc_length / self.avg_doc_length)
                    term_score = idf * (tf * (self.k1 + 1)) / (tf + self.k1 * length_norm)
                    total_contribution += term_score
                    doc_count += 1
            
            if doc_count > 0:
                avg_score = total_contribution / doc_count
                term_scores[term] = avg_score
        
        # Sort by average score
        sorted_terms = sorted(term_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_terms[:top_k]