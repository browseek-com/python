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
