# Running Tests

## Quick Start

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=agentic_test_framework

# Run specific test file
pytest tests/test_actions.py

# Run specific test
pytest tests/test_actions.py::TestActionModels::test_navigate_action

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

## Test Categories

### Unit Tests
Fast tests that don't require external services:
```bash
pytest -m "not integration"
```

### Integration Tests
Tests that may require external services (marked with `@pytest.mark.integration`):
```bash
pytest -m integration
```

## Coverage Reports

After running tests with `--cov`, open the HTML coverage report:
```bash
# Generate coverage report
pytest --cov=agentic_test_framework --cov-report=html

# Open in browser (Linux)
xdg-open htmlcov/index.html
```

## Test Structure

```
tests/
├── __init__.py
├── conftest.py           # Shared fixtures and configuration
├── test_actions.py       # Action model tests
├── test_parser.py        # OpenAI parser tests
├── test_executor.py      # Playwright executor tests (future)
├── test_runner.py        # Test runner tests
└── test_reporter.py      # HTML reporter tests
```

## Writing New Tests

### Basic Test Structure

```python
import pytest
from agentic_test_framework.actions import NavigateAction

class TestMyFeature:
    """Test description"""
    
    def test_something(self):
        """Test case description"""
        action = NavigateAction(description="Go", url="https://example.com")
        assert action.url == "https://example.com"
```

### Using Fixtures

```python
def test_with_fixture(self, sample_test_description):
    """Test using a fixture from conftest.py"""
    assert "example.com" in sample_test_description
```

### Mocking External Services

```python
from unittest.mock import patch, Mock

@patch('agentic_test_framework.parser.openai_parser.OpenAI')
def test_with_mock(self, mock_openai):
    """Test with mocked OpenAI"""
    mock_client = Mock()
    mock_openai.return_value = mock_client
    # Your test code
```

## Continuous Integration

Add to your CI pipeline:
```yaml
# .github/workflows/test.yml
- name: Run tests
  run: |
    pip install -r requirements.txt
    pytest --cov=agentic_test_framework
```

## Common Issues

### Import Errors
Make sure package is installed in editable mode:
```bash
pip install -e .
```

### Missing Dependencies
Install test dependencies:
```bash
pip install pytest pytest-cov pytest-mock
```
