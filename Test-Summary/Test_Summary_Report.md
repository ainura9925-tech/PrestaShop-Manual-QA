# Test Summary Report

## 1. Project Overview

This document summarizes the results of manual testing performed on the PrestaShop Demo Store web application.

The objective of the testing was to evaluate the main customer-facing functionality, verify expected application behavior, identify defects, and assess basic usability, accessibility, security, and browser compatibility.

---

## 2. Test Execution

| Parameter | Details |
|-----------|---------|
| Application | PrestaShop Demo Store |
| Testing Type | Manual Web Application Testing |
| Test Execution Period | August–September 2026 |
| Platform | Desktop Web |
| Primary Browser | Google Chrome |
| Additional Browsers | Microsoft Edge, Safari |
| Test Management | Qase |
| Browser Tools | Chrome DevTools |

A total of **100 test cases** were executed.

---

## 3. Test Results

| Status | Count |
|--------|------:|
| Passed | 98 |
| Failed | 2 |
| Blocked | 0 |
| **Total** | **100** |

### Pass Rate

**98%**

The pass rate was calculated as:

**98 passed / 100 executed × 100 = 98%**

---

## 4. Failed Test Cases

Two test cases failed during execution.

| Test Case | Title | Result | Defect |
|-----------|-------|--------|--------|
| PSQA-10 | Registration with special characters in the first name field | Failed | BUG-01 |
| PSQA-87 | Password reset with a registered email address | Failed | BUG-02 |

---

## 5. Defects

### BUG-01 — Unsupported special character is accepted in the first name field

**Severity:** Low  
**Priority:** Medium  
**Status:** Open

The First name field accepts the `&` character even though the field validation rule states that only letters and the dot (`.`) character followed by a space are allowed.

As a result, registration can be completed using a value that does not comply with the stated field validation rule.

[View BUG-01](../Bugs/BUG-01.md)

---

### BUG-02 — Password reset request fails for a registered email address

**Severity:** High  
**Priority:** High  
**Status:** Open

When a registered email address is entered into the password recovery form, the application displays the following error:

`An error occurred while sending the email.`

The password reset process cannot be completed.

This prevents a registered customer from recovering access to their account through the password recovery functionality.

[View BUG-02](../Bugs/BUG-02.md)

---

## 6. Enhancement

### ENH-01 — Add password confirmation field during registration

A password confirmation field could be added to the registration form.

This would allow users to verify that the password was entered correctly and reduce the risk of accidental password-entry errors.

[View ENH-01](../Enhancements/ENH-01.md)

---

## 7. Compatibility Testing

Google Chrome was used as the primary browser throughout the test execution.

Additional lightweight compatibility checks were performed in:

- Microsoft Edge
- Safari

The compatibility checks focused on:

- Main navigation
- Key links
- Basic page functionality
- General rendering and interaction

These checks were limited in scope and **do not represent full cross-browser regression testing**.

---

## 8. Test Coverage

The executed test cases covered the following areas:

- Homepage and Navigation
- Registration
- Authentication
- Login and Logout
- Password Reset
- Search and Catalog
- Product Page
- Shopping Cart
- Checkout
- Customer Account
- Basic Security Checks
- Accessibility
- Usability and UI
- Compatibility

A total of **100 test cases** were executed across these areas.

---

## 9. Out of Scope

The following activities were not included in the testing scope:

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

## 10. Overall Assessment

The main customer-facing functionality of the PrestaShop Demo Store was tested using 100 manual test cases.

The final execution result was:

- **98 Passed**
- **2 Failed**
- **0 Blocked**
- **98% Pass Rate**
- **2 Defects Identified**
- **1 Enhancement Proposed**

The identified defects affect customer-facing functionality, including registration data validation and password recovery.

The testing results provide a documented overview of the application's current behavior within the defined testing scope.

---

## 11. Conclusion

Based on the executed test cases, the application demonstrated generally stable behavior across the tested functionality, with a **98% pass rate**.

Two functional issues were identified and documented as BUG-01 and BUG-02.

The testing was limited to the defined scope and should not be considered a full regression, performance, security, API, database, or mobile assessment.