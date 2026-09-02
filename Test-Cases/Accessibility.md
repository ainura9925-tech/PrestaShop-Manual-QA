# Accessibility — Test Cases

## PSQA-104 — Form fields have accessible labels

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Other  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a page containing a form. | Form is displayed. |
| 2 | Open browser DevTools and inspect the form fields. | Form fields can be inspected. |
| 3 | Inspect the labels and associated input elements. | Each form field has a meaningful accessible label. |
| 4 | Check required fields. | Required fields have an appropriate accessible indication where applicable. |
## PSQA-105 — Interactive elements are keyboard accessible

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Other  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a page containing interactive elements. | Page is displayed. |
| 2 | Use the Tab key to navigate through links, buttons, and form controls. | Interactive elements receive keyboard focus. |
| 3 | Observe the focused element. | Current keyboard focus is visually identifiable. |
| 4 | Use Enter or Space where applicable. | Focused interactive elements can be activated using the keyboard. |
## PSQA-106 — Images have meaningful alt text where applicable

**Priority:** Medium  
**Behavior:** Positive  
**Type:** Other  
**Layer:** UI  
**Automation:** Manual

### Preconditions

None specified.

### Test Steps

| # | Action | Expected Result |
|---|---|---|
| 1 | Open a page containing product or content images. | Page is displayed. |
| 2 | Open browser DevTools and inspect relevant images. | Image elements can be inspected. |
| 3 | Review the alt attribute of informative images. | Informative images have meaningful alternative text. |
| 4 | Review decorative images. | Decorative images do not contain unnecessary alternative text where appropriate. |
