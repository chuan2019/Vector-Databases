# TF-IDF Calculator with Docker

A Python implementation of TF-IDF (Term Frequency-Inverse Document Frequency) calculation for keyword search in RAG (Retrieval-Augmented Generation) systems.

## Features

- **TF-IDF Calculator**: Core implementation for calculating term frequency and inverse document frequency
- **Simple Example**: Demonstrates TF-IDF calculation for a single sentence
- **Document Ranker**: Shows how to rank documents by relevance using TF-IDF similarity scores
- **Docker Support**: Complete containerized environment for consistent execution

## Quick Start with Docker

### Prerequisites

- Docker
- Docker Compose

### Running Examples

1. **Run all examples:**
   ```bash
   ./run_docker.sh all
   ```

2. **Run specific examples:**
   ```bash
   # Main TF-IDF calculator demo
   ./run_docker.sh main

   # Simple sentence analysis
   ./run_docker.sh simple

   # Document ranking demo
   ./run_docker.sh ranker
   ```

3. **Interactive development:**
   ```bash
   ./run_docker.sh dev
   ```

### Alternative: Using Docker Compose directly

```bash
# Build the image
docker-compose build

# Run main demo
docker-compose run --rm tfidf-calculator

# Run simple example
docker-compose run --rm simple-example

# Run document ranker
docker-compose run --rm document-ranker

# Start development shell
docker-compose run --rm dev
```

### Using Helper Functions

Source the helper script for convenient functions:

```bash
source docker_helpers.sh

# Then use these functions:
build        # Build Docker image
run_main     # Run main demo
run_simple   # Run simple example
run_ranker   # Run document ranker
dev          # Start development shell
clean        # Clean up Docker resources
```

## File Structure

```
.
├── .gitignore              # Git ignore patterns for Python/Docker
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── Makefile               # Make targets for Docker operations
├── requirements.txt        # Python dependencies (minimal)
├── run_docker.sh           # Convenience script for running examples
├── docker_helpers.sh       # Helper functions for Docker commands
├── tfidf_calculator.py     # Core TF-IDF implementation with demo
├── simple_tfidf_example.py # Simple single sentence analysis
├── document_ranker.py      # Document ranking using TF-IDF similarity
└── README.md              # This file
```

## TF-IDF Concepts

### Term Frequency (TF)
```
TF = (Number of times term appears in document) / (Total number of terms in document)
```

### Inverse Document Frequency (IDF)
```
IDF = log(Total number of documents / Number of documents containing the term)
```

### TF-IDF Score
```
TF-IDF = TF × IDF
```

## Example Output

### Main Demo
Shows TF-IDF calculation for a query against a small document corpus, demonstrating:
- Vocabulary building
- TF-IDF vector calculation
- Top keyword extraction
- Document-level analysis

### Simple Example
Analyzes a single sentence in the context of a knowledge base:
- Detailed TF-IDF breakdown
- Step-by-step calculation explanation
- Keyword ranking

### Document Ranker
Demonstrates document retrieval using TF-IDF similarity:
- Query analysis
- Document ranking by relevance
- Cosine similarity calculation

## Development

### Modifying the Code

The Docker setup mounts the current directory as a volume, so you can:
1. Edit files on your host machine
2. Run them immediately in the container without rebuilding

### Adding Dependencies

If you need additional Python packages:
1. Add them to `requirements.txt`
2. Rebuild the Docker image: `docker-compose build`

## Use Cases in RAG Systems

1. **Keyword Extraction**: Identify important terms in queries and documents
2. **Document Retrieval**: Rank documents by relevance to user queries
3. **Query Enhancement**: Understand which terms are most significant
4. **Content Analysis**: Analyze document collections for key themes

## Performance Notes

- Pure Python implementation (no external dependencies)
- Suitable for small to medium document collections
- For large-scale applications, consider using specialized libraries like scikit-learn
- TF-IDF is a baseline technique; modern RAG systems often use dense embeddings

## License

This is educational code for learning TF-IDF concepts in RAG systems.