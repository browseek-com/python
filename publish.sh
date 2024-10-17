#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the package
python setup.py sdist bdist_wheel

# Install the package locally
pip install --editable .

# Run unit tests
venv/bin/python -m unittest discover tests

# Check if tests passed
if [ $? -ne 0 ]; then
    echo "Unit tests failed. Aborting publish."
    exit 1
fi

# Upload to PyPI
twine upload dist/*

echo "Browseek package published to PyPI successfully!"
