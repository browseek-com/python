import os
from dotenv import load_dotenv
from browseek import BrowserRouter

# Load environment variables from .env file
load_dotenv()

TEST_URL = os.getenv("TEST_URL")

router = BrowserRouter(config={"dns_over_https": True})

def check_dns_leak(page):
    page.goto("https://ipleak.net")
    return page.query_selector("#dnsips").inner_text()

task = TEST_URL, check_dns_leak
dns_ips = router.execute(task)
print(f"DNS IPs: {dns_ips}")

router.close()
