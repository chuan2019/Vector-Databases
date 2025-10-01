# BM25 Information Retrieval System Makefile
# Provides convenient commands for testing and running BM25 examples

.PHONY: help demo simple ranking clean test

# Default Python command
PYTHON := python3

help:
	@echo "BM25 Information Retrieval System"
	@echo "================================="
	@echo ""
	@echo "Available commands:"
	@echo "  demo      - Run comprehensive BM25 demonstration"
	@echo "  simple    - Run simple BM25 example"
	@echo "  ranking   - Run document ranking demo"
	@echo "  test      - Run all examples and tests"
	@echo "  clean     - Clean up generated files"
	@echo "  help      - Show this help message"

demo: simple ranking
	@echo "BM25 demonstration completed!"

simple:
	@echo "Running simple BM25 example..."
	@$(PYTHON) simple_bm25_example.py
	@echo ""

ranking:
	@echo "Running BM25 document ranking demo..."
	@$(PYTHON) document_ranker.py
	@echo ""

test: demo
	@echo "All BM25 tests completed successfully!"

clean:
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean completed!"

# Quick test to verify imports work
verify:
	@echo "Verifying BM25 imports..."
	@$(PYTHON) -c "from bm25_calculator import BM25Calculator; from document_ranker import BM25DocumentRanker; print('All imports successful!')"

# Parameter analysis
params:
	@echo "Running parameter analysis..."
	@$(PYTHON) -c "from simple_bm25_example import parameter_impact_demo; parameter_impact_demo()"

# Show module info
info:
	@echo "BM25 Module Information:"
	@echo "======================="
	@$(PYTHON) -c "import bm25_calculator; help(bm25_calculator.BM25Calculator.__init__)"