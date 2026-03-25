from datetime import datetime
import pytest
import base64

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # If no report name is provided, generate a timestamped one automatically
    if not config.option.htmlpath:
        now = datetime.now().strftime("%Y%m%d_%H%M")
        config.option.htmlpath = f"results/report_{now}.html"
        config.option.self_contained_html = True
    # Add custom metadata to the report header
    if hasattr(config, '_metadata'):
        config._metadata['Project'] = 'The Internet Automation'
        config._metadata['Tester'] = 'Your Name'
        config._metadata['Site'] = 'Heroku'

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the pytest-html plugin to access its 'extras'
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Get the 'page' fixture from the test
        page = item.funcargs.get("page")
        if page:
            # 1. Capture screenshot as raw bytes
            screenshot_bytes = page.screenshot()
            # 2. Convert bytes to a base64 string
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            # 3. Create the HTML image tag
            html = f'<div><img src="data:image/png;base64,{screenshot_base64}" style="width:600px;height:300px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>'
            # 4. Inject into the report
            extra.append(pytest_html.extras.html(html))
        report.extra = extra