.PHONY: install run clean test lint format

install:
	python -m pip install -r requirements.txt
	pre-commit install

run:
	streamlit run app.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -r {} +

lint:
	flake8 .
	black . --check
	isort . --check-only

format:
	black .
	isort .

setup: clean install
