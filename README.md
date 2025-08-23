# Vector Databases

This repository contains comprehensive study materials, practical implementations, and hands-on projects for understanding and working with vector databases, with a focus on Weaviate as the primary vector database platform.

## 📋 Overview

Vector databases are specialized databases designed to store, index, and query high-dimensional vector data efficiently. They are essential for modern AI applications including semantic search, recommendation systems, RAG (Retrieval-Augmented Generation) systems, and similarity matching.

This repository provides:
- **Practical implementations** of vector database setups
- **Interactive notebooks** for learning and experimentation
- **Real-world datasets** for testing and development
- **GUI tools** for database management and visualization
- **Comprehensive documentation** and guides

## 📁 Repository Structure

### 📚 Notebooks
Interactive Jupyter notebooks for learning and experimentation:
- [`notebooks/Vector-Database.ipynb`](./notebooks/Vector-Database.ipynb) - Comprehensive vector database tutorial and concepts
- [`notebooks/vdb-indexing.001.lsh.ipynb`](./notebooks/vdb-indexing.001.lsh.ipynb) - Locality-Sensitive Hashing (LSH) indexing techniques

### 📊 Datasets
Sample datasets for testing and development:
- [`datasets/data.joblib`](./datasets/data.joblib) - Serialized dataset for quick loading
- [`datasets/jeopardy_tiny.json`](./datasets/jeopardy_tiny.json) - Small Jeopardy dataset for testing
- [`datasets/recipes/`](./datasets/recipes/) - Recipe-related datasets and examples

### 🛠️ Weaviate Implementation
Complete Weaviate setup with development environment:
- [`weaviate/`](./weaviate/) - Weaviate database implementation and tooling
  - Local development environment with Docker
  - GUI applications for database management
  - Configuration and deployment scripts

## 🚀 Quick Start

1. **Explore the concepts**: Start with the [`notebooks/Vector-Database.ipynb`](./notebooks/Vector-Database.ipynb) to understand vector database fundamentals

2. **Set up Weaviate**: Navigate to [`weaviate/local-dev/`](./weaviate/local-dev/) for a complete local development environment

3. **Try the GUI tools**: Check out the [`weaviate/gui/`](./weaviate/gui/) directory for visual database management tools

4. **Experiment with datasets**: Use the provided datasets in [`datasets/`](./datasets/) for testing and learning

## 📖 Learning Path

1. **Foundation**: Review vector database concepts in the notebooks
2. **Setup**: Install and configure Weaviate using the local development setup
3. **Practice**: Upload and query datasets using the provided tools
4. **Explore**: Use GUI applications to visualize and manage your data
5. **Advanced**: Implement custom solutions using the examples as templates

## 🔧 Requirements

- Python 3.8+
- Docker and Docker Compose
- Jupyter Notebook environment
- Required Python packages (see individual directories for specific requirements)

## 📚 Additional Resources

- [Weaviate Official Documentation](https://weaviate.io/docs)
- [Vector Database Concepts](https://www.pinecone.io/learn/vector-database/)
- [Embeddings and Similarity Search](https://huggingface.co/blog/getting-started-with-embeddings)

---

*This repository is designed for educational purposes and practical implementation of vector database concepts. Each component is self-contained with its own documentation and examples.*
