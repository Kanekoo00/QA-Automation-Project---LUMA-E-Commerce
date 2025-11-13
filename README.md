# 🧪 QA Automation Project - LUMA E-Commerce

## 📋 Overview
This project is a **QA Automation Framework** built using **Python + Selenium + Pytest**.  
The goal is to automate testing for the **LUMA E-Commerce website** using a **data-driven approach**.

---

## 🧰 Requirements

### 1️⃣ Python Installation
Make sure **Python 3.11+** is installed.  
Check your version:
```bash
python --version
```

### 2️⃣ Install Project Dependencies
All dependencies are listed in `requirements.txt`.  
Run the following command to install them:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Project Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Kanekoo00/QA-Automation-Project---LUMA-E-Commerce.git
```

### 2️⃣ Navigate into the Project Folder
```bash
cd QA-Automation-Project---LUMA-E-Commerce
```

### 3️⃣ Project Structure
```
📦 QA-Automation-Project---LUMA-E-Commerce
 ┣ 📂 Tests/              → Test scripts (Pytest)
 ┣ 📂 Pages/              → Page Object Model (locators & actions)
 ┣ 📂 Utilities/          → Helper functions (Excel reader, config, etc.)
 ┣ 📂 Reports/            → Test result reports (HTML / Allure / XML)
 ┣ 📜 conftest.py         → Test setup & fixtures
 ┣ 📜 requirements.txt    → Dependencies
 ┗ 📜 README.md           → Documentation
```

---

## 🚀 Running the Tests

### ✅ Run All Tests (Exclude Manual Tests)
```bash
pytest -v -m "not manual"
```

This command will run all automated test cases, skipping any test marked as `@pytest.mark.manual`.

---

## 🧾 Generate Reports

### 📄 1️⃣ Generate HTML Report
```bash
pytest -v -m "not manual" --html=Reports/report.html --self-contained-html
```
- Report file: `Reports/report.html`  
- Open it directly in your browser to see:
  - ✅ Passed / ❌ Failed test cases  
  - ⏱ Execution time  
  - 🧩 Test names & details  

---

### 🧱 2️⃣ Generate JUnit XML Report (for CI/CD)
If you plan to integrate this project with Jenkins, GitHub Actions, or GitLab CI/CD:
```bash
pytest -v -m "not manual" --junitxml=Reports/results.xml
```
- Output file: `Reports/results.xml`
- This format is used by CI/CD tools for test result tracking.

---

### 🌈 3️⃣ Generate Allure Report (Interactive Dashboard)

#### Install Allure Command-Line Tool
If you haven’t installed Allure, run:
```bash
pip install allure-pytest
```

(Optional: you can also install the Allure command-line tool if needed for visualization)

#### Run Test and Generate Allure Results
```bash
pytest -v -m "not manual" --alluredir=Reports/allure-results
```

#### Generate and View Allure Report
```bash
allure serve Reports/allure-results
```

Allure will automatically:
- Generate the dashboard report
- Open it in your default browser with:
  - 📊 Graphs & Statistics
  - 🧩 Test Suites
  - 🕒 Execution timeline
  - ❌ Error trace & logs

---

## 🧼 Clean Old Reports
Before running a new test session, you can clear old reports with:
```bash
rm -rf Reports/*
```

---

## 💡 Tips

- Make sure your **ChromeDriver** or browser driver version matches your installed browser.
- Use a **virtual environment (venv)** to avoid dependency conflicts.
- Use `pytest -k <keyword>` to run a specific test (e.g., `pytest -k login`).
- Mark slow/manual tests with `@pytest.mark.manual` to skip them easily.

---

## 📄 Example HTML Report
Once executed, the HTML report will show a table of:
- Test names
- Execution results (Pass/Fail)
- Duration per test case
- Summary (total passed/failed/skipped)


Example:
```
3 tests executed in 00:01:34
✔ 3 Passed
✖ 0 Failed
⏩ 0 Skipped
```

---

## 👨‍💻 Author
**Budi Octaviandy (Kaneko00)**  
QA Automation Engineer | Python + Selenium | Data-Driven Framework

📧 [LinkedIn / GitHub: Kaneko00](https://github.com/Kanekoo00)

---
