#!/bin/bash

# Build and run TF-IDF Calculator in Docker
# Usage: ./run_docker.sh [example_name]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed or not in PATH"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed or not in PATH"
    exit 1
fi

# Build the Docker image
print_info "Building Docker image..."
docker-compose build tfidf-calculator

# Determine which example to run
EXAMPLE=${1:-"main"}

case $EXAMPLE in
    "main"|"tfidf")
        print_info "Running main TF-IDF calculator demo..."
        docker-compose run --rm tfidf-calculator
        ;;
    "simple")
        print_info "Running simple TF-IDF example..."
        docker-compose run --rm simple-example
        ;;
    "ranker"|"rank")
        print_info "Running document ranker example..."
        docker-compose run --rm document-ranker
        ;;
    "dev"|"bash")
        print_info "Starting interactive development environment..."
        docker-compose run --rm dev
        ;;
    "all")
        print_info "Running all examples..."
        print_info "1. Main TF-IDF Calculator Demo"
        docker-compose run --rm tfidf-calculator
        echo ""
        print_info "2. Simple TF-IDF Example"
        docker-compose run --rm simple-example
        echo ""
        print_info "3. Document Ranker Example"
        docker-compose run --rm document-ranker
        ;;
    *)
        print_error "Unknown example: $EXAMPLE"
        echo "Usage: $0 [main|simple|ranker|dev|all]"
        echo "  main   - Run the main TF-IDF calculator demo (default)"
        echo "  simple - Run the simple TF-IDF example"
        echo "  ranker - Run the document ranker example"
        echo "  dev    - Start interactive bash shell"
        echo "  all    - Run all examples sequentially"
        exit 1
        ;;
esac

print_info "Done!"