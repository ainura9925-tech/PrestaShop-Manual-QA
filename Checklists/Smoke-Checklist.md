# Smoke Testing Checklist — PrestaShop Demo Store

## Homepage & Navigation

* [ ] Homepage loads successfully.
* [ ] Main navigation menu is displayed.
* [ ] Main navigation links open the corresponding pages.
* [ ] Product categories are accessible.
* [ ] Product pages can be opened.
* [ ] Shopping cart is accessible.

## Authentication

* [ ] Registration form opens successfully.
* [ ] User can register with valid data.
* [ ] Sign-in form opens successfully.
* [ ] User can log in with valid credentials.
* [ ] User can log out successfully.
* [ ] Customer account is accessible after successful login.

## Search & Catalog

* [ ] Search field is available.
* [ ] Search returns relevant products for a valid query.
* [ ] Product category pages load successfully.
* [ ] Product cards display basic product information.

## Product Page

* [ ] Product page loads successfully.
* [ ] Product name is displayed.
* [ ] Product price is displayed.
* [ ] Product availability/status is displayed.
* [ ] Product can be added to the cart.

## Shopping Cart

* [ ] Added product appears in the cart.
* [ ] Product quantity can be changed.
* [ ] Cart total is updated after quantity changes.
* [ ] Product can be removed from the cart.
* [ ] Cart total is updated after removing a product.

## Checkout

* [ ] User can proceed from the cart to checkout.
* [ ] Customer information can be entered or retrieved.
* [ ] Valid address can be entered.
* [ ] Available delivery method can be selected.
* [ ] Available payment method can be selected.
* [ ] Order summary is displayed.
* [ ] Order can be placed successfully.
* [ ] Order confirmation is displayed.


### Notes

* Smoke testing covers only critical customer-facing functionality.
* Failed smoke checks should be investigated before proceeding with full test execution.
* This checklist does not represent full functional, security, accessibility, or regression testing.
