import pytest
import base64

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