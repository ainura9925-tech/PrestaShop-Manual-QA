# Usability / UI — Test Cases

## PSQA-97 — Form validation messages are clear

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Usability  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a form containing required fields. | Form is displayed. |
| 2 | Leave one or more required fields empty or enter invalid data. | Invalid input is present. |
| 3 | Submit or continue the form. | Validation messages are displayed. |
| 4 | Review the validation messages. | Messages clearly indicate which field requires correction and what is expected. |
| 5 | Correct the invalid data. | Validation messages disappear or are updated appropriately. |
## PSQA-98 — Keyboard navigation

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Usability  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the registration or checkout form. | Form is displayed. |
| 2 | Use the Tab key to move through interactive elements. | Focus moves through interactive elements in a logical order. |
| 3 | Use Shift + Tab to move backwards. | Focus moves to the previous interactive element. |
| 4 | Use the keyboard to interact with available controls. | Controls can be operated without requiring a mouse where applicable. |
## PSQA-99 — Required fields are visually identifiable

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Usability  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a form containing required and optional fields. | Form is displayed. |
| 2 | Review the field labels and indicators. | Required fields are visually distinguishable from optional fields. |
| 3 | Compare required and optional fields. | The visual indication is consistent throughout the form. |
## PSQA-100 — Layout at different screen sizes

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Usability  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open the PrestaShop Demo Store in a desktop browser window. | Page layout is displayed correctly. |
| 2 | Resize the browser window to a smaller width. | Layout adapts to the available screen width. |
| 3 | Review navigation, product content, forms, and buttons. | Elements remain visible and usable without unexpected overlap or horizontal scrolling where not intended. |
| 4 | Resize the window to a mobile-sized width. | Mobile layout is displayed correctly. |
