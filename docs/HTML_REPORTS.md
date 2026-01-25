# HTML Reports

The framework automatically generates beautiful HTML test reports with embedded screenshots, similar to RobotFramework's reporting.

## Features

- **📊 Visual Summary**: Test status, passed/failed counts, duration
- **📸 Embedded Screenshots**: Screenshots are embedded inline (no external files needed)
- **🎨 Color-Coded Results**: Green for pass, red for fail
- **📂 Expandable Steps**: Click to expand/collapse test step details
- **🔍 Auto-Expand Failures**: Failed steps are automatically expanded
- **📝 Extracted Data**: Shows any data extracted during the test
- **❌ Error Details**: Clear error messages for failed steps

## Location

Reports are saved to: `test-results/report_YYYYMMDD_HHMMSS.html`

## Opening Reports

### On Linux/Mac:
```bash
# Open the latest report
xdg-open test-results/report_*.html  # Linux
open test-results/report_*.html      # Mac
```

### On Windows:
```bash
start test-results\report_*.html
```

### Or just open in your browser:
Simply open the HTML file in any web browser - it's a self-contained file with everything embedded!

## Disabling Reports

If you don't want HTML reports:
```bash
python -m agentic_test_framework "your test" --no-report
```

## Report Contents

Each report includes:

1. **Header**: Framework name and timestamp
2. **Summary Cards**:
   - Overall status (PASS/FAIL)
   - Total steps
   - Passed count
   - Failed count  
   - Duration
   - Start time

3. **Test Description**: The natural language test you provided

4. **Execution Steps**: Each step with:
   - Step number
   - Pass/fail status
   - Action type (navigate, click, type, etc.)
   - Description
   - Expandable details with:
     - Success/error messages
     - Extracted data (if any)
     - Embedded screenshot (if any)

5. **Footer**: Generation timestamp

## Example

```bash
# Run a test (generates report automatically)
python -m agentic_test_framework "Go to example.com, take a screenshot, verify it contains 'Example'"

# Output will show:
📄 HTML Report: test-results/report_20260124_234528.html

# Open it in your browser!
```

## Sharing Reports

The HTML reports are fully self-contained - you can:
- Email them
- Upload to file sharing services
- Archive them for test history
- Open them on any computer with a browser

No need to share screenshots separately - they're all embedded!
