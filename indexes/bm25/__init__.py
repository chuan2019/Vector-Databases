"""
BM25 Information Retrieval Package

This package provides a complete implementation of the BM25 ranking algorithm
for information retrieval and document ranking applications.

Modules:
- bm25_calculator: Core BM25 algorithm implementation
- document_ranker: High-level document ranking interface
- simple_bm25_example: Basic usage examples and demonstrations
"""

__version__ = "1.0.0"
__author__ = "Vector Database Study"

from .bm25_calculator import BM25Calculator
from .document_ranker import BM25DocumentRanker

__all__ = ['BM25Calculator', 'BM25DocumentRanker']