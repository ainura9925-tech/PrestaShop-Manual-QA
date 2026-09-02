# Checkout Test Data

Test data used for validating the checkout flow in the PrestaShop Demo Store.

The data is intended for manual functional, negative, boundary, and validation checks.

---

## 1. Customer Information

| Field | Valid Data | Invalid / Negative Data |
|---|---|---|
| First Name | Sarah | Empty value, special characters |
| Last Name | Smith | Empty value, special characters |
| Email | `test@example.com` | Empty value, invalid email format |
| Password | `Test@123456` | Empty value, invalid value |

---

## 2. Address Data

### Valid Address

| Field | Test Value |
|---|---|
| First Name | Sarah |
| Last Name | Smith |
| Address | 350 5th Avenue |
| City | New York |
| State | New York |
| Postal Code | 10018 |
| Country | United States |
| Phone | +441234567890 |

### Negative Address Data

| Scenario | Test Value |
|---|---|
| Empty address | Empty |
| Empty city | Empty |
| Empty postal code | Empty |
| Invalid postal code | `123` |
| Special characters | `@@@###` |
| Leading/trailing spaces | ` 10 Downing Street ` |
| Long input | Value exceeding the field's documented maximum length |

---

## 3. Email Test Data

### Valid

```text
test@example.com
customer@example.org
```

### Invalid

```text
test@
@example.com
test
test@@example.com
```

---

## 4. Postal Code Test Data

### Valid

```text
SW1A 2AA
```

### Invalid

```text
123
ABCDE
!!!
```

---

## 5. Phone Number Test Data

### Valid

```text
+441234567890
```

### Negative

```text
123
abcdefgh
!!!
```

---

## 6. Boundary and Validation Data

The following values can be used to verify field validation at or around documented input limits:

- Minimum allowed value
- Maximum allowed value
- One character below the minimum
- One character above the maximum
- Empty value
- Leading/trailing spaces
- Special characters
- Invalid format

Where a maximum field length is explicitly displayed by the application, the documented limit should be used as the boundary value.

---

## 7. Checkout State

The following checkout states are considered during testing:

- Product added to cart
- Cart contains at least one product
- Customer is logged in
- Customer is not logged in
- Address is completed
- Required address field is empty
- Delivery method is selected
- Payment method is selected
- Order confirmation is displayed

---

## 8. Test Data Notes

- Test data should not contain real personal or payment information.
- Placeholder email addresses are used for testing purposes.
- Payment details should be limited to data supported by the demo environment.
- Actual payment transactions are out of scope.
- When testing validation, the expected behavior should be based on the application's requirements or explicitly documented field constraints.