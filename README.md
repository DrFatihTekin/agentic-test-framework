# Agentic Test Framework

An AI-powered browser testing framework that accepts natural language test descriptions and executes them using Playwright.

## Quick Start

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Set up environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# Run an example test
python -m agentic_test_framework "Go to example.com and take a screenshot"

# Or run from an ATF file
agentic-test examples/login.atf
```

## Features

- 🤖 **Natural Language Tests**: Write tests in plain English
- 🌐 **Browser Automation**: Powered by Playwright (Chrome, Firefox, Safari)
- 🧠 **AI-Driven**: Uses OpenAI to interpret test scenarios
- 📸 **Auto Screenshots**: Captures screenshots on demand or failure
- � **HTML Reports**: Beautiful test reports with embedded screenshots (like RobotFramework)
- ✅ **Assertions**: Verify conditions and extract data
- �🔄 **Smart Retries**: Handles flaky elements automatically

## Example Tests

### Command Line
```bash
# Simple navigation
agentic-test "Go to google.com and search for 'playwright testing'"

# Multi-step workflow
agentic-test "Navigate to github.com, click Sign in, type 'testuser' in username field"

# Validation
agentic-test "Go to example.com, verify the page title contains 'Example', take screenshot"
```

### ATF File Format

Create structured test files with `.atf` extension:

```atf
# Login Test Suite

@config browser=chromium
@config headless=false

## Scenario: Successful Login
@tag smoke
@tag login

Go to example.com/login
Type 'testuser' into username field
Type 'password123' into password field
Click login button
Verify page contains 'Welcome'
Take a screenshot
```

**Quick Start: Generate ATF Templates**

```bash
# Create basic template
agentic-test --create tests/my_test.atf

# Create from predefined templates
agentic-test --create tests/login.atf --template login
agentic-test --create tests/shop.atf --template ecommerce
agentic-test --create tests/api.atf --template api
```

Available templates:
- **basic** - Simple test structure
- **login** - Login/authentication flows
- **ecommerce** - Shopping and checkout flows
- **api** - API/integration tests

Run ATF files:
```bash
# Run all scenarios
agentic-test tests/login.atf

# Run specific scenario
agentic-test tests/login.atf --scenario "Successful Login"

# Run by tag
agentic-test tests/login.atf --tag smoke
```

See [docs/ATF_FORMAT.md](docs/ATF_FORMAT.md) for complete format specification.

## Architecture

```
Natural Language → OpenAI Parser → Action Objects → Playwright Executor → Results
```

See [.github/copilot-instructions.md](.github/copilot-instructions.md) for detailed architecture documentation.

## Project Structure

```
agentic-test-framework/
├── agentic_test_framework/
│   ├── actions/          # Action type definitions
│   ├── parser/           # OpenAI integration
│   ├── executor/         # Playwright execution engine
│   ├── runner/           # Test orchestration
│   └── reporter/         # HTML report generation
├── config/               # Configuration files
├── examples/             # Example test scenarios
├── docs/                 # Documentation
└── tests/                # Framework tests
```

## HTML Reports

Every test automatically generates a beautiful HTML report with:
- ✅ Pass/fail status for each step
- 📸 Embedded screenshots
- 📊 Extracted data
- ⏱️ Execution timing
- 🎨 Color-coded results

Reports are saved to `test-results/report_YYYYMMDD_HHMMSS.html`

See [docs/HTML_REPORTS.md](docs/HTML_REPORTS.md) for details.

## Development

### Running Unit Tests

The framework includes a comprehensive test suite with pytest:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=agentic_test_framework --cov-report=html

# Run specific test file
pytest tests/test_actions.py

# Open coverage report in browser
xdg-open htmlcov/index.html  # Linux
open htmlcov/index.html       # macOS
```

See [tests/README.md](tests/README.md) for detailed testing documentation.

## License

MIT
