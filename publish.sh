#!/bin/bash

# Run unit tests
python -m unittest discover tests

# Check if tests passed
if [ $? -ne 0 ]; then
    echo "Unit tests failed. Aborting publish."
    exit 1
fi

# Build the package
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*

echo "Browseek package published to PyPI successfully!"
