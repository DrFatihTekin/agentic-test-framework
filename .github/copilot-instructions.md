# Agentic Test Framework - AI Coding Agent Instructions

## Project Overview
An AI-powered test framework that accepts natural language test descriptions and executes them using Playwright. The framework leverages OpenAI to interpret test scenarios and translate them into browser automation commands (click, type, screenshot, navigate, etc.).

**Core Flow**: Natural Language Test → OpenAI Interpretation → Playwright Execution → Results/Screenshots

## Architecture Components

### 1. Test Parser (`src/parser/`)
- **OpenAI Parser**: Accepts natural language test descriptions, communicates with OpenAI API to extract test steps
- **ATF Parser**: Reads structured `.atf` (Agentic Test Format) files with multiple scenarios and configurations
- Converts inputs into structured action objects
- **Key Pattern**: Uses function calling/structured outputs from OpenAI to get deterministic action sequences

### 2. Playwright Executor (`src/executor/`)
- Executes structured actions against real browsers
- Implements core actions: `click()`, `type()`, `screenshot()`, `navigate()`, `waitFor()`
- Handles error recovery and retry logic
- **Key Pattern**: Each action is idempotent and includes validation

### 3. Test Runner (`src/runner/`)
- Orchestrates the test lifecycle
- Main class: `AgenticTestRunner` (handles browser contexts and test execution)
- Manages browser context and cleanup
- Collects screenshots and test artifacts
- Generates HTML reports with embedded screenshots

### 4. HTML Reporter (`src/reporter/`)
- Generates beautiful HTML test reports
- Embeds screenshots inline (base64)
- Shows pass/fail status with color coding
- Expandable test steps (failed tests expanded by default)
- Similar to RobotFramework's report style

### 5. Configuration (`config/`)
- OpenAI API settings (model, temperature, prompts)
- Playwright configuration (browsers, timeouts, viewports)
- Test environment settings

## Tech Stack
- **Language**: Python 3.11+
- **Browser Automation**: Playwright for Python
- **AI Integration**: OpenAI API (GPT-4 or compatible models)
- **Dependencies**: `openai`, `playwright`, `pytest` (for running the framework itself)

## Getting Started

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Set OpenAI API key
export OPENAI_API_KEY="your-api-key"

# Run a test from command line
python -m agentic_test_framework "Go to google.com, search for 'playwright', and click the first result"

# Create ATF template file
agentic-test --create tests/my_test.atf
agentic-test --create tests/login.atf --template login

# Run from an ATF file
agentic-test examples/login.atf
agentic-test examples/login.atf --scenario "Successful Login"
agentic-test examples/login.atf --tag smoke
```

## Development Workflows

### Adding a New Action Type
1. Add action definition to `src/actions/base.py`
2. Implement executor method in `src/executor/playwright_executor.py`
3. Update OpenAI function schema in `src/parser/openai_parser.py`
4. Add example in `examples/` directory

### Testing the Framework
```bash
# Run framework unit tests
pytest tests/

# Run example scenarios
python -m agentic_test_framework examples/login_test.txt
```

### Debugging Failed Tests
- Screenshots automatically saved to `./test-results/`
- Use `DEBUG=true` for verbose OpenAI prompts and responses
- Playwright traces can be enabled via config

## Project Conventions

### Action Naming
- Use imperative verbs: `click`, `type`, `navigate`, `wait`, `screenshot`
- Actions should be atomic and composable
- Each action returns execution status and optional data

### Natural Language Patterns
The AI is prompted to recognize these test patterns:
- Navigation: "go to [url]", "navigate to [url]", "open [url]"
- Interaction: "click [element]", "type [text] into [field]", "select [option]"
- Validation: "verify [condition]", "check that [assertion]"
- Capture: "take screenshot", "screenshot [name]"

### Error Handling
- Retries: Flaky actions (clicks, waits) retry up to 3 times
- Graceful degradation: Framework continues on non-critical failures
- Context preservation: Browser state maintained across retries

## Configuration

### OpenAI Settings (`config/openai_config.yaml`)
```yaml
model: gpt-4-turbo-preview
temperature: 0.1  # Low for deterministic test steps
max_tokens: 2000
system_prompt: "You are a test automation expert..."
```

### Playwright Settings (`config/playwright_config.yaml`)
```yaml
browser: chromium
headless: false  # Show browser during development
viewport: {width: 1920, height: 1080}
timeout: 30000
screenshot_on_failure: true
```

## Key Files

- `src/parser/openai_parser.py` - OpenAI integration and prompt engineering
- `src/executor/playwright_executor.py` - Core Playwright action implementations
- `src/actions/base.py` - Action type definitions and schemas
- `src/runner/test_runner.py` - Main orchestration logic
- `examples/` - Sample natural language test scenarios

## Common Patterns

### Selector Strategy
The AI generates selectors in order of preference:
1. `data-testid` attributes (most reliable)
2. ARIA labels and roles (accessibility-friendly)
3. Text content (user-visible)
4. CSS classes (least preferred)

### State Management
- Each test gets a fresh browser context
- Cookies/storage can be preserved across steps within a test
- Use `context.json` to share state between tests

### Extension Points
- Custom actions: Implement `Action` base class
- Custom validators: Extend `Validator` for assertions
- Custom reporters: Implement `Reporter` interface

---

**Development Philosophy**: Keep the AI prompt simple and focused. Let OpenAI handle ambiguity in natural language. Make Playwright execution robust and observable. Fail fast with clear error messages.
