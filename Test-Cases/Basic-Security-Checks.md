# Basic Security Checks — Test Cases

## PSQA-89 — Password is masked

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Login/registration form is open.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Click the password field. | Password field is active. |
| 2 | Enter a password. | Password characters are masked and are not displayed as plain text. |
## PSQA-90 — Password is not exposed in URL

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the login page. | Login page is displayed. |
| 2 | Enter a password. | Password is entered. |
| 3 | Submit the login form. | Authentication request is processed. |
| 4 | Review the browser URL. | Password is not present in the URL or query parameters. |
## PSQA-91 — Sensitive data is not stored in browser URL

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Perform an authentication-related action. | Request is sent successfully. |
| 2 | Review the browser address bar. | Passwords and other sensitive credentials are not exposed in the URL. |
## PSQA-92 — Unauthenticated user cannot access account page

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Log in successfully. | Customer account is accessible. |
| 2 | Log out. | User is logged out. |
| 3 | Use navigation/browser history to return to the account page. | User is not granted access to authenticated account content. |
## PSQA-93 — Session is invalidated after logout

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Log in to a customer account. | User is authenticated. |
| 2 | Open DevTools → Application/Storage → Cookies. | Session-related cookies can be inspected. |
| 3 | Log out. | User is logged out. |
| 4 | Review the session state/cookies. | Verify that the user session is terminated after logout |
| 5 | Attempt to access an authenticated page. | User is not authenticated. |
## PSQA-94 — Sensitive information is not exposed in Network requests

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Browser DevTools is available.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Open browser DevTools and select the Network tab. | Network requests are displayed. |
| 3 | Perform a login or checkout action using test data. | Relevant network requests are generated. |
| 4 | Review request URLs, parameters, payloads, and responses. | Sensitive information such as passwords is not exposed in URLs, query parameters, or responses. |
| 5 | Review the Network entries containing authentication or checkout data. | No unnecessary sensitive information is exposed. |
## PSQA-95 — HTTPS is used for authentication

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the login page. | Login page is displayed. |
| 2 | Review the browser address bar. | Authentication page uses HTTPS. |
| 3 | Submit login credentials. | Authentication request is sent over a secure HTTPS connection. |
## PSQA-96 — Security-related browser console errors

**Priority:** High  
**Behavior:** Positive  
**Type:** Security  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open DevTools → Console. | Console is displayed. |
| 2 | Navigate through login/registration pages. | Pages function normally. |
| 3 | Perform normal authentication actions. | Verify that no critical JavaScript errors occur during authentication flows |
