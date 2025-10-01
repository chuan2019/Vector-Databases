#!/bin/bash

# Quick Docker commands for TF-IDF Calculator

# Build the image
build() {
    echo "Building TF-IDF Calculator Docker image..."
    docker-compose build
}

# Run main demo
run_main() {
    docker-compose run --rm tfidf-calculator
}

# Run simple example
run_simple() {
    docker-compose run --rm simple-example
}

# Run document ranker
run_ranker() {
    docker-compose run --rm document-ranker
}

# Start development shell
dev() {
    docker-compose run --rm dev
}

# Clean up containers and images
clean() {
    echo "Cleaning up Docker containers and images..."
    docker-compose down --rmi local --volumes --remove-orphans
}

# Show usage
usage() {
    echo "Usage: source docker_helpers.sh"
    echo "Then use these functions:"
    echo "  build      - Build Docker image"
    echo "  run_main   - Run main TF-IDF demo"
    echo "  run_simple - Run simple example"
    echo "  run_ranker - Run document ranker"
    echo "  dev        - Start development shell"
    echo "  clean      - Clean up Docker resources"
}

# If script is executed directly (not sourced), show usage
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    usage
fi