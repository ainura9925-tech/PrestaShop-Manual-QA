# Checkout — Test Cases

## PSQA-57 — Proceed from cart to checkout

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is added to the shopping cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the shopping cart. | Shopping cart page is displayed. |
| 2 | Review the cart contents. | Added product, quantity, price, and cart total are displayed. |
| 3 | Click the checkout button. | Checkout process is opened. |
| 4 | Review the checkout page. | Checkout steps and required customer/order information are displayed. |
## PSQA-58 — Checkout as logged-in customer

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
| 1 | Open the shopping cart. | Cart page is displayed. |
| 2 | Click the checkout button. | Checkout process is opened. |
| 3 | Review the customer information. | Logged-in customer's information is available or pre-filled where applicable. |
| 4 | Continue through the checkout process. | User can proceed without being required to create another account or re-enter unnecessary authentication information. |
## PSQA-59 — Checkout with valid customer information

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is in the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Proceed from the cart to checkout. | Checkout page is displayed. |
| 2 | Enter valid customer information. | Entered information is accepted. |
| 3 | Enter valid billing/shipping address information. | Address information is accepted. |
| 4 | Continue to the next checkout step. | User proceeds to the next checkout step successfully. |
| 5 | Review the entered information. | Customer and address information is displayed correctly. |
## PSQA-60 — Required checkout fields validation

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is on the checkout page.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Leave one or more required checkout fields empty. | Required fields remain empty. |
| 2 | Attempt to continue to the next checkout step. | Checkout cannot proceed while required information is missing. |
| 3 | Review the form. | Appropriate validation messages are displayed for the required fields. |
| 4 | Enter valid values into the required fields. | Validation messages are cleared and the entered values are accepted. |
## PSQA-61 — Invalid email during checkout

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is on a checkout step containing an email field.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Enter an invalid email format. | Invalid email value is entered. |
| 2 | Complete the remaining required fields with valid data. | Valid data is accepted. |
| 3 | Attempt to continue. | Checkout cannot proceed with an invalid email address. |
| 4 | Review the email field. | Appropriate email validation message is displayed. |
## PSQA-62 — Invalid/empty address data

**Priority:** High  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is on the address step of checkout.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Leave required address fields empty or enter invalid address data. | Entered data is accepted only where valid. |
| 2 | Attempt to continue. | Checkout does not proceed with invalid or missing required address information. |
| 3 | Review the address form. | Appropriate validation messages are displayed. |
| 4 | Enter valid address information. | Address data is accepted and checkout can proceed. |
## PSQA-63 — Select available delivery method

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is in the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Proceed to the delivery step. | Available delivery methods are displayed. |
| 2 | Review the available delivery methods. | Available delivery options and their prices/details are displayed. |
| 3 | Select an available delivery method. | Selected delivery method is highlighted or marked as selected. |
| 4 | Continue to the next checkout step. | Selected delivery method is applied to the order. |
## PSQA-64 — Select available payment method

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is in the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Proceed to the payment step. | Available payment methods are displayed. |
| 2 | Review the available payment methods. | Available payment options are displayed. |
| 3 | Select an available payment method. | Selected payment method is marked as selected. |
| 4 | Review the order summary. | Selected payment method is reflected in the checkout summary. |
## PSQA-65 — Order summary contains correct information

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is in the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Proceed to the order summary. | Order summary is displayed. |
| 2 | Review the products in the order. | Correct products are displayed. |
| 3 | Review product quantities. | Quantities correspond to the cart. |
| 4 | Review product prices. | Product prices correspond to the cart. |
| 5 | Review delivery information. | Selected delivery method and associated cost are displayed correctly. |
| 6 | Review the total amount. | Order total is calculated from the displayed order information. |
## PSQA-66 — Product quantity in order is correct

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is added to the cart with a known quantity.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the shopping cart. | Cart page is displayed. |
| 2 | Set the product quantity to a known value. | Selected quantity is displayed in the cart. |
| 3 | Proceed to checkout. | Checkout page is displayed. |
| 4 | Review the order summary. | Product quantity matches the quantity selected in the cart. |
## PSQA-67 — Total order amount is calculated correctly

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is in the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Add a product to the cart. | Product is added successfully. |
| 2 | Set the desired quantity. | Product quantity is updated. |
| 3 | Proceed to checkout. | Checkout page is displayed. |
| 4 | Select an available delivery method. | Delivery method and cost are applied. |
| 5 | Review the order summary. | Product subtotal, delivery cost, and total order amount are displayed correctly. |
| 6 | Compare the total with the expected calculation. | Displayed total corresponds to the product subtotal plus applicable delivery costs and other charges. |
## PSQA-68 — Place order with valid data

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is in the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Proceed to the final checkout step. | Order summary and payment information are displayed. |
| 2 | Review all order information. | Order information is correct. |
| 3 | Accept any required terms and conditions, if applicable. | Required agreement is selected. |
| 4 | Click the button to place/confirm the order. | Order is submitted successfully. |
| 5 | Wait for the order confirmation page. | Order confirmation is displayed. |
## PSQA-69 — Order confirmation is displayed

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Order has been successfully placed.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Complete the checkout process with valid data. | Order is successfully submitted. |
| 2 | Review the resulting page. | Order confirmation page is displayed. |
| 3 | Review the confirmation information. | Confirmation message and order details are displayed. |
| 4 | Verify the order reference, if provided. | Order reference is displayed and can be identified by the customer. |
## PSQA-70 — Order appears in customer order history

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
| 1 | Complete a successful checkout. | Order is successfully placed. |
| 2 | Open the customer account page. | Customer account page is displayed. |
| 3 | Open the order history section. | Order history is displayed. |
| 4 | Find the recently placed order. | Newly created order appears in the order history. |
| 5 | Compare the order with the completed checkout. | Order number, products, quantity, date, and total correspond to the completed order. |
