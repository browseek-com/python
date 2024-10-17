#!/bin/bash
# Check if the Browseek library is installed by running the following command:
pip list | grep browseek

# If the Browseek library is not listed in the output, install it using the following command:
pip install -e .

# run example
python examples/basic_usage.py