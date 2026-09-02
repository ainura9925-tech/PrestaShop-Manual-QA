# Product Page — Test Cases

## PSQA-38 — Product page opens successfully

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
| 1 | Open a product from the catalog. | Product details page is displayed. |
| 2 | Review the page. | Page loads without critical errors. |
| 3 | Review the URL. | URL corresponds to the selected product. |
## PSQA-39 — Product name is displayed

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
| 2 | Navigate to the product catalog. | Product listing is displayed. |
| 3 | Select a product. | Product page is displayed. |
| 4 | Review the product information. | The product name is displayed correctly. |
## PSQA-40 — Product price is displayed

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
| 2 | Navigate to the product catalog. | Product listing is displayed. |
| 3 | Select a product. | Product page is displayed. |
| 4 | Review the product information. | The product price is displayed correctly. |
## PSQA-41 — Product image is displayed correctly

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
| 1 | Open a product page. | Product page is displayed. |
| 2 | Review the main product image. | Product image loads correctly without broken-image indicators. |
| 3 | If additional images are available, select one. | Selected product image is displayed correctly. |
## PSQA-42 — Product description is displayed

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is available for purchase.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a product page. | Product page is displayed. |
| 2 | Locate the quantity control. | Quantity control is displayed. |
| 3 | Increase the quantity by one. | Quantity increases correctly. |
| 4 | Decrease the quantity by one. | Quantity decreases correctly. |
| 5 | Review the selected quantity. | Displayed quantity corresponds to the user's actions. |
## PSQA-43 — Change product quantity

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Product is available for purchase.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a product page. | Product page is displayed. |
| 2 | Locate the quantity control. | Quantity control is displayed. |
| 3 | Increase the quantity by one. | Quantity increases correctly. |
| 4 | Decrease the quantity by one. | Quantity decreases correctly. |
| 5 | Review the selected quantity. | Displayed quantity corresponds to the user's actions. |
## PSQA-44 — Add product to cart

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
| 1 | Open a product page. | Product page is displayed. |
| 2 | Select a valid quantity. | Selected quantity is displayed. |
| 3 | Click Add to cart. | Product is added to the shopping cart. |
| 4 | Review the cart confirmation/update. | Cart reflects the added product and quantity. |
## PSQA-45 — Add multiple units of a product to cart

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
| 1 | Open a product page. | Product page is displayed. |
| 2 | Set quantity to more than one. | Selected quantity is displayed. |
| 3 | Click Add to cart. | Product is added to cart with the selected quantity. |
| 4 | Open the shopping cart. | Cart displays the correct product quantity. |
## PSQA-46 — Product variant selection works

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
| 1 | Open a product with available variants. | Product page is displayed. |
| 2 | Select an available variant. | Selected variant is displayed. |
| 3 | Review the product information. | Price/availability or other relevant information updates according to the selected variant. |
| 4 | Add the product to cart. | Selected variant is added to the cart. |
