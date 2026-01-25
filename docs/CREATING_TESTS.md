# Creating ATF Test Files

## Quick Reference

### Create New ATF File

```bash
# Basic template
agentic-test --create tests/my_test.atf

# Login template
agentic-test --create tests/login.atf --template login

# E-commerce template
agentic-test --create tests/shop.atf --template ecommerce

# API testing template
agentic-test --create tests/api.atf --template api

# Overwrite existing file
agentic-test --create tests/test.atf --overwrite
```

## Available Templates

### 1. Basic Template (`--template basic`)

**Best for:** Simple test scenarios, getting started

**Includes:**
- Basic test structure
- Example navigation and assertion
- Single screenshot action
- Placeholder for additional tests

**Example usage:**
```bash
agentic-test --create tests/simple.atf
```

### 2. Login Template (`--template login`)

**Best for:** Authentication flows, user login/logout tests

**Includes:**
- Successful login scenario
- Invalid credentials test
- Empty form validation
- Tagged with `@tag login`, `@tag negative`, `@tag validation`

**Placeholders to customize:**
- `YOUR_APP_URL` - Replace with your application URL
- `YOUR_USERNAME` - Replace with test username
- `YOUR_PASSWORD` - Replace with test password

**Example usage:**
```bash
agentic-test --create tests/auth.atf --template login
# Edit file to replace YOUR_APP_URL with actual URL
# Run: agentic-test tests/auth.atf --tag smoke
```

### 3. E-commerce Template (`--template ecommerce`)

**Best for:** Shopping carts, product search, checkout flows

**Includes:**
- Product search scenario
- Add to cart workflow
- Checkout flow with payment
- Tagged with `@tag smoke`, `@tag cart`, `@tag checkout`, `@tag critical`

**Placeholders to customize:**
- `YOUR_SHOP_URL` - Replace with your shop URL
- Product names and search terms

**Example usage:**
```bash
agentic-test --create tests/shopping.atf --template ecommerce
```

### 4. API Template (`--template api`)

**Best for:** Integration tests, user registration, profile updates

**Includes:**
- User registration flow
- Profile update scenario
- Form submissions
- URL verification
- Tagged with `@tag smoke`, `@tag registration`, `@tag profile`

**Placeholders to customize:**
- `YOUR_APP_URL` - Replace with your application URL
- Email addresses and credentials

**Example usage:**
```bash
agentic-test --create tests/integration.atf --template api
```

## Workflow

### 1. Create Template
```bash
agentic-test --create tests/login.atf --template login
```

### 2. Edit File
Open `tests/login.atf` and customize:
- Replace placeholder URLs (`YOUR_APP_URL`)
- Update test data (usernames, passwords)
- Add/remove scenarios
- Modify tags

### 3. Run Tests
```bash
# Run all scenarios
agentic-test tests/login.atf

# Run specific scenario
agentic-test tests/login.atf --scenario "Successful Login"

# Run by tag
agentic-test tests/login.atf --tag smoke

# Run in headless mode
agentic-test tests/login.atf --headless
```

## Common Patterns

### Organizing Tests

```
tests/
├── smoke/
│   ├── critical.atf          # Basic template
│   └── login.atf              # Login template
├── regression/
│   ├── checkout.atf           # E-commerce template
│   └── profile.atf            # API template
└── integration/
    └── api.atf                # API template
```

### Running Organized Tests

```bash
# All smoke tests
for f in tests/smoke/*.atf; do agentic-test $f --tag smoke; done

# All regression tests
for f in tests/regression/*.atf; do agentic-test $f; done
```

## Tips

1. **Start with templates** - Faster than writing from scratch
2. **Replace placeholders** - Always customize YOUR_APP_URL and test data
3. **Use meaningful names** - Name files by feature (login.atf, checkout.atf)
4. **Tag strategically** - Use `@tag smoke` for critical tests
5. **Version control** - Commit ATF files to git
6. **Don't overwrite accidentally** - Files are protected unless you use `--overwrite`

## Examples

### Create and run login test
```bash
agentic-test --create tests/login.atf --template login
# Edit tests/login.atf (replace YOUR_APP_URL)
agentic-test tests/login.atf --tag smoke
```

### Create suite for new feature
```bash
agentic-test --create tests/new_feature.atf
# Edit and add scenarios
agentic-test tests/new_feature.atf
```

### Replace existing test
```bash
agentic-test --create tests/old_test.atf --template ecommerce --overwrite
```
