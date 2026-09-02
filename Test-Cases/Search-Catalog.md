# Search & Catalog — Test Cases

## PSQA-28 — Search with existing product

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Homepage is opened.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Locate the search field. | Search field is displayed. |
| 2 | Enter the name of an existing product. | Product name is accepted. |
| 3 | Submit the search. | Search results page is displayed. |
| 4 | Review the results. | Relevant product is displayed in the search results. |
## PSQA-29 — Search with non-existing product

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Homepage is opened.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Locate the search field. | Search field is displayed. |
| 2 | Enter a product name that does not exist. | Search query is accepted. |
| 3 | Submit the search. | Search results page is displayed. |
| 4 | Review the results. | No irrelevant products are displayed and an appropriate "no results" message is shown. |
## PSQA-30 — Search with partial product name

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

A product with a known name exists.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Enter part of an existing product name in the search field. | Search query is accepted. |
| 2 | Submit the search. | Search results are displayed. |
| 3 | Review the results. | Products relevant to the partial search query are displayed. |
## PSQA-31 — Search with empty input

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the homepage. | Homepage is displayed. |
| 2 | Leave the search field empty. | Search field remains empty. |
| 3 | Submit the search. | System handles the empty query appropriately without displaying an unexpected error. |
## PSQA-32 — Search with special characters

**Priority:** Medium  
**Behavior:** Negative  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Enter special characters into the search field. | Characters are accepted or handled by the input validation. |
| 2 | Submit the search. | Search request is processed without a system error. |
| 3 | Review the results. | Page remains functional and displays appropriate results/message. |
## PSQA-33 — Open product from search results

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

Search results contain at least one product.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Perform a search for an existing product. | Relevant search results are displayed. |
| 2 | Click a product in the results. | Product page is opened. |
| 3 | Compare the selected product with the product page. | Correct product page is displayed. |
## PSQA-34 — Product category displays relevant products

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

At least one product category is available.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a product category. | Category page is displayed. |
| 2 | Review the category title. | Correct category name is displayed. |
| 3 | Review the products. | Products belonging to the selected category are displayed. |
## PSQA-35 — Product card displays required information

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
| 1 | Open a category containing products. | Product listing is displayed. |
| 2 | Select a product card. | Product card is displayed. |
| 3 | Review the product card. | Product name, image and price are displayed correctly. |
| 4 | Review the product card actions. | Available actions, such as opening the product or adding it to cart, work correctly. |
## PSQA-36 — Product price is displayed correctly

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
| 3 | Open a product or review a product in the listing. | Product price is displayed. |
| 4 | Compare the displayed price between the product listing and product page. | The displayed price is consistent. |
## PSQA-37 — Product availability/status is displayed

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
| 3 | Open a product. | Product page is displayed. |
| 4 | Review the product availability/status. | Product availability or stock status is displayed correctly. |
