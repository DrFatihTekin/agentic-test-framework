# Playwright Reporting & Debugging

The Agentic Test Framework now integrates Playwright's powerful reporting and debugging capabilities alongside your custom HTML reports.

## Available Reports

### 1. Custom HTML Report (Default)
Your natural language test report with:
- ✅ Test description and parsed actions
- ✅ Step-by-step execution results
- ✅ Embedded screenshots
- ✅ Expected vs Actual comparisons for assertions
- ✅ Pass/fail indicators with color coding

**Location**: `test-results/report_YYYYMMDD_HHMMSS.html`

### 2. Playwright Trace (Default - NEW!)
Time-travel debugging with:
- 🎬 DOM snapshots at each action
- 🌐 Network traffic logs
- 📋 Console logs
- 🖼️ Screenshots
- 📊 Timeline view
- 🔍 Ability to inspect any point in execution

**Location**: `test-results/traces/trace_YYYYMMDD_HHMMSS.zip`

**View trace:**
```bash
playwright show-trace test-results/traces/trace_YYYYMMDD_HHMMSS.zip
```

### 3. Video Recordings (Automatic)
Full video recording of browser session

**Location**: `test-results/videos/*.webm`

## Usage Examples

### Enable All Reports (Default)
```bash
# All Playwright features enabled by default
agentic-test "Go to example.com and click login"
```

Output:
```
📄 HTML Report: test-results/report_20260125_012345.html
🎬 Playwright Trace: test-results/traces/trace_20260125_012345.zip
   View with: playwright show-trace test-results/traces/trace_20260125_012345.zip
```

### Disable Playwright Trace
```bash
# Only generate custom HTML report
agentic-test "test description" --no-trace
```

### Disable All Reports
```bash
# Console output only
agentic-test "test description" --no-report --no-trace
```

### Disable Screenshots but Keep Trace
```bash
# Trace without individual step screenshots
agentic-test "test description" --no-step-screenshots
```

## Viewing Playwright Traces

### Interactive Trace Viewer

1. **After test completion**, copy the trace path from output
2. **Run the viewer**:
   ```bash
   playwright show-trace test-results/traces/trace_20260125_012345.zip
   ```

3. **Explore features**:
   - **Timeline**: See all actions in chronological order
   - **DOM Snapshot**: Inspect HTML at any point
   - **Network**: View all requests/responses
   - **Console**: See console.log() output
   - **Screenshots**: Browse captured screenshots
   - **Source**: View JavaScript sources

### What You Can Debug

✅ **Why did a click fail?**
- Inspect DOM to see if element was visible
- Check if element was covered by another element
- See exact selector that was tried

✅ **Network issues?**
- View all API calls
- See request/response headers
- Check timing and status codes

✅ **JavaScript errors?**
- Console tab shows all errors
- Stack traces available
- Source code inspection

✅ **Timing issues?**
- Timeline shows exact wait times
- See when elements appeared/disappeared
- Identify race conditions

## ATF File Configuration

```yaml
@config
browser: chromium
headless: false
trace: true        # Enable Playwright trace
screenshots: true  # Enable step screenshots
@end

## My Test Scenario
Navigate to https://example.com
Click on the login button
Type "user@example.com" into email field
```

## CLI Options Summary

| Option | Description | Default |
|--------|-------------|---------|
| `--no-report` | Disable custom HTML report | Enabled |
| `--no-trace` | Disable Playwright trace | Enabled |
| `--no-step-screenshots` | Disable automatic screenshots | Enabled |
| `--headless` | Run browser without UI | Visible |

## Programmatic Usage

```python
from agentic_test_framework import AgenticTestRunner

runner = AgenticTestRunner(
    browser_type="chromium",
    headless=False,
    generate_report=True,           # Custom HTML report
    screenshot_all_steps=True,       # Step screenshots
    enable_playwright_trace=True     # Playwright trace
)

results = runner.run("Go to google.com and search for playwright")
```

## Artifacts Structure

```
test-results/
├── screenshots/               # Individual step screenshots
│   ├── step_001_navigate.png
│   ├── step_002_click.png
│   └── ...
├── traces/                    # Playwright traces
│   ├── trace_20260125_012345.zip
│   └── ...
├── videos/                    # Video recordings
│   ├── video-20260125-012345.webm
│   └── ...
├── report_20260125_012345.html  # Custom HTML report
└── ...
```

## Best Practices

### For Development
```bash
# Full visibility - all reports + visible browser
agentic-test test.atf --no-headless
```

### For CI/CD
```bash
# Fast execution - headless with reports
agentic-test test.atf --headless
```

### For Quick Tests
```bash
# Minimal artifacts - console only
agentic-test "quick test" --no-report --no-trace --headless
```

### For Debugging Failed Tests
```bash
# Generate trace, then view it
agentic-test test.atf
playwright show-trace test-results/traces/trace_*.zip
```

## Trace File Sharing

Trace files are fully self-contained and can be shared:

1. **Zip file is portable** - contains all data
2. **Share with team members** - they can view with `playwright show-trace`
3. **Attach to bug reports** - includes full reproduction data
4. **Archive for later** - traces can be viewed anytime

## Performance Considerations

- **Trace files**: 5-20 MB per test (includes snapshots, network, videos)
- **Screenshots**: ~100-500 KB per step
- **Videos**: 1-10 MB per test

To reduce artifact size:
```bash
# Disable features you don't need
agentic-test test.atf --no-trace --no-step-screenshots
```

## Troubleshooting

### Trace viewer not opening
```bash
# Install Playwright browsers
playwright install
```

### Large trace files
```bash
# Disable video recording in code or use shorter tests
# Traces grow with test duration and page complexity
```

### Missing artifacts
```bash
# Check test-results/ directory permissions
# Ensure sufficient disk space
ls -lah test-results/
```

## Learn More

- [Playwright Trace Viewer](https://playwright.dev/docs/trace-viewer)
- [Playwright Inspector](https://playwright.dev/docs/inspector)
- [Debugging Tests](https://playwright.dev/docs/debug)
