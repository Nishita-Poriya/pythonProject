import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestBookCartSearchFilter:
    @pytest.fixture
    def driver(self):
        """
        Setup method to initialize WebDriver before each test
        Using Chrome WebDriver for this example
        """
        # Initialize ChromeDriver
        driver = webdriver.Chrome()

        # Maximize browser window
        driver.maximize_window()

        # Navigate to BookCart website
        driver.get("https://bookcart.azurewebsites.net/")

        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search books or authors']"))
        )

        yield driver

        # Close browser after test
        driver.quit()

    def test_search_and_filter(self, driver):
        """
        Test method to perform search and filter functionality
        """
        # 1. Search for a specific book or category
        search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search books']")
        search_input.send_keys("fiction")

        # Click search button
        search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()

        # Wait for search results
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".book-card"))
        )

        # 2. Apply Genre Filter
        genre_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Fiction')]")
        genre_filter.click()

        # 3. Apply Price Range Filter
        price_min_input = driver.find_element(By.ID, "price-min")
        price_max_input = driver.find_element(By.ID, "price-max")

        # Set price range (example: $10-$50)
        price_min_input.clear()
        price_min_input.send_keys("10")
        price_max_input.clear()
        price_max_input.send_keys("50")

        # Apply price filter
        apply_price_button = driver.find_element(By.ID, "apply-price-filter")
        apply_price_button.click()

        # 4. Verify Search Results
        book_results = driver.find_elements(By.CSS_SELECTOR, ".book-card")

        # Validate number of results
        assert len(book_results) > 0, "No books found matching the search criteria"

        # Validate each book's genre and price
        for book in book_results:
            # Check genre
            book_genre = book.find_element(By.CSS_SELECTOR, ".book-genre").text
            assert "Fiction" in book_genre, f"Book {book} is not in Fiction genre"

            # Check price
            book_price = float(book.find_element(By.CSS_SELECTOR, ".book-price").text.replace('$', ''))
            assert 10 <= book_price <= 50, f"Book price {book_price} is outside the specified range"

        # Optional: Take screenshot for reporting
        driver.save_screenshot("search_filter_results.png")

        # Print total matching books
        print(f"Total matching books: {len(book_results)}")


# Allow running the script directly
if __name__ == "__main__":
    pytest.main(["-v", __file__])