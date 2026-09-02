# Registration — Test Cases

## PSQA-4 — Registration with valid data

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated. A unique email address is available for registration.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed successfully. |  |
| 2 | Click Sign in. | Sign-in page is displayed. |  |
| 3 | Click Create an account. | Registration form is displayed. |  |
| 4 | Select a valid social title, if applicable. | Selected title is displayed. |  |
| 5 | Enter a valid first name. | First name is accepted. | Sarah |
| 6 | Enter a valid last name. | Last name is accepted. | Smith |
| 7 | Enter a unique valid email address. | Email address is accepted. | qa.test@example.com |
| 8 | Enter a valid password. | Password is accepted. | <valid password> |
| 9 | Complete any other required fields. | Entered data is accepted. | 20/04/2001 |
| 10 | Submit the registration form. | Account is successfully created and the user is logged in or redirected to the customer account page. |  |
## PSQA-5 — Registration with already registered email

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |  |
| 2 | Click Sign in. | Sign-in page is displayed. |  |
| 3 | Click Create an account. | Registration form is displayed. |  |
| 4 | Enter valid registration data. | Data is accepted. |  |
| 5 | Enter an email address already associated with an existing account. | Email address is accepted in the field. | qa.test@example.com |
| 6 | Complete the remaining required fields with valid data. | All entered data is accepted. |  |
| 7 | Submit the registration form. | Registration is rejected and an appropriate error message informs the user that the email address is already registered. |  |
## PSQA-6 — Registration with invalid email format

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |  |
| 2 | Navigate to the registration form. | Registration form is displayed. |  |
| 3 | Enter valid data into all required fields except email. | Entered data is accepted. | qa.test@example.com |
| 4 | Enter an invalid email format. | Invalid email is rejected or validation is triggered. | qa.test@example.com |
| 5 | Submit the registration form. | Account is not created and an appropriate validation message is displayed. |  |
## PSQA-7 — Registration with empty required fields

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |  |
| 2 | Navigate to the registration form. | Registration form is displayed. |  |
| 3 | Leave all required fields empty. | Required fields remain empty. |  |
| 4 | Click the registration/submit button. | Registration is not completed. |  |
| 5 | Review the form validation messages. | Appropriate validation messages are displayed for required fields. |  |
## PSQA-8 — Registration with password below minimum length

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |  |
| 2 | Navigate to the registration form. | Registration form is displayed. |  |
| 3 | Enter valid data into all required fields. | Entered data is accepted. |  |
| 4 | Enter a password containing 7 characters, which is one character below the minimum required length of 8. | Password is rejected or validation indicates that the password does not meet the requirements. | <valid password> |
| 5 | Submit the registration form. | Account is not created and an appropriate validation message is displayed. |  |
## PSQA-10 — Registration with special characters in name

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |  |
| 2 | Navigate to the registration form. | Registration form is displayed. |  |
| 3 | Enter a valid name containing a supported special character, e.g. hyphen or apostrophe. | Special characters that are not supported are rejected and an appropriate validation message is displayed. | First name: Sarah& |
| 4 | Complete the remaining required fields with valid data. | Entered data is accepted. |  |
| 5 | Submit the registration form. | Registration is completed successfully, or an appropriate validation message is displayed if the entered name is not supported. |  |
## PSQA-71 — Registration with leading/trailing spaces in input fields

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the registration form. | Registration form is displayed. |  |
| 2 | Enter valid registration data. | Data is accepted. |  |
| 3 | Add leading and trailing spaces to text fields such as first name and last name. | Input accepts the entered values or applies appropriate validation/normalization. | First name: " Sarah "
Last name: " Smith " |
| 4 | Enter a valid email address with leading/trailing spaces, if the field allows it. | System handles the spaces appropriately. | qa.test@example.com |
| 5 | Complete all required fields. | Form data is accepted. |  |
| 6 | Submit the registration form. | Registration is completed successfully or appropriate validation is displayed. |  |
| 7 | Open the customer account information. | Stored customer information is handled correctly without unexpected leading/trailing spaces. |  |
## PSQA-72 — Registration with maximum allowed field length

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the registration form. | Registration form is displayed. |  |
| 2 | Enter a value containing exactly the maximum allowed number(255) of characters in the selected field. | The entire value is accepted without validation errors or unexpected truncation. | [255 characters] |
| 3 | Enter valid data into the remaining required fields. | All entered data is accepted. |  |
| 4 | Submit the registration form. | Registration is completed successfully. |  |
| 5 | Open the customer account information. | The entered value is displayed correctly. |    |
## PSQA-73 — Registration with value below maximum field length

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the registration form. | Registration form is displayed. |  |
| 2 | Enter a value containing 254 characters. | The value is accepted without validation errors. | [254 characters] |
| 3 | Complete the remaining required fields with valid data. | Valid data is accepted. |  |
| 4 | Submit the registration form using the maximum valid value. | Registration is processed successfully if all entered data is valid. |  |
| 5 | Review the created customer information, if registration succeeds. | The stored value corresponds to the valid input. |  |
## PSQA-74 — Registration with value exceeding maximum field length

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the registration form. | Registration form is displayed. |  |
| 2 | Identify the maximum allowed length of the selected field. | Maximum allowed length is known. |  |
| 3 | Enter a value containing maximum allowed length + 1 character(256). | The system prevents entering the additional character or displays an appropriate validation message. | [256 characters] |
| 4 | Enter valid data into the remaining required fields. | Valid data is accepted. |  |
| 5 | Attempt to submit the registration form. | Registration is not completed if the field contains an invalid value. |  |
| 6 | Review the validation message or field value. | The field indicates that the maximum allowed length has been exceeded, or the extra character has been prevented from being entered. |  |
## PSQA-75 — Registration with one-character first and last name

**Priority:** Medium  
**Behavior:** Positive  
**Type:** nan  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Enter a first name consisting of exactly one character. | One-character first and last names are accepted. | First name: A |
| 2 | Enter a valid last name consisting of exactly one character.. | One-character first and last names are accepted. | Last name: B |
| 3 | Enter valid data into the remaining required fields. | All valid data is accepted. | Valid data |
| 4 | Submit the registration form. | Registration is completed successfully. |  |
## PSQA-76 — Registration with invalid date value

**Priority:** Medium  
**Behavior:** Negative  
**Type:** nan  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result | Data |
|---|---|---|---|
| 1 | Open the registration form. | Registration form is displayed. |  |
| 2 | Enter valid data into all required fields. | Valid data is accepted. |  |
| 3 | Enter a date using an invalid format. | The date is rejected or validation is triggered. | Date of birth: 31/02/2001 |
| 4 | Complete the remaining required fields. | Other valid data is accepted. |  |
| 5 | Submit the registration form. | Registration is not completed and an appropriate validation message is displayed. |  |
