# ATF File Format

## Overview

ATF (Agentic Test Format) is a simple, readable file format for defining test scenarios. It allows you to organize multiple test cases in a structured way with configuration and metadata.

## File Extension

`.atf`

## Basic Structure

```
# Test Suite Name

Description: Optional description of the test suite

@config browser=chromium
@config headless=false

## Scenario: Test name
@tag smoke
@tag login

Test steps in natural language...
Go to example.com
Click button
Verify something
Take screenshot

## Scenario: Another test
@tag regression

More test steps...
```

## Syntax

### Test Suite Header

```
# Test Suite Name
```

- Must start with single `#`
- Should be on the first non-empty line
- Only the first `#` header is used as the suite name

### Description

```
Description: This is what the test suite does
```

- Optional
- Should appear after the suite name
- Only the first description is used

### Configuration

```
@config key=value
```

- Set default configuration for all scenarios in the file
- Can be overridden by CLI arguments
- Common configs:
  - `browser`: chromium, firefox, webkit
  - `headless`: true, false

### Scenario Definition

```
## Scenario: Scenario Name
```

or

```
## Test: Test Name
```

- Starts with `##` followed by `Scenario:` or `Test:`
- Each scenario contains natural language test steps

### Tags

```
@tag tagname
```

- Add tags before a scenario
- Use for filtering tests (e.g., `@tag smoke`, `@tag login`)
- Can have multiple tags per scenario
- Run specific tags with `--tag` CLI flag

### Test Steps

Natural language instructions after the scenario header:

```
Go to example.com
Type 'username' into email field
Click login button
Verify page contains 'Welcome'
Take a screenshot
```

## Complete Example

```atf
# E-Commerce Checkout Flow

Description: Test the complete checkout process from cart to payment

@config browser=chromium
@config headless=false

## Scenario: Guest Checkout
@tag smoke
@tag checkout
@tag guest

Go to shop.example.com
Click 'Add to Cart' button
Click cart icon
Click 'Checkout as Guest'
Type 'test@example.com' into email field
Type '123 Main St' into address field
Click 'Continue to Payment'
Verify page contains 'Payment Information'
Take a screenshot named 'payment_page'

## Scenario: Registered User Checkout
@tag checkout
@tag registered

Go to shop.example.com/login
Type 'user@example.com' into email field
Type 'password123' into password field
Click 'Login' button
Click 'Add to Cart' button
Click cart icon
Click 'Checkout'
Verify address is pre-filled
Click 'Continue to Payment'
Take a screenshot

## Scenario: Empty Cart
@tag checkout
@tag edge-case

Go to shop.example.com
Click cart icon
Verify page contains 'Your cart is empty'
```

## Creating ATF Files

### Quick Start with Templates

```bash
# Create a basic template
agentic-test --create tests/my_test.atf

# Create from specific template
agentic-test --create tests/login.atf --template login
agentic-test --create tests/shop.atf --template ecommerce
agentic-test --create tests/api.atf --template api

# Overwrite existing file
agentic-test --create tests/test.atf --overwrite
```

**Available Templates:**
- `basic` - Simple test structure with example scenarios
- `login` - Login and authentication flow tests
- `ecommerce` - Shopping, cart, and checkout tests
- `api` - API and integration testing flows

Each template includes:
- Pre-configured settings (@config)
- Tagged scenarios (@tag)
- Placeholder URLs and values to customize
- Common test patterns for the use case

## Usage

### Run entire ATF file

```bash
agentic-test tests/checkout.atf
```

### Run specific scenario

```bash
agentic-test tests/checkout.atf --scenario "Guest Checkout"
```

### Run scenarios by tag

```bash
agentic-test tests/checkout.atf --tag smoke
```

### Override configuration

```bash
# Run in headless mode even if ATF says headless=false
agentic-test tests/checkout.atf --headless

# Use different browser
agentic-test tests/checkout.atf --browser firefox
```

## Best Practices

### Organization

- **One file per feature**: Create separate ATF files for login, search, checkout, etc.
- **Meaningful names**: Use descriptive scenario names
- **Tag strategically**: Use tags like `smoke`, `regression`, `critical` for test organization

### Test Steps

- **Be specific**: "Click login button" is better than "Click button"
- **One action per line**: Each line should be a single, clear instruction
- **Add context**: Use descriptive names for screenshots and data extraction

### Tags

Common tag conventions:
- `@tag smoke` - Critical tests that should always pass
- `@tag regression` - Full regression suite
- `@tag login` - Feature-specific tests
- `@tag edge-case` - Boundary/edge case tests
- `@tag negative` - Negative test cases
- `@tag slow` - Tests that take longer to run

### Configuration

- Set `headless=true` for CI/CD environments
- Set `headless=false` for local development and debugging
- Use `browser=chromium` for best compatibility

## Validation

The ATF parser validates:
- ✅ At least one scenario exists
- ✅ Each scenario has test steps
- ⚠️ Warns about empty scenarios

## Comments

ATF format doesn't support comments yet. Use the Description field for documentation.

## Future Enhancements

Planned features:
- Variables and data-driven tests
- Conditional execution
- Test dependencies
- Setup/teardown blocks
- Comments support
- Import/include other ATF files
