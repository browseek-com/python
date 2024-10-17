#!/bin/bash

echo "START"

# Exit immediately if a command exits with a non-zero status
set -e

# Function to update version in setup.py
update_version() {
    sed -i "s/version=\".*\"/version=\"$1\"/" setup.py
    git tag "$1"
}

# Check if current directory is a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Error: Not a git repository. Please run this script from the root of your git repository."
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "Error: There are uncommitted changes in the repository. Please commit or stash them before publishing."
    exit 1
fi

# Prompt for new version
echo "Current version: $(grep version setup.py | cut -d'"' -f2)"
read -p "Enter new version number: " NEW_VERSION

# Update version in setup.py
update_version $NEW_VERSION

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

# Run tests
echo "Running tests..."
#python -m unittest discover tests

# Clean up old builds
echo "Cleaning up old builds..."
rm -rf build dist *.egg-info

# Build the package
echo "Building the package..."
python setup.py sdist bdist_wheel

# Check if tests passed
if [ $? -ne 0 ]; then
    echo "Unit tests failed. Aborting publish."
    exit 1
fi

# Check the package
echo "Checking the package..."
twine check dist/*

# Prompt for confirmation before uploading
echo "Uploading to PyPI..."
twine upload dist/*

echo "DONE"

