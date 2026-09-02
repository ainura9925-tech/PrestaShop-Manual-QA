# Registration — Test Data

Test data used for registration and input validation scenarios in the PrestaShop Demo Store.

---

## 1. Valid Registration Data

| Field | Test Value |
|---|---|
| First name | Sarah |
| Last name | Smith |
| Email | `qa.test@example.com` |
| Password | `<valid password>` |
| Date of birth | 20/04/2001 |

> Use a unique email address when testing successful registration.

---

## 2. Existing Email

Used for testing registration with an email address that is already associated with an existing account.

| Field | Test Value |
|---|---|
| Email | `qa.test@example.com` |

> The email address must already be associated with an existing test account.

---

## 3. Invalid Email Formats

Used to verify validation of incorrectly formatted email addresses.

| Test Value | Validation Scenario |
|---|---|
| `sarah.smith.example.com` | Missing `@` symbol |
| `sarah.smith@example` | Missing domain extension |
| `sarah.smithexample.com` | Missing `@` symbol |

---

## 4. Password Validation

The application indicates a minimum password length of **8 characters**.

| Test Value | Purpose |
|---|---|
| `aB12345` | 7 characters — one character below the minimum |
| `<valid password>` | Valid password within the allowed range |

> The test suite covers a password below the minimum boundary. No additional password boundary cases are included.

---

## 5. Leading and Trailing Spaces

Used to verify how the application handles leading and trailing spaces in registration fields.

| Field | Test Value |
|---|---|
| First name | ` Sarah ` |
| Last name | ` Smith ` |
| Email | ` qa.test@example.com ` |

> Leading and trailing spaces are intentionally included in the test values.

---

## 6. Special Characters in Name

Used to verify how the application handles special characters in first name fields.

| Field | Test Value |
|---|---|
| First name | `Sarah&` |

> The test verifies whether the application accepts or rejects the special character according to its input validation rules.

---

## 7. Maximum Field Length

The application indicates a maximum field length of **255 characters** for the tested field.

| Boundary | Length | Purpose |
|---|---:|---|
| Below maximum | 254 characters | Verify that a value one character below the maximum is accepted |
| Maximum | 255 characters | Verify that the maximum allowed value is accepted |
| Above maximum | 256 characters | Verify that the additional character is prevented or an appropriate validation is displayed |

> The 255-character limit is based on the maximum length indicated by the application's field information.

---

## 8. One-Character Names

Used to verify whether first and last names consisting of a single character are accepted.

| Field | Test Value |
|---|---|
| First name | `A` |
| Last name | `B` |

---

## 9. Invalid Date Value

Used to verify validation of a date that follows the expected format but represents a non-existent calendar date.

| Field | Test Value |
|---|---|
| Date of birth | `31/02/2001` |

> `31/02/2001` uses the expected date format but represents an invalid calendar date.