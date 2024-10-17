# Examples

This document provides examples of how to use the Browseek library for various scenarios.

## Basic Usage

```python
from browseek import BrowserRouter

router = BrowserRouter()
router.add_browser("chrome", count=2)
router.add_browser("firefox", count=1)

result = router.execute("https://example.com", lambda page: page.title())
print(result)

router.close()
```

## Request Redirection

```python
from browseek import BrowserRouter, RequestInterceptor

class CustomInterceptor(RequestInterceptor):
    def intercept(self, request):
        if request.resource_type == "image":
            request.abort()
        elif "ads" in request.url:
            request.redirect("about:blank")
        return request

router = BrowserRouter()
router.add_browser("chrome")
router.set_request_interceptor(CustomInterceptor())

result = router.execute("https://example.com", lambda page: len(page.query_selector_all("img")))
print(f"Number of images loaded: {result}")

router.close()
```

## DNS Security

```python
from browseek import BrowserRouter

router = BrowserRouter(config={"dns_over_https": True})

def check_dns_leak(page):
    page.goto("https://ipleak.net")
    return page.query_selector("#dnsips").inner_text()

task = "https://ipleak.net", check_dns_leak
dns_ips = router.execute(task)
print(f"DNS IPs: {dns_ips}")

router.close()
```

## CAPTCHA Handling

```python
from browseek import BrowserRouter, CaptchaSolver

class CustomCaptchaSolver(CaptchaSolver):
    def solve(self, captcha_type, captcha_data):
        # Implementation for solving CAPTCHAs
        pass

router = BrowserRouter()
router.add_browser("chrome")
router.set_captcha_solver(CustomCaptchaSolver())

def login_with_captcha(page):
    page.fill("#username", "user")
    page.fill("#password", "pass")
    captcha_element = page.query_selector("#captcha")
    if captcha_element:
        captcha_solution = router.solve_captcha("image", captcha_element.screenshot())
        page.fill("#captcha-solution", captcha_solution)
    page.click("#login-button")

task = "https://example.com/login", login_with_captcha
router.execute(task)

router.close()
```

## Device Simulation

```python
from browseek import BrowserRouter, DeviceProfile

iphone_profile = DeviceProfile(
    user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    screen_size=(375, 812),
    os="iOS",
    browser="Safari"
)

router = BrowserRouter()
router.add_browser("chrome")
router.set_device_profile(iphone_profile)

def check_mobile_version(page):
    return "mobile" in page.url

task = "https://example.com", check_mobile_version
is_mobile = router.execute(task)
print(f"Received mobile version: {is_mobile}")

router.close()
```

## Network Configuration

```python
from browseek import BrowserRouter, NetworkConfig

network_config = NetworkConfig(
    vpn_config={
        "provider": "nordvpn",
        "country": "us"
    },
    speed_limit=1000000  # 1 Mbps
)

router = BrowserRouter()
router.add_browser("chrome")
router.set_network_config(network_config)

def check_ip(page):
    page.goto("https://ifconfig.me")
    return page.query_selector("body").inner_text()

task = "https://ifconfig.me", check_ip
ip_address = router.execute(task)
print(f"Current IP: {ip_address}")

router.close()
```

## Docker Example

```python
from browseek import BrowserRouter

router = BrowserRouter()
router.add_browser("chrome")

def get_title(page):
    return page.title()

task = "https://example.com", get_title
result = router.execute(task)
print(result)

router.close()
```

To run the Docker example, use the following commands:

```bash
docker-compose build
docker-compose up
```

This will build the Docker image and start a container running the Browseek library with the example script.
