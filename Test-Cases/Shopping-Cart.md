# Shopping Cart — Test Cases

## PSQA-47 — Cart opens successfully

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop store. | Homepage is displayed. |
| 2 | Open the shopping cart. | Shopping cart page is displayed. |
| 3 | Review the page. | Cart content and total are displayed correctly. |
## PSQA-48 — Added product appears in cart

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product has been added to the cart.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Add a product to the cart. | Product is added successfully. |
| 2 | Open the cart. | Cart page is displayed. |
| 3 | Review the cart contents. | Added product is displayed with the correct name, price and quantity. |
## PSQA-49 — Correct product price is displayed

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Add a product to the cart. | Product is added. |
| 2 | Open the cart. | Cart is displayed. |
| 3 | Compare the product price with the product page. | Cart displays the correct product price. |
## PSQA-50 — Increase product quantity

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Add a product to the cart. | Product is displayed in cart. |
| 2 | Increase the product quantity. | Quantity is increased. |
| 3 | Review the product subtotal. | Subtotal is recalculated according to the new quantity. |
| 4 | Review the cart total. | Cart total is recalculated correctly. |
## PSQA-51 — Decrease product quantity

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the cart containing a product. | Product is displayed. |
| 2 | Decrease the product quantity. | Quantity is decreased. |
| 3 | Review the subtotal. | Subtotal is updated correctly. |
| 4 | Review the total. | Cart total is updated correctly. |
## PSQA-52 — Remove product from cart

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the cart containing a product. | Product is displayed. |
| 2 | Click the remove/delete option. | Product is removed from the cart. |
| 3 | Review the cart. | Removed product is no longer displayed. |
| 4 | Review the cart total. | Total is recalculated correctly. |
## PSQA-53 — Cart total is recalculated after quantity change

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Open a product page. | Product page is displayed. |
| 3 | Add the product to the cart. | Product is added to the cart. |
| 4 | Open the shopping cart. | Shopping cart displays the added product and current total. |
| 5 | Increase the product quantity. | Product quantity is updated. |
| 6 | Review the cart total. | Cart total is recalculated according to the updated quantity. |
## PSQA-54 — Cart total is recalculated after removing product

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed. |
| 2 | Add a product to the cart. | Product is added to the cart. |
| 3 | Open the shopping cart. | Shopping cart displays the added product and current total. |
| 4 | Remove the product from the cart. | Product is removed from the cart. |
| 5 | Review the cart total. | Cart total is recalculated correctly after the product is removed. |
## PSQA-55 — Add multiple different products

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Add the first product to the cart. | First product is added. |
| 2 | Return to the catalog. | Catalog is displayed. |
| 3 | Add a different product to the cart. | Second product is added. |
| 4 | Open the cart. | Both products are displayed with correct quantities and prices. |
## PSQA-56 — Cart persists after navigating to another page

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Add a product to the cart. | Product is added. |
| 2 | Navigate to another page. | Selected page is displayed. |
| 3 | Open the cart again. | Cart is displayed. |
| 4 | Review the contents. | Previously added product remains in the cart with the correct quantity. |
