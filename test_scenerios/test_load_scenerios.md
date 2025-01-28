# Load Test Scenarios for n11.com Search Module

## Scenario 1: Search with Valid Input
- **Action**: Search for a common term like "laptop".
- **Expectation**: The results page should load, and search results should match the input keyword.

## Scenario 2: Search with Invalid Input
- **Action**: Search for a random, non-existent term like "asdfghjkl12345".
- **Expectation**: The results page should display a "no results found" message.

## Scenario 3: Search with Empty Input
- **Action**: Perform a search with no input.
- **Expectation**: The page should handle the case gracefully without crashing.

## Scenario 4: Search with Special Characters
- **Action**: Search for special characters like "!@#$%^&*()".
- **Expectation**: The search results page should load, and the input should be sanitized.

## Scenario 6: Search with Common Query and Pagination
- **Action**: Search for a common term like "phone", then navigate to the second page of results.
- **Expectation**: The second page of results should load correctly.
