# Test Scenarios for UseInsider Website Automation

## Overview
This document outlines the test scenarios for automating functional checks on the UseInsider website. The tests include navigation verification, filtering of job listings, and redirection validation for the career-related pages.

---

## Test Scenarios

### 1. Verify Insider Homepage is Opened
**Description**: Validate that the Insider homepage is accessible and properly loaded.

- **Steps**:
  1. Open the browser (Chrome or Firefox).
  2. Navigate to `https://useinsider.com/`.
  3. Verify that the homepage is successfully loaded.
  4. Confirm that the page title contains "Insider" or a related keyword.
  5. Check for the presence of the main navigation bar.

- **Expected Result**:
  - Insider homepage is loaded successfully with the correct title and navigation bar visible.

---

### 2. Verify "Careers" Page and Subsections
**Description**: Navigate to the Careers page via the "Company" menu and verify that all relevant blocks are displayed.

- **Steps**:
  1. On the homepage, locate the "Company" menu in the navigation bar.
  2. Click on the "Careers" option.
  3. Verify that the Careers page is opened (`https://useinsider.com/careers/`).
  4. Verify the presence of the following blocks on the Careers page:
     - **Locations**
     - **Teams**
     - **Life at Insider**

- **Expected Result**:
  - The Careers page opens successfully.
  - All three blocks (Locations, Teams, and Life at Insider) are visible and accessible.

---

### 3. Verify Job Filtering for Quality Assurance in Istanbul, Turkey
**Description**: Navigate to the QA jobs section, filter jobs by location and department, and check the results.

- **Steps**:
  1. On the Careers page, scroll to the "Quality Assurance" section and click "See all QA jobs."
  2. Verify redirection to the jobs page (`https://useinsider.com/careers/quality-assurance/`).
  3. Use the filtering options:
     - Set **Location** to "Istanbul, Turkey."
     - Set **Department** to "Quality Assurance."
  4. Verify that the list of jobs is displayed.

- **Expected Result**:
  - Jobs page is loaded successfully.
  - Jobs are filtered, and a list of available Quality Assurance jobs in Istanbul, Turkey, is displayed.

---

### 4. Verify Job Details Contain Correct Information
**Description**: Validate the details of the job list, ensuring they match the filtering criteria.

- **Steps**:
  1. Verify that all job positions in the list contain the term **"Quality Assurance"**.
  2. Verify that all job departments are **"Quality Assurance"**.
  3. Verify that all job locations are **"Istanbul, Turkey"**.

- **Expected Result**:
  - All job listings match the selected filters for **Position**, **Department**, and **Location**.

---

### 5. Verify Job Redirection to Application Form
**Description**: Validate that clicking the "View Role" button redirects to the Lever Application form.

- **Steps**:
  1. On the filtered job list, locate a job and click the **"View Role"** button.
  2. Verify that clicking this button redirects to the Lever Application form page.
  3. Confirm that the Lever Application form contains the correct job title and details.

- **Expected Result**:
  - Clicking "View Role" successfully redirects to the Lever Application form with accurate job details.

---
