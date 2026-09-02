# BUG-01 — Unsupported special character is accepted in the first name field

**Severity:** Low
**Priority:** Medium
**Status:** Open
**Environment:** PrestaShop Demo Store / Web / Desktop browser

## Preconditions

* User is not authenticated.
* Registration form is available.

## Steps to Reproduce

1. Open the PrestaShop Demo Store.
2. Navigate to the registration form.
3. Enter `Sarah&` in the **First name** field.
4. Enter valid data into all remaining required fields.
5. Submit the registration form.

## Actual Result

The value containing the `&` character is accepted, and the registration is completed successfully.

## Expected Result

The field tooltip states that only letters and the dot (`.`) character followed by a space are allowed. The `&` character is used to verify that unsupported special characters are rejected.

## Test Data

| Field      | Value                                                             |
| ---------- | ----------------------------------------------------------------- |
| First name | Sarah&                                                            |
| Last name  | Smith                                                             |
| Email      | [qa.registration@example.com](mailto:qa.registration@example.com) |

## Notes

The issue may result in invalid or unexpected customer name data being stored in the system.
