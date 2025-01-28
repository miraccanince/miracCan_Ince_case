from locust import HttpUser, task, between
import random
import logging

class N11SearchUser(HttpUser):
    wait_time = between(1, 3)  # Simulate realistic wait time between actions

    # List of search keywords for the valid searches
    search_keywords = ["laptop", "phone", "shoes", "books", "headphones", "watch"]

    # Define headers to mimic browser behavior
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/132.0.6834.111 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.n11.com/",
    }

    @task(2)
    def valid_search(self):
        """Perform valid searches."""
        keyword = random.choice(self.search_keywords)
        logging.info(f"Performing valid search for keyword: {keyword}")
        with self.client.get(f"/arama?q={keyword}", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info(f"Valid search for '{keyword}' succeeded.")
            else:
                response.failure(f"Valid search for '{keyword}' failed with status code {response.status_code}")

    @task(1)
    def empty_search(self):
        """Perform empty searches without a query."""
        logging.info("Performing empty search (no query parameter).")
        with self.client.get("/arama?q=", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info("Empty search returned results (unexpected).")
            else:
                response.failure(f"Empty search failed with status code {response.status_code}")

    @task(1)
    def invalid_search(self):
        """Perform searches with invalid or special characters."""
        invalid_keywords = ["@#$%^&*", "<script>", "😎👍", "SELECT * FROM users", "random$chars"]
        keyword = random.choice(invalid_keywords)
        logging.info(f"Performing invalid search with keyword: {keyword}")
        with self.client.get(f"/arama?q={keyword}", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info(f"Invalid search for '{keyword}' succeeded (unexpected).")
            else:
                logging.info(f"Invalid search for '{keyword}' returned status code {response.status_code}.")

    @task(1)
    def long_search(self):
        """Perform searches with a very long keyword."""
        long_keyword = "a" * 1000  # 1000-character long string
        logging.info("Performing search with a long keyword.")
        with self.client.get(f"/arama?q={long_keyword}", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info("Long search request succeeded.")
            else:
                response.failure(f"Long search request failed with status code {response.status_code}")
  
    @task(1)
    def excessive_query_params(self):
        """Perform searches with excessive query parameters."""
        extra_params = "&".join([f"param{i}=value{i}" for i in range(20)])  # Generate 20 query parameters
        keyword = random.choice(self.search_keywords)
        logging.info(f"Performing search with excessive parameters for keyword: {keyword}")
        with self.client.get(f"/arama?q={keyword}&{extra_params}", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info(f"Search for '{keyword}' with excessive parameters succeeded.")
            else:
                response.failure(f"Search for '{keyword}' with excessive parameters failed with status code {response.status_code}")
