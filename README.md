# python
python.browseer.com - task automation for browser library 



# Browseek: Advanced Multi-Browser Automation Library

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Core Concepts](#core-concepts)
4. [API Reference](#api-reference)
5. [Configuration](#configuration)
6. [Basic Usage](#basic-usage)
7. [Advanced Features](#advanced-features)
   - [Request Redirection](#request-redirection)
   - [DNS Security](#dns-security)
   - [CAPTCHA Handling](#captcha-handling)
   - [Device Simulation](#device-simulation)
   - [Network Configuration](#network-configuration)
8. [Performance Optimization](#performance-optimization)
9. [Error Handling](#error-handling)
10. [Best Practices](#best-practices)


## 1. Introduction

Browseek is a sophisticated Python library designed for advanced multi-task and multi-browser automation. It provides a robust solution for managing complex web automation scenarios, including request redirection, DNS security, CAPTCHA handling, device simulation, and fine-grained network control.

## 2. Installation

```bash
pip install browseek
```

## 3. Core Concepts

- **BrowserRouter**: Central manager for browser instances and task distribution.
- **BrowserInstance**: Represents a single browser instance with customizable properties.
- **Task**: A unit of work to be executed in a browser instance.
- **RequestInterceptor**: Handles request redirection and modification.
- **DeviceProfile**: Defines device-specific properties for simulation.
- **NetworkConfig**: Configures network-related settings including VPN and speed limits.

## 4. API Reference

```python
class BrowserRouter:
    def __init__(self, config: Dict[str, Any] = None):
        """Initialize the BrowserRouter with optional configuration."""

    def add_browser(self, browser_type: str, count: int = 1, options: Dict[str, Any] = None):
        """Add browser instances to the pool."""

    def set_request_interceptor(self, interceptor: RequestInterceptor):
        """Set a custom request interceptor for all managed browsers."""

    def set_device_profile(self, profile: DeviceProfile):
        """Set a device profile for browser simulation."""

    def set_network_config(self, config: NetworkConfig):
        """Set network configuration including VPN and speed limits."""

    def execute(self, task: Task) -> Any:
        """Execute a single task."""

    def execute_batch(self, tasks: List[Task]) -> List[Any]:
        """Execute a batch of tasks in parallel."""

class RequestInterceptor:
    def intercept(self, request: Request) -> Request:
        """Intercept and optionally modify a request before it's sent."""

class DeviceProfile:
    def __init__(self, user_agent: str, screen_size: Tuple[int, int], os: str, browser: str):
        """Initialize a device profile for simulation."""

class NetworkConfig:
    def __init__(self, vpn_config: Dict[str, Any] = None, speed_limit: int = None):
        """Initialize network configuration."""

class CaptchaSolver:
    def solve(self, captcha_type: str, captcha_data: Any) -> str:
        """Solve a CAPTCHA challenge."""
```

## 5. Configuration

```python
config = {
    "max_concurrent_browsers": 10,
    "default_browser": "chrome",
    "timeout": 30,
    "retry_attempts": 3,
    "proxy": {
        "enabled": True,
        "servers": ["proxy1.example.com", "proxy2.example.com"]
    },
    "dns_over_https": True,
    "captcha_service": "2captcha",
    "captcha_api_key": "your_api_key_here"
}

router = BrowserRouter(config)
```

## 6. Basic Usage

```python
from browseek import BrowserRouter, Task, DeviceProfile, NetworkConfig

router = BrowserRouter()
router.add_browser("chrome", count=2)
router.add_browser("firefox", count=1)

def get_title(page):
    return page.title()

task = Task("https://example.com", get_title)
result = router.execute(task)
print(result)

router.close()
```

## 7. Advanced Features

### Request Redirection

```python
class CustomInterceptor(RequestInterceptor):
    def intercept(self, request):
        if request.resource_type == "image":
            request.abort()
        elif "ads" in request.url:
            request.redirect("about:blank")
        return request

router.set_request_interceptor(CustomInterceptor())
```

### DNS Security

```python
router = BrowserRouter(config={"dns_over_https": True})

def check_dns_leak(page):
    page.goto("https://ipleak.net")
    return page.query_selector("#dnsips").inner_text()

task = Task("https://ipleak.net", check_dns_leak)
dns_ips = router.execute(task)
print(f"DNS IPs: {dns_ips}")
```

### CAPTCHA Handling

```python
class CustomCaptchaSolver(CaptchaSolver):
    def solve(self, captcha_type, captcha_data):
        # Implementation for solving CAPTCHAs
        pass

router.set_captcha_solver(CustomCaptchaSolver())

def login_with_captcha(page):
    page.fill("#username", "user")
    page.fill("#password", "pass")
    captcha_element = page.query_selector("#captcha")
    if captcha_element:
        captcha_solution = router.solve_captcha("image", captcha_element.screenshot())
        page.fill("#captcha-solution", captcha_solution)
    page.click("#login-button")

task = Task("https://example.com/login", login_with_captcha)
router.execute(task)
```

### Device Simulation

```python
iphone_profile = DeviceProfile(
    user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    screen_size=(375, 812),
    os="iOS",
    browser="Safari"
)

router.set_device_profile(iphone_profile)

def check_mobile_version(page):
    return "mobile" in page.url

task = Task("https://example.com", check_mobile_version)
is_mobile = router.execute(task)
print(f"Received mobile version: {is_mobile}")
```

### Network Configuration

```python
network_config = NetworkConfig(
    vpn_config={
        "provider": "nordvpn",
        "country": "us"
    },
    speed_limit=1000000  # 1 Mbps
)

router.set_network_config(network_config)

def check_ip(page):
    page.goto("https://ifconfig.me")
    return page.query_selector("body").inner_text()

task = Task("https://ifconfig.me", check_ip)
ip_address = router.execute(task)
print(f"Current IP: {ip_address}")
```

## 8. Performance Optimization

```python
def warm_up_browsers():
    warm_up_tasks = [Task("https://example.com", lambda p: None) for _ in range(5)]
    router.execute_batch(warm_up_tasks)

warm_up_browsers()

# Browser recycling
router.set_browser_recycling(max_pages=100, max_duration=3600)
```

## 9. Error Handling

```python
from browseek.exceptions import BrowserNotAvailableError, CaptchaError, NetworkError

try:
    result = router.execute(Task("https://example.com", get_title))
except BrowserNotAvailableError:
    print("No suitable browser available")
except CaptchaError as e:
    print(f"CAPTCHA solving failed: {e}")
except NetworkError as e:
    print(f"Network error occurred: {e}")
```

## 10. Best Practices

1. **Resource Management**: Always use `router.close()` to clean up resources.
2. **Error Handling**: Implement proper error handling for various scenarios.
3. **Ethical Automation**: Respect websites' `robots.txt` and implement rate limiting.
4. **Security**: Regularly update VPN configurations and use secure DNS.
5. **Performance**: Use browser recycling and warm-up techniques for optimal performance.

```python
import time

def rate_limited_execution(router, tasks, rate_limit):
    results = []
    for task in tasks:
        result = router.execute(task)
        results.append(result)
        time.sleep(1 / rate_limit)  # Sleep to respect rate limit
    return results

tasks = [Task(f"https://example.com/page/{i}", scrape_data) for i in range(100)]
results = rate_limited_execution(router, tasks, rate_limit=2)  # 2 requests per second
```

---

This documentation provides a comprehensive overview of the Browseek library for advanced multi-task and multi-browser automation. For more detailed information, advanced usage scenarios, and community support, please visit our official documentation website at https://docs.browseek.io






## Headless Browser Router Python Library

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
