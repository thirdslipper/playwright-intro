from datetime import datetime
import pytest
import base64

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # If no report name is provided, generate a timestamped one automatically
    if hasattr(config.option, 'htmlpath') and not config.option.htmlpath:
            now = datetime.now().strftime("%Y%m%d_%H%M")
            config.option.htmlpath = f"results/report_{now}.html"
            config.option.self_contained_html = True

# This hook specifically handles the metadata for the report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata, config):
    """
    Specific hook for pytest-html v4.0+ and pytest-metadata to 
    populate the 'Environment' section of the report.
    """
    metadata['Project'] = 'The Internet Automation'
    metadata['Tester'] = 'Slipper'
    metadata['Site'] = 'Heroku'
    # If Base URL is missing from metadata, try to pull it from the config
    url = config.getoption('base_url', default='Not Defined')
    metadata['Base URL'] = url
        
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    # Insert the header at index 2 (between 'Test' and 'Duration')# Insert 'Description' header before 'Result'
    cells.insert(1, '<th class="sortable">Description</th>')

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    # Pull the docstring we stored in the report during 'makereport'
    description = getattr(report, "description", "")
    cells.insert(1, f"<td>{description}</td>")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the pytest-html plugin to access its 'extras'
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    # Capture the docstring from the test function
    report.description = str(item.function.__doc__) if item.function.__doc__ else ""

    # Screenshot logic for failures
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