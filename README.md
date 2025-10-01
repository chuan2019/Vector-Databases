# Vector Databases

This repository contains comprehensive study materials, practical implementations, and hands-on projects for understanding and working with vector databases, focusing on fundamental indexing algorithms and retrieval techniques.

## Overview

Vector databases are specialized databases designed to store, index, and query high-dimensional vector data efficiently. They are essential for modern AI applications including semantic search, recommendation systems, RAG (Retrieval-Augmented Generation) systems, and similarity matching.

This repository provides:
- **Algorithm implementations** of core indexing techniques (TF-IDF, BM25, LSH)
- **Interactive notebooks** for learning fundamental concepts and practical applications
- **Modular code structures** for production-ready implementations
- **Comprehensive documentation** and educational materials

## Repository Structure

### Notebooks (`notebooks/`)
Interactive Jupyter notebooks for learning and experimentation:
- [`Vector-Database.ipynb`](./notebooks/Vector-Database.ipynb) - Comprehensive vector database tutorial and concepts
- [`vdb-indexing.001.lsh.ipynb`](./notebooks/vdb-indexing.001.lsh.ipynb) - Locality-Sensitive Hashing (LSH) indexing techniques
- [`vdb-indexing.002.tf-idf.ipynb`](./notebooks/vdb-indexing.002.tf-idf.ipynb) - TF-IDF algorithm theory and implementation
- [`vdb-indexing.003.bm25.ipynb`](./notebooks/vdb-indexing.003.bm25.ipynb) - BM25 ranking function with detailed analysis
- [`Weaviate-Collections.ipynb`](./notebooks/Weaviate-Collections.ipynb) - Weaviate collections tutorial (legacy)
- [`Weaviate-Modules.ipynb`](./notebooks/Weaviate-Modules.ipynb) - Weaviate modules tutorial (legacy)

### Algorithm Implementations (`indexes/`)
Production-ready implementations of core indexing algorithms:

#### TF-IDF Implementation (`indexes/tf-idf/`)
- **`tfidf_calculator.py`** - Core TF-IDF algorithm implementation
- **`document_ranker.py`** - Document ranking using TF-IDF scores
- **`simple_tfidf_example.py`** - Basic usage example
- **`Makefile`** - Build and test automation
- **`requirements.txt`** - Python dependencies
- **`README.md`** - Detailed documentation and usage guide

#### BM25 Implementation (`indexes/bm25/`)
- **`bm25_calculator.py`** - Core BM25 algorithm implementation
- **`document_ranker.py`** - Document ranking using BM25 scores
- **`simple_bm25_example.py`** - Basic usage example
- **`Makefile`** - Build and test automation
- **`requirements.txt`** - Python dependencies
- **`README.md`** - Detailed documentation and usage guide

## Quick Start

### 1. Explore Core Concepts
Start with the educational notebooks:
```bash
# Navigate to notebooks directory
cd notebooks/

# Start with fundamentals
jupyter notebook Vector-Database.ipynb

# Learn indexing algorithms
jupyter notebook vdb-indexing.002.tf-idf.ipynb    # TF-IDF theory and practice
jupyter notebook vdb-indexing.003.bm25.ipynb      # BM25 ranking function
jupyter notebook vdb-indexing.001.lsh.ipynb       # LSH for approximate search
```

### 2. Use Algorithm Implementations
Try the production-ready implementations:
```bash
# Test TF-IDF implementation
cd indexes/tf-idf/
python simple_tfidf_example.py

# Test BM25 implementation  
cd ../bm25/
python simple_bm25_example.py

# Build and test with make
make test
```

### 3. Experiment with Your Data
Use sample data or bring your own:
```bash
# Create sample data for testing
python -c "
from indexes.bm25.bm25_calculator import BM25Calculator

# Use sample documents
documents = [
    'Machine learning is transforming data analysis',
    'Natural language processing enables text understanding', 
    'Deep learning uses neural networks for pattern recognition',
    'Computer vision analyzes images and visual data',
    'Data science combines statistics and programming'
]

# Create and train BM25 model
bm25 = BM25Calculator()
bm25.fit(documents)

# Query the model
results = bm25.rank_documents('science technology', top_k=3)
for rank, (idx, doc, score) in enumerate(results, 1):
    print(f'{rank}. {doc} (score: {score:.3f})')
"
```

## Learning Path

1. **Foundation**: Start with `Vector-Database.ipynb` to understand vector database fundamentals
2. **Algorithms**: Learn TF-IDF and BM25 through the interactive notebooks  
3. **Hands-on**: Run the example scripts in each `indexes/` implementation
4. **Build**: Use the modular implementations in your own projects
5. **Advanced**: Explore LSH and approximate search techniques

## Requirements

- **Python 3.8+** (recommended: Python 3.12.9)
- **Jupyter Notebook** environment for interactive learning
- **Python packages**: See `requirements.txt` in each implementation directory
  - Core: `numpy`, `pandas`, `matplotlib`, `seaborn`
  - Additional: `scikit-learn` (for comparisons and validation)

### Installation
```bash
# Create virtual environment (recommended)
python -m venv vdb-env
source vdb-env/bin/activate  # On Windows: vdb-env\Scripts\activate

# Install dependencies for specific implementations
cd indexes/tf-idf && pip install -r requirements.txt
cd ../bm25 && pip install -r requirements.txt

# For notebooks, install additional dependencies
pip install jupyter matplotlib seaborn scikit-learn
```

## Algorithm Implementations Overview

### TF-IDF (Term Frequency-Inverse Document Frequency)
- **Use Case**: Document similarity and basic information retrieval
- **Strengths**: Simple, interpretable, good baseline for text analysis
- **Implementation**: Full calculation with normalization options
- **Features**: Document ranking, similarity scoring, term importance analysis

### BM25 (Best Matching 25)
- **Use Case**: Advanced information retrieval and search ranking
- **Strengths**: Handles document length normalization, tunable parameters
- **Implementation**: Production-ready with detailed parameter analysis
- **Features**: Probabilistic ranking, length normalization, parameter optimization

### LSH (Locality-Sensitive Hashing)  
- **Use Case**: Approximate similarity search for large-scale data
- **Strengths**: Sub-linear query time, scalable to massive datasets
- **Implementation**: Multiple hash family implementations
- **Features**: Configurable precision/recall trade-offs, collision analysis

## Key Features

- **Educational**: Step-by-step explanations with mathematical foundations
- **Visual**: Rich visualizations showing algorithm behavior and parameter effects  
- **Modular**: Clean, reusable implementations suitable for production
- **Testable**: Comprehensive examples and test cases
- **Comparative**: Side-by-side algorithm comparisons and analysis

## Additional Resources

- [Information Retrieval Fundamentals](https://nlp.stanford.edu/IR-book/)
- [Vector Database Concepts](https://www.pinecone.io/learn/vector-database/)
- [BM25 Research Paper](https://en.wikipedia.org/wiki/Okapi_BM25)
- [TF-IDF Mathematical Foundation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Locality-Sensitive Hashing](https://web.stanford.edu/class/cs246/slides/03-lsh.pdf)
