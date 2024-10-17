from browseek import BrowserRouter

router = BrowserRouter()
router.add_browser("chrome")

def get_title(page):
    return page.title()

task = "https://example.local", get_title
result = router.execute(task)
print(result)

router.close()
