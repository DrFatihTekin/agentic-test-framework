"""Test configuration and fixtures"""

import pytest
import os
from pathlib import Path


@pytest.fixture
def sample_test_description():
    """Sample test description"""
    return "Go to example.com, click login, and take a screenshot"


@pytest.fixture
def test_output_dir(tmp_path):
    """Create temporary test output directory"""
    output_dir = tmp_path / "test-results"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def mock_openai_key(monkeypatch):
    """Mock OpenAI API key in environment"""
    monkeypatch.setenv("OPENAI_API_KEY", "test-api-key-12345")
    return "test-api-key-12345"


@pytest.fixture
def sample_screenshot(tmp_path):
    """Create a sample screenshot file"""
    screenshot_dir = tmp_path / "screenshots"
    screenshot_dir.mkdir()
    screenshot_path = screenshot_dir / "test_screenshot.png"
    
    # Create a minimal PNG file
    png_header = b'\x89PNG\r\n\x1a\n'
    screenshot_path.write_bytes(png_header + b'\x00' * 100)
    
    return str(screenshot_path)


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test (may require external services)"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
