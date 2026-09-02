# Authentication — Test Cases

## PSQA-12 — Login with valid credentials

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User has a registered account.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Enter a valid registered email address. | Email address is accepted. |
| 4 | Enter the valid password associated with the account. | Password is accepted. |
| 5 | Click Sign in. | User is successfully authenticated and redirected to the customer account page. |
## PSQA-13 — Login with incorrect password

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User has a registered account.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Enter a registered email address. | Email is accepted. |
| 4 | Enter an incorrect password. | Password is accepted in the input field. |
| 5 | Click Sign in. | Authentication fails and an appropriate error message is displayed. |
| 6 | Review the page. | User remains unauthenticated |
## PSQA-14 — Login with unregistered email

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Enter an unregistered email address. | Email is accepted. |
| 4 | Enter any password. | Password is accepted in the input field. |
| 5 | Click Sign in. | Authentication fails and an appropriate error message is displayed. |
| 6 | Review the account area. | User remains unauthenticated. |
## PSQA-15 — Login with empty email

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Leave the email field empty. | Email field remains empty. |
| 4 | Enter any password. | Password is accepted. |
| 5 | Click Sign in. | Login is not completed and appropriate validation is displayed for the email field. |
## PSQA-16 — Login with empty password

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Enter a registered email address. | Email is accepted. |
| 4 | Leave the password field empty. | Password field remains empty. |
| 5 | Click Sign in. | Login is not completed and appropriate validation is displayed for the password field. |
## PSQA-17 — Login with invalid email format

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Enter an invalid email format. | Invalid email is entered into the field. |
| 4 | Enter any password. | Password is accepted. |
| 5 | Click Sign in. | Login is not completed and an appropriate validation message is displayed. |
## PSQA-18 — Logout from customer account

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is successfully authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Locate the Sign out option. | Sign out option is visible. |
| 3 | Click Sign out. | User is logged out. |
| 4 | Review the page. | User is redirected to the appropriate page and the Sign in option is displayed. |
## PSQA-19 — Access account after logout

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User has a registered account.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Click Sign out. | User is logged out. |
| 3 | Use the browser Back button. | Previous page is displayed or the user remains unauthenticated. |
| 4 | Try to access the customer account page again. | User is not granted access to authenticated account content and is redirected to the login page or appropriate unauthenticated page. |
## PSQA-87 — Password reset with registered email

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User has a registered account.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Click Sign in. | Sign-in page is displayed. |
| 3 | Select Forgot your password? | Password recovery form is displayed. |
| 4 | Enter a registered email address. | Email address is entered successfully. |
| 5 | Submit the password recovery form. | Password reset confirmation message is displayed. |
| 6 | Open the registered email inbox. | Password reset email is received. |
| 7 | Open the password reset link from the email. | Password reset page is displayed. |
| 8 | Enter a new valid password and confirm it. | New password is accepted. |
| 9 | Submit the new password. | Password is successfully reset. |
| 10 | Log in using the registered email and new password. | User is successfully authenticated. |
## PSQA-88 — Password reset with unregistered email

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the login page. | Login page is displayed. |
| 2 | Select Forgot your password? | Password recovery form is displayed. |
| 3 | Enter an unregistered email address. | Email address is entered successfully. |
| 4 | Submit the password recovery form. | Appropriate message is displayed indicating that the email is not associated with an account, or the system displays a generic confirmation message without revealing whether the account exists. |
| 5 | Check the inbox of the unregistered email address. | No password reset email is received. |
