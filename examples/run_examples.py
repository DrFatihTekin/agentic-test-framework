"""Example: Running tests programmatically"""

from agentic_test_framework import AgenticTestRunner


def main():
    # Initialize the test runner
    runner = AgenticTestRunner(headless=False)  # Set headless=True to hide browser
    
    # Example 1: Simple navigation and screenshot
    print("\n=== Example 1: Simple Test ===")
    runner.run("Go to example.com and take a screenshot")
    
    # Example 2: Search workflow
    print("\n=== Example 2: Search Test ===")
    runner.run(
        "Navigate to google.com, "
        "search for 'playwright automation', "
        "wait 2 seconds, "
        "and take a screenshot of the results"
    )
    
    # Example 3: Multi-step interaction
    print("\n=== Example 3: Complex Test ===")
    runner.run(
        "Go to github.com, "
        "click the search button, "
        "type 'agentic testing' in the search field, "
        "take a screenshot"
    )


if __name__ == "__main__":
    main()
