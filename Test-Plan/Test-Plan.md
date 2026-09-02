# Test Plan — PrestaShop Demo Store

## 1. Project Overview

### Application

PrestaShop Demo Store

### Testing Type

Manual Web Application Testing

### Objective

The objective of this project is to evaluate the main customer-facing functionality of the PrestaShop Demo Store, verify expected behavior, identify defects, and document the testing process and results.

The testing focuses on functional behavior as well as selected usability, accessibility, basic security, and browser compatibility checks.

---

## 2. Scope

### 2.1 In Scope

The following areas are included in testing:

- Homepage and Navigation
- User Registration
- Authentication
- Login and Logout
- Password Reset
- Search and Product Catalog
- Product Page
- Shopping Cart
- Checkout
- Customer Account
- Basic Security Checks
- Usability and UI
- Accessibility
- Browser Compatibility

---

### 2.2 Out of Scope

The following areas are excluded from the project:

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

## 3. Test Approach

Testing is performed using a manual, risk-based approach.

The test suite includes:

- Positive testing
- Negative testing
- Boundary and validation testing
- Functional testing
- UI and usability testing
- Accessibility checks
- Basic security checks
- Basic browser compatibility checks

The testing focuses primarily on customer-facing functionality and common user flows.

---

## 4. Test Coverage

A total of **100 manual test cases** were created and executed.

The test cases cover:

| Area | Coverage |
|------|----------|
| Homepage & Navigation | Included |
| Registration | Included |
| Authentication | Included |
| Search & Catalog | Included |
| Product Page | Included |
| Shopping Cart | Included |
| Checkout | Included |
| Customer Account | Included |
| Basic Security | Included |
| Accessibility | Included |
| Usability & UI | Included |
| Compatibility | Included |

---

## 5. Test Environment

| Parameter | Details |
|-----------|---------|
| Application | PrestaShop Demo Store |
| Platform | Desktop Web |
| Primary Browser | Google Chrome |
| Additional Browsers | Microsoft Edge, Safari |
| Test Management | Qase |
| Browser Tools | Chrome DevTools |
| Documentation | Markdown |
| Version Control | Git / GitHub |

### Browser Compatibility

Google Chrome was used as the primary browser for test execution.

Additional lightweight compatibility checks were performed using Microsoft Edge and Safari.

These checks focused on:

- Main navigation
- Key links
- Basic page functionality
- General rendering and interaction

The compatibility checks were limited in scope and were **not intended to replace full cross-browser regression testing**.

---

## 6. Test Data

Test data was prepared for the following areas:

- Registration
- Authentication
- Checkout

Test data files are stored in the `Test-data/` directory.

Test data includes valid and invalid values used for input validation and negative testing scenarios.

---

## 7. Test Management

Test cases were created and managed using Qase.

The project contains **100 test cases** covering the defined testing scope.

Test execution results were recorded in Qase and summarized in the Test Summary Report.

---

## 8. Defect Management

Defects identified during testing were documented separately using structured bug reports.

Each defect report contains:

- Defect ID
- Title
- Severity
- Priority
- Status
- Environment
- Preconditions
- Steps to Reproduce
- Actual Result
- Expected Result
- Test Data
- Additional notes or impact

The following defects were identified:

| ID | Description | Severity | Priority |
|----|-------------|----------|----------|
| BUG-01 | Unsupported special character is accepted in the first name field | Low | Medium |
| BUG-02 | Password reset request fails for a registered email address | High | High |

---

## 9. Enhancement

One enhancement proposal was documented separately:

**ENH-01 — Add password confirmation field during registration**

The proposal is classified as an enhancement rather than a defect because the current registration flow can be completed successfully without a password confirmation field.

---

## 10. Entry Criteria

Testing can begin when:

- The application is available and accessible.
- The required testing environment is available.
- Test cases have been prepared.
- Required test data is available.
- The main application functionality is accessible for testing.

---

## 11. Exit Criteria

Testing is considered complete when:

- All planned test cases have been executed.
- Test results have been recorded.
- Failed test cases have been reviewed.
- Identified defects have been documented.
- Test execution results have been summarized.
- Test documentation has been prepared.

---

## 12. Deliverables

The project deliverables include:

- Test Plan
- Test Cases
- Test Data
- Functional Checklist
- Smoke Checklist
- Test Execution Results
- Test Summary Report
- Bug Reports
- Enhancement Proposal
- Qase Test Case Export
- Supporting screenshots

---

## 13. Tools

### Qase

Used for:

- Test case management
- Test execution
- Recording test results
- Test reporting

### Chrome DevTools

Used for:

- Inspecting page elements
- Checking browser console messages
- Reviewing network requests
- Supporting defect investigation

### Git / GitHub

Used for:

- Version control
- Project organization
- Portfolio presentation

### Markdown

Used for:

- Test documentation
- Bug reports
- Test plan
- Test summary
- Test data documentation

---

## 14. Risks and Limitations

The testing project has the following limitations:

- Testing was performed on a demo environment.
- The project does not represent full regression testing.
- Performance and load behavior were not evaluated.
- No full penetration testing or security assessment was performed.
- Database and source code were not tested.
- Full API testing was not performed.
- Mobile application testing was not included.
- Automated testing was not included.
- Payment processing was not validated using real transactions.
- Browser compatibility testing was limited to basic checks in Chrome, Edge, and Safari.

---

## 15. Expected Test Results

The expected outcome of the testing is to:

- Verify the main customer-facing functionality.
- Identify functional defects.
- Detect validation and usability issues.
- Document reproducible problems.
- Provide structured QA documentation.
- Assess the application within the defined testing scope.

---

## 16. Final Test Execution

The final test execution consisted of **100 test cases**.

| Result | Count |
|--------|------:|
| Passed | 98 |
| Failed | 2 |
| Blocked | 0 |
| **Total** | **100** |

**Pass Rate: 98%**

Two failed test cases resulted in documented defects:

- PSQA-10 → BUG-01
- PSQA-87 → BUG-02

The final execution results are documented in the [Test Summary Report](../Test-Summary/Test_Summary_Report.md).