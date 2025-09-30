# Makefile for TF-IDF Calculator Docker operations

.PHONY: build run-main run-simple run-ranker run-all dev clean help

# Default target
help:
	@echo "TF-IDF Calculator Docker Commands:"
	@echo "  make build      - Build Docker image"
	@echo "  make run-main   - Run main TF-IDF demo"
	@echo "  make run-simple - Run simple example" 
	@echo "  make run-ranker - Run document ranker"
	@echo "  make run-all    - Run all examples"
	@echo "  make dev        - Start development shell"
	@echo "  make clean      - Clean up Docker resources"

# Build Docker image
build:
	docker-compose build

# Run main demo
run-main: build
	docker-compose run --rm tfidf-calculator

# Run simple example
run-simple: build
	docker-compose run --rm simple-example

# Run document ranker
run-ranker: build
	docker-compose run --rm document-ranker

# Run all examples
run-all: build
	@echo "=== Running Main Demo ==="
	docker-compose run --rm tfidf-calculator
	@echo ""
	@echo "=== Running Simple Example ==="
	docker-compose run --rm simple-example
	@echo ""
	@echo "=== Running Document Ranker ==="
	docker-compose run --rm document-ranker

# Start development environment
dev: build
	docker-compose run --rm dev

# Clean up Docker resources
clean:
	docker-compose down --rmi local --volumes --remove-orphans

