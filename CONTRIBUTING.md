# Contributing to Browseek

Thank you for your interest in contributing to the Browseek library! We welcome contributions from the community to help improve and expand the capabilities of Browseek.

## Development Setup

To set up the development environment for Browseek, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/browseek.git
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the tests to ensure everything is set up correctly:
   ```
   python -m unittest discover tests
   ```

## Code Style and Conventions

When contributing to Browseek, please adhere to the following code style and conventions:

- Follow the PEP 8 style guide for Python code.
- Use meaningful variable and function names.
- Write docstrings for classes, methods, and functions.
- Add comments to explain complex or non-obvious code.
- Keep the code modular and reusable.

## Testing

Browseek uses the `unittest` framework for testing. When adding new features or making changes, please ensure that the existing tests pass and add new tests to cover the changes.

To run the test suite, use the following command:
```
python -m unittest discover tests
```

For more information on writing and running tests, please refer to the [TESTING.md](TESTING.md) file.

## Publishing to PyPI

To publish a new version of the Browseek library to PyPI, follow these steps:

1. Ensure that all tests pass by running the test suite.
2. Update the version number in `setup.py` and `browseek/__init__.py`.
3. Run the publish script:
   ```
   ./publish.sh
   ```

The publish script will run the unit tests, build the package, and upload it to PyPI. If the tests fail, the publish process will be aborted.

## Submitting Pull Requests

To submit a pull request to Browseek, follow these steps:

1. Fork the repository and create a new branch for your changes.
2. Make your changes and ensure that the tests pass.
3. Commit your changes with a descriptive commit message.
4. Push your changes to your forked repository.
5. Open a pull request against the main Browseek repository.

Please provide a clear description of your changes and the problem they solve in the pull request.

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. When reporting an issue, please provide the following information:

- A clear description of the issue or suggestion.
- Steps to reproduce the issue, if applicable.
- The version of Browseek you are using.
- Any relevant error messages or logs.

We appreciate your contributions to making Browseek better!
