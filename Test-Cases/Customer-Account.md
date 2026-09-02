# Customer Account — Test Cases

## PSQA-77 — Customer account page opens

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
| 2 | Sign in using valid credentials. | User is successfully authenticated. |
| 3 | Open the customer account page. | Customer account page is displayed. |
| 4 | Review the account page. | Available customer account sections and options are displayed. |
## PSQA-78 — Customer information is displayed correctly

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the customer information section. | Customer information page is displayed. |
| 3 | Review the stored customer information. | First name, last name, email, and other available information are displayed correctly. |
## PSQA-79 — Edit customer information

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the customer information section. | Customer information is displayed. |
| 3 | Edit one or more editable customer information fields. | New values are entered successfully. |
| 4 | Save the changes. | Customer information is updated successfully. |
| 5 | Review the updated information. | Updated values are displayed correctly. |
## PSQA-80 — Change password with valid data

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the customer information or password change section. | Password change option is displayed. |
| 3 | Enter the current password. | Current password is accepted. |
| 4 | Enter a valid new password. | New password is accepted. |
| 5 | Confirm the password change, if applicable. | Password confirmation is accepted. |
| 6 | Save the changes. | Password is changed successfully. |
## PSQA-81 — Change password with incorrect current password

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the password change section. | Password change option is displayed. |
| 3 | Enter an incorrect current password. | Incorrect password is entered. |
| 4 | Enter a valid new password. | New password is accepted. |
| 5 | Submit the password change. | Password is not changed and an appropriate validation message is displayed. |
## PSQA-82 — Add new address

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the Addresses section. | Saved addresses are displayed. |
| 3 | Select the option to add a new address. | New address form is displayed. |
| 4 | Enter valid address information. | Address data is accepted. |
| 5 | Save the address. | New address is saved successfully. |
| 6 | Review the address list. | The newly added address is displayed. |
## PSQA-83 — Edit existing address

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the Addresses section. | Saved addresses are displayed. |
| 3 | Select an existing address to edit. | Address form is displayed with the existing information. |
| 4 | Modify one or more address fields. | Updated values are entered successfully. |
| 5 | Save the changes. | Address is updated successfully. |
| 6 | Review the address list. | Updated address information is displayed correctly. |
## PSQA-84 — Delete address

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the Addresses section. | Saved addresses are displayed. |
| 3 | Select an existing address to delete. | Delete option is available. |
| 4 | Delete the selected address. | Address is removed successfully. |
| 5 | Review the address list. | Deleted address is no longer displayed. |
## PSQA-85 — View order history

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the order history section. | Order history page is displayed. |
| 3 | Review the order list. | Previous orders are displayed with relevant order information. |
## PSQA-86 — Open order details

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the customer account page. | Customer account page is displayed. |
| 2 | Open the order history section. | Order history is displayed. |
| 3 | Select an existing order. | Order details page is displayed. |
| 4 | Review the order information. | Order number, date, products, quantities, prices, and order total are displayed correctly. |
