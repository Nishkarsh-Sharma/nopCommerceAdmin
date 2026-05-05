# nopCommerce Admin Automation Framework 🚀

A robust, data-driven web automation framework built to test the admin portal of the nopCommerce e-commerce platform. 

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Tool:** Selenium WebDriver
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)

## 🌟 Key Features
* **Data-Driven Testing (DDT):** Capable of reading and executing test cases across multiple data sets using Excel utilities.
* **Centralized Configuration:** Base URLs and credentials managed securely via `config.ini`.
* **Automated Logging:** Custom `LogGen` utility generates detailed execution logs for every test run.
* **Failure Capture:** Automatically captures and saves screenshots if an assertion fails.
* **HTML Reporting:** Integrated with `pytest-html` to generate visually comprehensive test dashboards.

## ⚙️ How to Run the Tests
To execute the test suite and generate an HTML report, run the following command in the terminal:
`pytest -v -s -n=2 --html=Reports/report.html TestCases/`