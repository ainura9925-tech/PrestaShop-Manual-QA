# Functional & UI Testing Checklist

## 1. Homepage & Navigation

* [ ] Homepage loads successfully
* [ ] Main navigation is displayed
* [ ] Navigation links lead to correct pages
* [ ] Product categories can be opened
* [ ] Product pages can be opened
* [ ] Logo redirects to homepage
* [ ] Breadcrumb navigation works
* [ ] Browser Back/Forward navigation works
* [ ] Navigation does not lead to broken pages

## 2. Registration

* [ ] User can register with valid data
* [ ] Required fields are validated
* [ ] Invalid email format is rejected
* [ ] Password requirements are validated
* [ ] Minimum password length is enforced
* [ ] Maximum field length is handled correctly
* [ ] Values exceeding maximum length are handled correctly
* [ ] Special characters are handled correctly
* [ ] Leading/trailing spaces are handled correctly
* [ ] One-character names are handled correctly
* [ ] Invalid date values are rejected
* [ ] Appropriate validation messages are displayed

## 3. Login & Logout

* [ ] User can log in with valid credentials
* [ ] Incorrect password is rejected
* [ ] Unregistered email is rejected
* [ ] Empty email is validated
* [ ] Empty password is validated
* [ ] Invalid email format is validated
* [ ] User can log out
* [ ] Account cannot be accessed after logout
* [ ] Session is invalidated after logout

## 4. Password Reset

* [ ] Password reset works for a registered email
* [ ] Unregistered email is handled correctly
* [ ] Reset validation/error messages are displayed
* [ ] Password fields are masked where applicable

## 5. Search & Catalog

* [ ] Search returns an existing product
* [ ] Search handles a non-existing product
* [ ] Partial product names return relevant results
* [ ] Empty search is handled correctly
* [ ] Special characters are handled correctly
* [ ] Products can be opened from search results
* [ ] Categories display relevant products
* [ ] Product cards contain required information
* [ ] Product prices are displayed
* [ ] Product availability/status is displayed

## 6. Product Page

* [ ] Product page opens successfully
* [ ] Product name is displayed
* [ ] Product price is displayed
* [ ] Product image is displayed correctly
* [ ] Product description is displayed
* [ ] Product quantity can be changed
* [ ] Product can be added to cart
* [ ] Multiple units can be added
* [ ] Product variants can be selected

## 7. Shopping Cart

* [ ] Cart opens successfully
* [ ] Added product appears in cart
* [ ] Correct product price is displayed
* [ ] Product quantity can be increased
* [ ] Product quantity can be decreased
* [ ] Product can be removed
* [ ] Cart total is recalculated after quantity changes
* [ ] Cart total is recalculated after removing products
* [ ] Multiple different products can be added
* [ ] Cart persists while navigating between pages
* [ ] User can proceed from cart to checkout

## 8. Checkout

* [ ] Logged-in customer can access checkout
* [ ] Customer information can be entered
* [ ] Required fields are validated
* [ ] Invalid email is rejected
* [ ] Invalid/empty address is handled correctly
* [ ] Delivery method can be selected
* [ ] Payment method can be selected
* [ ] Order summary contains correct information
* [ ] Product quantity is correct
* [ ] Total order amount is calculated correctly
* [ ] Order can be placed with valid data
* [ ] Order confirmation is displayed
* [ ] Order appears in customer order history

## 9. Customer Account

* [ ] Customer account page opens
* [ ] Customer information is displayed correctly
* [ ] Customer information can be edited
* [ ] Password can be changed with valid data
* [ ] Incorrect current password is rejected
* [ ] New address can be added
* [ ] Existing address can be edited
* [ ] Address can be deleted
* [ ] Order history can be viewed
* [ ] Order details can be opened

## 10. Basic Security Checks

* [ ] Password is masked
* [ ] Password is not exposed in the URL
* [ ] Sensitive data is not present in the browser URL
* [ ] Unauthenticated user cannot access protected account pages
* [ ] Session is invalidated after logout
* [ ] Sensitive information is not exposed in Network requests
* [ ] HTTPS is used for authentication
* [ ] No obvious security-related browser console errors are present

## 11. UI & Usability

* [ ] Form validation messages are clear
* [ ] Required fields are visually identifiable
* [ ] Interactive elements are keyboard accessible
* [ ] Keyboard navigation works
* [ ] Layout remains usable at different screen sizes
* [ ] Buttons and links have understandable labels
* [ ] Important information is visually distinguishable
* [ ] UI elements are displayed consistently

## 12. Accessibility

* [ ] Form fields have accessible labels
* [ ] Interactive elements can be reached using keyboard
* [ ] Focus state is visible
* [ ] Required fields are identifiable
* [ ] Images have meaningful alt text where applicable
* [ ] Form validation messages are understandable
* [ ] Content remains usable without relying exclusively on a mouse

## 13. Compatibility

* [ ] Application works correctly in the primary browser
* [ ] Main functionality works at different viewport sizes
* [ ] Navigation remains usable on smaller screens
* [ ] Product pages remain usable on smaller screens
* [ ] Cart remains usable on smaller screens
* [ ] Checkout remains usable on smaller screens
