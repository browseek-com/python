import os
from dotenv import load_dotenv
from browseek import BrowserRouter

# Load environment variables from .env file
load_dotenv()

TEST_URL = os.getenv("TEST_URL")

router = BrowserRouter()
router.add_browser("chrome")

def get_title(page):
    return page.title()

task = TEST_URL, get_title
result = router.execute(task)
print(result)

router.close()
