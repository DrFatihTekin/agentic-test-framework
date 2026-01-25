# Example Test Scenarios

This directory contains example test scenarios that demonstrate the framework's capabilities.

## Running Examples

### Command Line
```bash
# Run a test from a file
python -m agentic_test_framework examples/google_search.txt

# Run a test directly
python -m agentic_test_framework "Go to example.com and take a screenshot"

# Run with different browsers
python -m agentic_test_framework examples/github_search.txt --browser firefox
python -m agentic_test_framework examples/google_search.txt --browser webkit

# Run in headless mode
python -m agentic_test_framework examples/google_search.txt --headless
```

### Programmatically
```bash
# Run multiple examples
python examples/run_examples.py

# Use components directly
python examples/direct_usage.py
```

## Example Test Files

- `google_search.txt` - Simple search test
- `github_search.txt` - Multi-step search workflow
- `run_examples.py` - Programmatic test execution
- `direct_usage.py` - Using framework components directly

## Creating Your Own Tests

Create a text file with natural language instructions:

```text
Go to mywebsite.com
Click the "Sign In" button
Type "testuser@example.com" into the email field
Type "password123" into the password field
Click the "Login" button
Wait 3 seconds
Take a screenshot named "logged_in"
```

Then run it:
```bash
python -m agentic_test_framework my_test.txt
```
