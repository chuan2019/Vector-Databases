# BM25 Information Retrieval System

A comprehensive implementation of the BM25 (Best Matching 25) ranking algorithm for information retrieval and document ranking applications.

## Overview

BM25 is a probabilistic ranking function used to estimate the relevance of documents to a given search query. It's widely considered the state-of-the-art for keyword-based information retrieval and is used by major search engines and databases.

## Features

- **Complete BM25 Implementation**: Full implementation of the BM25 ranking algorithm
- **Tunable Parameters**: Configurable k1 and b parameters for different datasets
- **Document Analysis**: Detailed term-by-term scoring breakdown
- **Ranking Interface**: High-level API for document ranking and search
- **Performance Optimized**: Efficient implementation suitable for large document collections
- **Educational Examples**: Comprehensive examples demonstrating BM25 concepts

## Files Structure

```
bm25/
├── __init__.py                 # Package initialization
├── bm25_calculator.py          # Core BM25 algorithm implementation
├── document_ranker.py          # High-level document ranking interface  
├── simple_bm25_example.py      # Basic usage examples
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

## Quick Start

### Basic Usage

```python
from bm25_calculator import BM25Calculator

# Initialize BM25 with default parameters
bm25 = BM25Calculator(k1=1.2, b=0.75)

# Fit on document collection
documents = [
    "Machine learning algorithms enable pattern recognition",
    "Deep learning uses neural networks for complex tasks", 
    "Natural language processing understands human text"
]
bm25.fit(documents)

# Rank documents for a query
results = bm25.rank_documents("machine learning", top_k=3)
for rank, (doc_idx, document, score) in enumerate(results, 1):
    print(f"{rank}. Score: {score:.4f} - {document}")
```

### Advanced Usage with Document Ranker

```python
from document_ranker import BM25DocumentRanker

# Initialize ranker
ranker = BM25DocumentRanker(k1=1.2, b=0.75)
ranker.fit(documents)

# Search with explanation
results = ranker.search("machine learning", top_k=5)
explanation = ranker.explain_ranking("machine learning", results[0][0])
```

## BM25 Algorithm

The BM25 score for a document D and query Q is calculated as:

```
BM25(D,Q) = Σ IDF(qi) × (f(qi,D) × (k1 + 1)) / (f(qi,D) + k1 × (1 - b + b × |D|/avgdl))
```

Where:
- `qi`: query terms
- `f(qi,D)`: term frequency of qi in document D  
- `|D|`: length of document D in words
- `avgdl`: average document length in the corpus
- `k1`: controls term frequency scaling (typically 1.2-2.0)
- `b`: controls length normalization (typically 0.75)
- `IDF(qi)`: inverse document frequency

## Parameters

### k1 Parameter
- **Range**: 1.2 to 2.0 (typical)
- **Effect**: Controls how much term frequency contributes to the score
- **Higher k1**: More weight to term frequency
- **Lower k1**: Less sensitivity to term frequency

### b Parameter  
- **Range**: 0.0 to 1.0
- **Effect**: Controls document length normalization
- **b = 0**: No length normalization
- **b = 1**: Full length normalization
- **b = 0.75**: Standard balanced normalization

## Examples

### Run Basic Example
```bash
python simple_bm25_example.py
```

### Run Document Ranker Demo
```bash
python document_ranker.py
```

## Use Cases

- **Search Engines**: Primary ranking algorithm for keyword search
- **Information Retrieval**: Academic and commercial IR systems  
- **Document Databases**: MongoDB, Elasticsearch, Weaviate keyword search
- **RAG Systems**: Keyword retrieval component in hybrid search
- **Enterprise Search**: Internal document and knowledge base systems

## Comparison with TF-IDF

| Feature | BM25 | TF-IDF |
|---------|------|---------|
| **Term Frequency** | Saturating function | Linear |
| **Length Normalization** | Built-in with b parameter | Manual implementation |
| **Theoretical Foundation** | Probabilistic model | Heuristic approach |
| **Performance** | Generally better | Baseline method |
| **Parameters** | Tunable (k1, b) | Fixed formula |

## Performance Tips

1. **Parameter Tuning**: Experiment with k1 and b for your specific dataset
2. **Preprocessing**: Consider stemming and stop word removal
3. **Corpus Size**: BM25 works well with larger document collections
4. **Query Length**: More effective with multi-term queries

## Integration

The BM25 implementation can be easily integrated with:
- **Vector Search**: For hybrid retrieval systems
- **Elasticsearch**: As a reference implementation
- **Database Systems**: For full-text search capabilities
- **ML Pipelines**: As a feature extraction method

## Educational Value

This implementation is designed for learning and includes:
- Detailed mathematical explanations
- Step-by-step calculation breakdowns
- Parameter impact demonstrations  
- Comparison with other IR methods
- Visualization-ready output formats

## License

This implementation is part of the Vector Database Study project and is provided for educational and research purposes.