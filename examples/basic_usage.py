import os
from dotenv import load_dotenv
from browseek import BrowserRouter

# Load environment variables from .env file
load_dotenv()

# TEST_URL = os.getenv("TEST_URL")
TEST_URL = 'https://softreck.com'

# Initialize the router
router = BrowserRouter()

# Add browser instances
router.add_browser("chrome", count=2)
router.add_browser("firefox", count=1)

# Use the router to perform a task
result = router.execute(TEST_URL, lambda page: page.title())
print(result)

# Clean up
router.close()
