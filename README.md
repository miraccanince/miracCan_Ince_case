# miracCan_Ince_case

# Test Automation Project

## Overview
This repository contains automated tests for:
1. **Web UI Testing**: Automated tests for the [Insider](https://useinsider.com/) website.
2. **Load Testing**: Performance testing of the search module on [n11.com](https://www.n11.com/).
3. **API Testing**: CRUD operations on the Petstore API using [Swagger Petstore](https://petstore.swagger.io/).

---

##  Web UI Automation (Selenium)
### ✅ Test Scenarios:
1. **Navigate to Insider Website**
   - Open [Insider Homepage](https://useinsider.com/) and verify successful loading.
   
2. **Navigate to Careers Page**
   - Click the "Company" menu, select "Careers", and validate the Career page.
   - Check "Locations", "Teams", and "Life at Insider" sections.
   
3. **Find QA Jobs in Istanbul**
   - Open [Insider Careers](https://useinsider.com/careers/quality-assurance/) page.
   - Click "See all QA jobs".
   - Filter by Location: "Istanbul, Turkey" and Department: "Quality Assurance".
   - Validate job listings contain "Quality Assurance" in position, department, and location.

4. **View Job Details**
   - Click "View Role" and confirm redirection to the Lever Application Form.

---

##  Load Testing (Locust)
### ✅ Test Scenarios:
1. **Simulate User Load on Search Module**
   - Perform search queries on [n11.com](https://www.n11.com/) and measure response times.
   
2. **Performance Metrics**
   - Test response time under increasing user loads.
   - Validate system stability under concurrent requests.

---

##  API Testing (Swagger Petstore)
### ✅ CRUD Operations
- **Create a Pet** (`POST /pet`)
- **Get Pet Details** (`GET /pet/{petId}`)
- **Update Pet Details** (`PUT /pet`)
- **Delete a Pet** (`DELETE /pet/{petId}`)
- **Find Pets by Status** (`GET /pet/findByStatus`)

### ✅ Test Scenarios
- ✅ Positive & Negative cases for CRUD operations.
- ✅ Invalid ID scenarios for GET/DELETE requests.
- ✅ Empty request body validation.

---

## 🛠️ Technologies Used
- **Python**
- **Pytest** (for functional API/UI tests)
- **Selenium** (for web automation)
- **Locust** (for load testing)
- **Requests** (for API testing)
- **Logging & Reporting** (logs stored in `test_automation.log`)
- **Excel Reporting** (automated test reports in `.xlsx` format)

---

### 🛠 Installation Guide

#### 1️⃣ Clone the Repository
```sh
git clone https://github.com/miraccanince/miracCan_Ince_case.git
cd miracCan_Ince_case
```

#### 2️⃣ Create a Virtual Environment (Recommended)
It is highly recommended to use a virtual environment to manage dependencies.
```sh
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Install Dependencies
After activating the virtual environment, install the required dependencies:
```sh
pip install -r requirements.txt
```

#### 4️⃣ Run the Tests
To execute the test cases, use:
```sh
pytest
```
UI Tests
```sh
pytest tests/test_careers_page.py
pytest tests/home_page.py

```
API Tests
```sh
pytest api_tests/tests/test_petstore_api.py
```

#### 5️⃣ Run Load Tests (If Applicable)
If you're using Locust:
```sh
locust -f locustfile.py
```

#### 6️⃣ Deactivate the Virtual Environment (When Done)
```sh
deactivate
```

## 📊 Reporting
- **Test Logs:** `test_automation.log`
- **Excel Report:** Automatically generated in `api_tests/reports/`

---

## 🤝 Contributing
Feel free to submit issues or pull requests to improve the tests.

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
