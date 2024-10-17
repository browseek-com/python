from browseek import BrowserRouter

router = BrowserRouter(config={"dns_over_https": True})

def check_dns_leak(page):
    page.goto("https://ipleak.net")
    return page.query_selector("#dnsips").inner_text()

task = "https://ipleak.net", check_dns_leak
dns_ips = router.execute(task)
print(f"DNS IPs: {dns_ips}")

router.close()
