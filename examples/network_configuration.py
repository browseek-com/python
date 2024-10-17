import os
from dotenv import load_dotenv
from browseek import BrowserRouter, NetworkConfig

# Load environment variables from .env file
load_dotenv()

TEST_URL = os.getenv("TEST_URL")

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

task = TEST_URL, check_ip
ip_address = router.execute(task)
print(f"Current IP: {ip_address}")

router.close()
