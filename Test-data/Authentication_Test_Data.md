# Authentication — Test Data

## 1. Valid Credentials

Used for testing successful login.

| Field | Test Value |
|---|---|
| Email | qa.login@example.com |
| Password | `<valid password>` |

> The credentials must belong to an existing test account.

---

## 2. Incorrect Password

Used for testing login with a valid email and incorrect password.

| Field | Test Value |
|---|---|
| Email | qa.login@example.com |
| Password | `WrongPass123!` |

> The email must belong to an existing test account.

---

## 3. Unregistered Email

Used for testing login with an email address that is not associated with an account.

| Field | Test Value |
|---|---|
| Email | unregistered.user@example.com |
| Password | `<valid password>` |

> The email address must not be associated with an existing account.

---

## 4. Empty Email

| Field | Test Value |
|---|---|
| Email | Empty |
| Password | `<valid password>` |

---

## 5. Empty Password

| Field | Test Value |
|---|---|
| Email | qa.login@example.com |
| Password | Empty |

> The email must belong to an existing test account.

---

## 6. Invalid Email Format

| Test Value | Validation Scenario |
|---|---|
| qa.loginexample.com | Missing `@` symbol |
| qa.login@example | Missing domain extension |
| qa.login@ | Missing domain |

---

## 7. Logout

No additional test data is required.

> A valid authenticated customer account is required to perform the logout action.

---

## 8. Access Account After Logout

No additional test data is required.

> The user must be logged in before performing the logout action.

---

## 9. Password reset with registered email

| Field | Test Value |
|---|---|
| Registered email | `qa.login@example.com` |
| New password | `NewPassword123!` |

---

## 10. Password reset with unregistered email

| Field | Test Data |
|---|---|
| Unregistered email | `unregistered@example.com` |