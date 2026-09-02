# Homepage & Navigation — Test Cases

## PSQA-20 — Homepage loads successfully

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is not authenticated.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store URL. | Homepage loads successfully. |
| 2 | Wait until the page is fully loaded. | No critical loading errors are displayed. |
| 3 | Review the main page content. | Main homepage elements are displayed correctly. |
## PSQA-21 — Main navigation menu is displayed

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
| 1 | Open the homepage. | Homepage is displayed. |
| 2 | Locate the main navigation menu. | Navigation menu is visible. |
| 3 | Review the available navigation categories. | Categories are displayed with readable names and without visual overlap. |
## PSQA-22 — Navigation to product category works

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
| 1 | Locate a product category in the navigation menu. | Category link is visible. |
| 2 | Click the category. | User is redirected to the corresponding category page. |
| 3 | Review the opened page. | Correct category name and relevant products are displayed. |
## PSQA-23 — Navigation to product page works

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

A product is available on the homepage or category page.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the homepage. | Homepage is displayed. |
| 2 | Select a product. | Product link/card is clickable. |
| 3 | Click the product. | Product details page is opened. |
| 4 | Review the product page. | Correct product information is displayed. |
## PSQA-24 — Logo redirects to homepage

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User is on a page other than the homepage.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open any product or category page. | Selected page is displayed. |
| 2 | Click the PrestaShop store logo. | User is redirected to the homepage. |
| 3 | Review the URL and page content. | Homepage is displayed and the correct homepage URL is loaded. |
## PSQA-25 — Breadcrumb navigation works

**Priority:** High  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

A product page or nested category page is opened.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a product page from a category. | Product page is displayed. |
| 2 | Locate the breadcrumb navigation. | Breadcrumb displays the current navigation hierarchy. |
| 3 | Click the relevant parent category in the breadcrumb. | User is redirected to the selected parent category. |
| 4 | Review the page. | Correct category page is displayed. |
## PSQA-26 — Links lead to correct pages

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
| 1 | Open the homepage. | Homepage is displayed. |
| 2 | Select an available navigation link. | Link is clickable. |
| 3 | Click the link. | User is redirected to the corresponding page. |
| 4 | Compare the opened page with the selected link. | Opened page corresponds to the selected navigation item. |
## PSQA-27 — Browser Back/Forward navigation works

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Functional  
**Layer:** UI  
**Automation:** Manual

### Preconditions

User can navigate between at least two pages.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the homepage. | Homepage is displayed. |
| 2 | Navigate to a category page. | Category page is displayed. |
| 3 | Click the browser Back button. | Previous homepage is displayed. |
| 4 | Click the browser Forward button. | Category page is displayed again. |
| 5 | Review the page state. | Page loads correctly without unexpected errors or broken content. |
## PSQA-107 — Navigation links do not lead to broken pages

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
| 1 | Open the PrestaShop Demo Store. | Homepage is displayed successfully. |
| 2 | Review the main navigation menu and available navigation links. | Links are displayed and accessible. |
| 3 | Open each available main navigation link one by one. | Each link opens a corresponding page without errors. |
| 4 | Review the URL and page content after opening each link. | URL is valid and the opened page corresponds to the selected link. |
| 5 | Check whether any page displays a 404, 500, blank page or other unexpected error. | No broken pages or unexpected server errors are displayed. |
