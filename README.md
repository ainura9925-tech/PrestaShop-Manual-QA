# PrestaShop Demo Store — Manual QA Testing Project

## Project Overview

This project demonstrates manual testing of the PrestaShop Demo Store web application.

The goal of the project was to evaluate the main customer-facing functionality of an e-commerce application, identify functional defects, document test coverage, and provide structured QA documentation.

Testing was performed using a risk-based approach with functional, usability, accessibility, basic security, and compatibility checks.

---

## Testing Scope

### In Scope

- Homepage and navigation
- User registration
- Authentication
- Login and logout
- Password reset
- Search and product catalog
- Product page
- Shopping cart
- Checkout
- Customer account
- Basic security checks
- Usability and UI
- Accessibility checks
- Basic browser compatibility checks

### Out of Scope

The following areas were not included in the project:

- Full regression testing
- Performance testing
- Load and stress testing
- Full security assessment / penetration testing
- Database testing
- Back Office testing
- Source code testing
- Full API testing
- Mobile application testing
- Automated testing
- Payment processing validation with real transactions

---

## Test Coverage

A total of **100 manual test cases** were created and executed.

The test cases cover the main customer-facing functionality of the PrestaShop Demo Store, including positive, negative, boundary, validation, usability, accessibility, security, and compatibility scenarios.

Test cases were created and managed in Qase.

---

## Test Execution Results

| Metric | Result |
|--------|--------|
| Total Test Cases | 100 |
| Passed | 98 |
| Failed | 2 |
| Blocked | 0 |
| Pass Rate | 98% |
| Defects Identified | 2 |
| Enhancements Identified | 1 |

### Failed Test Cases

The two failed test cases resulted in documented defects:

- **PSQA-10** — Registration with special characters in the first name field → [BUG-01](Bugs/BUG-01.md)
- **PSQA-87** — Password reset with a registered email address → [BUG-02](Bugs/BUG-02.md)

---

## Defects Identified

### BUG-01 — Unsupported special character is accepted in the first name field

**Severity:** Low  
**Priority:** Medium

The registration form accepts the `&` character in the First name field even though the field validation rule states that only letters and the dot (`.`) character followed by a space are allowed.

[View BUG-01](Bugs/BUG-01.md)

### BUG-02 — Password reset request fails for a registered email address

**Severity:** High  
**Priority:** High

The password recovery process fails for a registered email address and displays an error stating that the email could not be sent.

[View BUG-02](Bugs/BUG-02.md)

---

## Enhancement Proposal

### ENH-01 — Add password confirmation field during registration

A password confirmation field could be added to the registration form to reduce the risk of users entering an unintended password due to typing errors.

[View ENH-01](Enhancements/ENH-01.md)

---

## Test Environment

| Parameter | Details |
|-----------|---------|
| Application | PrestaShop Demo Store |
| Testing Type | Manual Web Application Testing |
| Platform | Desktop Web |
| Primary Browser | Google Chrome |
| Additional Browsers | Microsoft Edge, Safari |
| Test Management | Qase |
| Browser Tools | Chrome DevTools |
| Documentation | Markdown |
| Version Control | Git / GitHub |

### Compatibility Testing

Google Chrome was used as the primary testing browser.

Additional lightweight compatibility checks were performed in Microsoft Edge and Safari. These checks focused on main navigation, key links, and basic page functionality.

This was a lightweight compatibility check and **not a full cross-browser regression test**.

---

## Project Structure

```text
PrestaShop-Manual-QA/
│
├── README.md
│
├── Bugs/
│   ├── BUG-01.md
│   ├── BUG-02.md
│   └── screenshots/
│       ├── BUG-01.png
│       └── BUG-02.png
│
├── Checklists/
│   ├── Functional-Checklist.md
│   └── Smoke-Checklist.md
│
├── Enhancements/
│   └── ENH-01.md
│
├── Test-Cases/
│   ├── Accessibility.md
│   ├── Authentication.md
│   ├── Basic-Security-Checks.md
│   ├── Checkout.md
│   ├── Compatibility.md
│   ├── Customer-Account.md
│   ├── Homepage-Navigation.md
│   ├── Product-Page.md
│   ├── Registration.md
│   ├── Search-Catalog.md
│   ├── Shopping-Cart.md
│   └── Usability-UI.md
│
├── Test-data/
│   ├── Authentication_Test_Data.md
│   ├── Checkout_Test Data.md
│   └── Registration_Test_Data.md
│
├── Test-Plan/
│   └── Test-Plan.md
│
├── Test-Summary/
│   ├── Test-Summary-Report-from-QASE.pdf
│   └── Test_Summary_Report.md
│
├── data/
│   └── qase_test_cases.xlsx
│
└── scripts/
    └── generate_test_cases.py
```

---

## QA Documentation

### Test Plan

[Test Plan](Test-Plan/Test-Plan.md)

### Test Summary Report

[Test Summary Report](Test-Summary/Test_Summary_Report.md)

### Test Cases

[Test Cases](Test-Cases/)

### Checklists

[Checklists](Checklists/)

### Test Data

[Test Data](Test-data/)

### Bugs

[Bugs](Bugs/)

### Enhancement

[Enhancements](Enhancements/)

---

## Key Outcomes

- Created and executed **100 manual test cases**
- Achieved a **98% pass rate**
- Identified and documented **2 functional defects**
- Documented **1 enhancement proposal**
- Created functional and smoke checklists
- Prepared reusable test data
- Performed basic accessibility and security checks
- Performed lightweight compatibility checks in Chrome, Edge, and Safari
- Structured the project as a reusable QA portfolio artifact

---

## Author

**Zhussupova Ainur**

Manual QA Testing Portfolio Project