"""ATF file template generator"""

from pathlib import Path
from typing import Optional


class ATFTemplateGenerator:
    """Generate ATF file templates"""
    
    @staticmethod
    def generate_basic_template() -> str:
        """Generate a basic ATF template"""
        return """# Test Suite Name

Description: Brief description of what this test suite does

@config browser=chromium
@config headless=false

## Scenario: First Test
@tag smoke

Go to example.com
Verify page contains 'Example Domain'
Take a screenshot

## Scenario: Second Test

Add your test steps here...
"""
    
    @staticmethod
    def generate_login_template() -> str:
        """Generate a login flow template"""
        return """# Login Test Suite

Description: Test suite for user authentication flows

@config browser=chromium
@config headless=false

## Scenario: Successful Login
@tag smoke
@tag login

Go to YOUR_APP_URL/login
Type 'YOUR_USERNAME' into username field
Type 'YOUR_PASSWORD' into password field
Click login button
Verify page contains 'Welcome'
Take a screenshot named 'successful_login'

## Scenario: Invalid Credentials
@tag login
@tag negative

Go to YOUR_APP_URL/login
Type 'invalid_user' into username field
Type 'wrong_password' into password field
Click login button
Verify page contains 'Invalid credentials'
Take a screenshot

## Scenario: Empty Form Validation
@tag login
@tag validation

Go to YOUR_APP_URL/login
Click login button
Verify page contains 'required'
"""
    
    @staticmethod
    def generate_ecommerce_template() -> str:
        """Generate an e-commerce flow template"""
        return """# E-Commerce Test Suite

Description: Test suite for shopping and checkout flows

@config browser=chromium
@config headless=false

## Scenario: Product Search
@tag smoke
@tag search

Go to YOUR_SHOP_URL
Type 'product name' into search box
Click search button
Verify page contains 'results'
Take a screenshot

## Scenario: Add to Cart
@tag cart

Go to YOUR_SHOP_URL
Click first product
Click 'Add to Cart' button
Verify page contains 'Added to cart'
Click cart icon
Verify page contains product name

## Scenario: Checkout Flow
@tag checkout
@tag critical

Go to YOUR_SHOP_URL/cart
Click 'Checkout' button
Type 'customer@email.com' into email field
Type '123 Main St' into address field
Click 'Continue' button
Verify page contains 'Payment'
"""
    
    @staticmethod
    def generate_api_testing_template() -> str:
        """Generate an API/integration testing template"""
        return """# API Integration Test Suite

Description: Test suite for API endpoints and integrations

@config browser=chromium
@config headless=true

## Scenario: User Registration Flow
@tag smoke
@tag registration

Go to YOUR_APP_URL/register
Type 'newuser@example.com' into email field
Type 'SecurePass123' into password field
Type 'SecurePass123' into confirm password field
Click register button
Verify page contains 'Registration successful'
Verify URL contains 'dashboard'

## Scenario: Profile Update
@tag profile

Go to YOUR_APP_URL/login
Type 'user@example.com' into email field
Type 'password' into password field
Click login button
Click 'Profile' link
Type 'Updated Name' into name field
Click 'Save' button
Verify page contains 'Profile updated'
"""
    
    @staticmethod
    def create_file(
        output_path: str,
        template_type: str = "basic",
        overwrite: bool = False
    ) -> bool:
        """Create an ATF file from template
        
        Args:
            output_path: Path where to create the ATF file
            template_type: Type of template (basic, login, ecommerce, api)
            overwrite: Whether to overwrite existing file
            
        Returns:
            True if file was created, False if file exists and overwrite=False
        """
        path = Path(output_path)
        
        # Check if file exists
        if path.exists() and not overwrite:
            return False
        
        # Ensure .atf extension
        if not output_path.endswith('.atf'):
            path = Path(f"{output_path}.atf")
        
        # Get template content
        templates = {
            "basic": ATFTemplateGenerator.generate_basic_template(),
            "login": ATFTemplateGenerator.generate_login_template(),
            "ecommerce": ATFTemplateGenerator.generate_ecommerce_template(),
            "api": ATFTemplateGenerator.generate_api_testing_template()
        }
        
        content = templates.get(template_type, templates["basic"])
        
        # Create directory if needed
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write file
        path.write_text(content)
        
        return True
