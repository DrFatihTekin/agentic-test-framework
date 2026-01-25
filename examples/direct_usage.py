"""Example: Direct usage of components"""

from agentic_test_framework import OpenAIParser, PlaywrightExecutor
from agentic_test_framework.actions import NavigateAction, ScreenshotAction


def example_direct_usage():
    """Example of using components directly without TestRunner"""
    
    # Example 1: Manual action creation
    print("=== Example: Manual Actions ===\n")
    
    actions = [
        NavigateAction(description="Go to Python.org", url="python.org"),
        ScreenshotAction(description="Capture homepage", name="python_home"),
    ]
    
    with PlaywrightExecutor(headless=False) as executor:
        for action in actions:
            result = executor.execute(action)
            print(f"{result.message}")
    
    # Example 2: Parse natural language
    print("\n=== Example: OpenAI Parsing ===\n")
    
    parser = OpenAIParser()
    test_desc = "Go to example.com and take a screenshot"
    actions = parser.parse(test_desc)
    
    print(f"Parsed {len(actions)} actions:")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. [{action.type}] {action.description}")


if __name__ == "__main__":
    example_direct_usage()
