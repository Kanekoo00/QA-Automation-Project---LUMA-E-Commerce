# 🧪 Test Execution Guide

Panduan lengkap menjalankan test untuk QA Automation Project --- LUMA
E-Commerce.

------------------------------------------------------------------------

## 🚀 1. Run All Tests

Jalankan seluruh test otomatis (skip manual):

``` bash
pytest -v -m "not manual"
```

------------------------------------------------------------------------

## 🎯 2. Run Specific Test Suites

### ▶ Run login tests only

``` bash
pytest -k login -v
```

### ▶ Run smoke tests only

``` bash
pytest -m smoke -v
```

### ▶ Run regression tests only

``` bash
pytest -m regression -v
```

### ▶ Run tests except manual

``` bash
pytest -m "not manual" -v
```

### ▶ Run a single test file

``` bash
pytest Tests/test_login.py -v
```

### ▶ Run a specific test method

``` bash
pytest Tests/test_login.py::TestLogin::test_valid_login -v
```

------------------------------------------------------------------------

## 📄 3. Generate Reports

### ▶ HTML Report

``` bash
pytest -v -m "not manual" --html=Reports/report.html --self-contained-html
```

### ▶ JUnit XML Report (CI/CD)

``` bash
pytest -v -m "not manual" --junitxml=Reports/results.xml
```

### ▶ Allure Results

Generate allure results:

``` bash
pytest -v -m "not manual" --alluredir=Reports/allure-results
```

Serve report:

``` bash
allure serve Reports/allure-results
```

------------------------------------------------------------------------

## 🏷️ 4. Pytest Marker Guide

Project ini menggunakan marker untuk mengelompokkan test case.

### 📌 Available Markers

  -----------------------------------------------------------------------
  Marker                      Description
  --------------------------- -------------------------------------------
  **smoke**                   Quick & essential checks to verify major
                              functionality

  **regression**              Full suite untuk memastikan tidak ada
                              defect sebelum release

  **manual**                  Test case yang tidak dijalankan oleh
                              automation
  -----------------------------------------------------------------------

### 📘 Example Usage

``` python
import pytest

@pytest.mark.smoke
def test_valid_login(self):
    ...

@pytest.mark.regression
def test_checkout_process(self):
    ...

@pytest.mark.manual
def test_payment_with_cod(self):
    ...
```

------------------------------------------------------------------------

## 🧼 5. Clean Old Reports

Sebelum menjalankan test baru:

### Windows PowerShell

``` bash
Remove-Item -Recurse -Force Reports/*
```

### Linux / macOS

``` bash
rm -rf Reports/*
```

------------------------------------------------------------------------
