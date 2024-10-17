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
