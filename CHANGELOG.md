# Changelog

All notable changes to the Browseek library will be documented in this file.

## [Unreleased]

## [0.1.6] - 2024-10-17
### Changed
- Updated Dockerfile to include default environment variables.
- Modified docker-compose.yml to use environment variables from .env file.
- Improved configuration management for Docker deployments.

## [0.1.5] - 2024-10-17
### Added
- Added `DriverRouter` class to support multiple browser automation frameworks (Playwright, Selenium, Puppeteer).
- Updated `BrowserInstance` class to use `DriverRouter` for browser automation.
- Modified example scripts and unit tests to demonstrate usage of `DriverRouter` with different frameworks.
- Updated documentation to explain the new `DriverRouter` feature and provide usage instructions.

### Changed
- Updated basic_usage.py example script to use the new `DriverRouter` with Playwright.
- Improved error handling and resource management in basic_usage.py.
- Added explanatory notes about potential warnings in basic_usage.py.

### Fixed
- Resolved import issues in basic_usage.py by updating requirements.txt.

## [0.1.3] - 2024-10-17
### Added
- Support for configurable test URLs in unit tests using environment variables.
- Example HTML file with images for testing purposes.

### Changed
- Updated Docker Compose setup to serve the example HTML file and images through the Nginx server.

## [0.1.0] - 2024-10-17
### Added
- Initial release of the Browseek library
- Basic browser automation functionality
- Support for Chrome and Firefox browsers
- Request interception and modification
- Device profile simulation
- Network configuration options
- CAPTCHA solving capabilities
- Custom exception classes
- Unit tests for core functionality
- Example scripts demonstrating usage
- Dockerfile and Docker Compose configuration
- Publish script for PyPI releases
- Contribution guidelines and testing instructions

### Changed
- Updated README with links to additional documentation files
- Improved documentation and code comments

### Fixed
- Minor bug fixes and improvements
