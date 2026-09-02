# ENH-01 — Add password confirmation field during registration

**Type:** Enhancement
**Priority:** Medium
**Status:** Proposed

## Description

Add a password confirmation field to the registration form.

Currently, the user enters the password only once during account registration.

## Current Behavior

The registration form contains a single password field. The user can submit the registration without re-entering the password for confirmation.

## Proposed Improvement

Add a **Confirm password** field below the password field.

The system should compare the password and confirmation values before allowing the registration to be completed.

## Expected Behavior

* The user enters a password.
* The user enters the same password in the confirmation field.
* If both values match, registration can proceed.
* If the values do not match, an appropriate validation message is displayed.
* Registration cannot be completed until the password values match.

## Benefit

Adding password confirmation could reduce the possibility of users accidentally entering an unintended password and being unable to log in after registration.
