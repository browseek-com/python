# python
python.browseer.com - task automation for browser library 



# Browseek: Headless Browser Router Python Library

## Overview

Browseek is a powerful Python library designed to simplify and optimize headless browser automation. It provides a high-level interface for routing and managing multiple headless browser instances, making it ideal for web scraping, testing, and automation tasks at scale.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Core Concepts](#core-concepts)
4. [API Reference](#api-reference)
5. [Configuration](#configuration)
6. [Advanced Usage](#advanced-usage)
7. [Performance Optimization](#performance-optimization)
8. [Error Handling](#error-handling)
9. [Examples](#examples)
10. [Contributing](#contributing)

## 1. Installation

```bash
pip install browseek
```

## 2. Quick Start

```python
from browseek import BrowserRouter

# Initialize the router
router = BrowserRouter()

# Add browser instances
router.add_browser("chrome", count=2)
router.add_browser("firefox", count=1)

# Use the router to perform a task
result = router.execute("https://example.com", lambda page: page.title())
print(result)

# Clean up
router.close()
```

## 3. Core Concepts

- **BrowserRouter**: The main class for managing browser instances and routing requests.
- **BrowserInstance**: Represents a single headless browser instance.
- **Route**: Defines rules for how specific requests should be handled.
- **Task**: A unit of work to be executed in a browser instance.

## 4. API Reference

### BrowserRouter

```python
class BrowserRouter:
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize the BrowserRouter with optional configuration."""

    def add_browser(self, browser_type: str, count: int = 1, options: Dict[str, Any] = None):
        """Add browser instances to the router."""

    def remove_browser(self, browser_id: str):
        """Remove a browser instance from the router."""

    def add_route(self, pattern: str, handler: Callable):
        """Add a route for specific URL patterns."""

    def execute(self, url: str, task: Callable, timeout: int = 30):
        """Execute a task on a suitable browser instance."""

    def close(self):
        """Close all browser instances and clean up resources."""
```

### BrowserInstance

```python
class BrowserInstance:
    def __init__(self, browser_type: str, options: Dict[str, Any] = None):
        """Initialize a browser instance."""

    def navigate(self, url: str):
        """Navigate to a specific URL."""

    def execute_script(self, script: str):
        """Execute JavaScript in the browser context."""

    def take_screenshot(self) -> bytes:
        """Capture a screenshot of the current page."""
```

## 5. Configuration

Browseek can be configured via a Python dictionary or a YAML file:

```python
config = {
    "max_concurrent_browsers": 5,
    "default_timeout": 30,
    "retry_attempts": 3,
    "proxy": {
        "enabled": True,
        "rotate_on_failure": True
    }
}

router = BrowserRouter(config)
```

## 6. Advanced Usage

### Custom Route Handlers

```python
def custom_handler(browser, url):
    # Custom logic for handling specific URLs
    pass

router.add_route("*.example.com/*", custom_handler)
```

### Parallel Execution

```python
results = router.execute_parallel([
    ("https://example.com", lambda page: page.title()),
    ("https://example.org", lambda page: page.content())
])
```

## 7. Performance Optimization

- Use `execute_parallel` for concurrent tasks
- Implement custom caching mechanisms
- Utilize browser recycling to reduce startup times

## 8. Error Handling

Browseek provides custom exceptions for various error scenarios:

```python
from browseek.exceptions import BrowserNotAvailableError, RoutingError

try:
    result = router.execute("https://example.com", lambda page: page.title())
except BrowserNotAvailableError:
    print("No browsers available")
except RoutingError as e:
    print(f"Routing error: {e}")
```

## 9. Examples

### Web Scraping

```python
def scrape_product_info(page):
    return {
        "title": page.query_selector("h1").inner_text(),
        "price": page.query_selector(".price").inner_text(),
        "description": page.query_selector(".description").inner_text()
    }

results = router.execute_parallel([
    (f"https://example.com/product/{i}", scrape_product_info)
    for i in range(1, 101)
])
```

### Automated Testing

```python
def test_login_flow(page):
    page.fill("#username", "testuser")
    page.fill("#password", "testpass")
    page.click("#login-button")
    return page.query_selector(".welcome-message").is_visible()

is_login_successful = router.execute("https://example.com/login", test_login_flow)
```

## 10. Contributing

We welcome contributions to Browseek! Please see our [Contributing Guide](CONTRIBUTING.md) for more information on how to get started.

---

For more detailed information, examples, and best practices, please refer to our full documentation at https://docs.browseek.io.
