import unittest
from unittest.mock import MagicMock, patch

from browseek import BrowserRouter, BrowserInstance, Task

class TestBrowserRouter(unittest.TestCase):
    def setUp(self):
        self.router = BrowserRouter()

    def test_add_browser(self):
        self.router.add_browser("chrome", count=2)
        self.assertEqual(len(self.router.browsers), 2)
        self.assertIsInstance(self.router.browsers[0], BrowserInstance)

    def test_execute_task(self):
        mock_browser = MagicMock(spec=BrowserInstance)
        mock_browser.is_available.return_value = True
        self.router.browsers = [mock_browser]

        task = Task("https://example.com", lambda page: page.title())
        result = self.router.execute(task)

        mock_browser.configure.assert_called_once()
        mock_browser.cleanup.assert_called_once()
        self.assertEqual(result, mock_browser.execute.return_value)

    def test_execute_batch(self):
        mock_browser = MagicMock(spec=BrowserInstance)
        mock_browser.is_available.return_value = True
        self.router.browsers = [mock_browser]

        tasks = [
            Task("https://example.com", lambda page: page.title()),
            Task("https://example.org", lambda page: page.url)
        ]
        results = self.router.execute_batch(tasks)

        self.assertEqual(len(results), 2)
        mock_browser.configure.assert_called()
        mock_browser.cleanup.assert_called()

    def test_close(self):
        mock_browser1 = MagicMock(spec=BrowserInstance)
        mock_browser2 = MagicMock(spec=BrowserInstance)
        self.router.browsers = [mock_browser1, mock_browser2]

        self.router.close()

        mock_browser1.quit.assert_called_once()
        mock_browser2.quit.assert_called_once()
        self.assertEqual(len(self.router.browsers), 0)

if __name__ == '__main__':
    unittest.main()
