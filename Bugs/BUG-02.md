# BUG-02 — Password reset request fails for a registered email address

**Severity:** High
**Priority:** High
**Status:** Open
**Environment:** PrestaShop Demo Store / Web / Desktop browser

## Preconditions

* A registered customer account exists.
* User is not authenticated.

## Steps to Reproduce

1. Open the PrestaShop Demo Store.
2. Click **Sign in**.
3. Select **Forgot your password?**
4. Enter a registered email address.
5. Submit the password recovery form.

## Actual Result

An error message is displayed:

`An error occurred while sending the email.`

The password reset process cannot be completed.

## Expected Result

A password reset request should be successfully processed, and a password reset email should be sent to the registered email address.

## Test Data

| Field | Value                                               |
| ----- | --------------------------------------------------- |
| Email | [qa.login@example.com](mailto:qa.login@example.com) |

## Impact

A registered customer cannot recover access to their account using the password reset functionality.
