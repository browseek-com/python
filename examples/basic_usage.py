import os
import asyncio
from dotenv import load_dotenv
from browseek import BrowserRouter

# Load environment variables from .env file
load_dotenv()

TEST_URL = os.getenv("TEST_URL")

async def main():
    # Initialize the router
    router = BrowserRouter()

    # Add browser instances
    await router.add_browser("chromium", count=2)

    # Use the router to perform a task
    result = await router.execute(TEST_URL, lambda page: page.title())
    print(result)

    # Clean up
    await router.close()

if __name__ == "__main__":
    asyncio.run(main())
