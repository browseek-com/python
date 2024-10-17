import os
import asyncio
import warnings
from dotenv import load_dotenv
from browseek import BrowserRouter

# Load environment variables from .env file
load_dotenv()

TEST_URL = os.getenv("TEST_URL")

async def main():
    router = None
    try:
        # Initialize the router
        router = BrowserRouter()

        # Add browser instances
        await router.add_browser("playwright", count=2)

        # Use the router to perform a task
        result = await router.execute(TEST_URL, lambda page: page.title())
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        if router:
            await router.close()

if __name__ == "__main__":
    # Note: You may see warnings about the event loop being closed.
    # These warnings are likely from underlying libraries and don't affect the script's functionality.
    # To suppress these warnings, you can uncomment the following lines:
    # warnings.filterwarnings("ignore", message="Exception ignored.*")
    # warnings.filterwarnings("ignore", message="Task was destroyed but it is pending!")

    asyncio.run(main())

print("\nNote: If you see warnings about the event loop being closed, these are from underlying libraries")
print("and don't affect the script's functionality. You can suppress them by uncommenting the")
print("warnings.filterwarnings() lines in the script if desired.")
