from datetime import datetime
import pytest
import base64
import shutil
import os
import re

def pytest_addoption(parser):
    """Registers custom command-line arguments."""
    parser.addoption(
        "--report-name", 
        action="store", 
        default=None, 
        help="Custom prefix for the HTML report filename"
    )

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """ Check if the user provided a custom name via --report-name
        If not, fall back to the timestamp naming convention"""
    report_name = config.getoption("--report-name", default=None)

    if not report_name:
        # 2. If no flag, look at the files being tested
        # config.args contains the list of files/folders passed to pytest
        if config.args:
            # Grab the last part of the path (e.g., 'test_js_alerts.py') 
            # and strip the '.py'
            # os.path.basename handles the path logic correctly for Windows/Mac
            # We strip the extension and use re.sub to remove any non-alphanumeric characters
            raw_target = os.path.basename(config.args[0]).replace(".py", "")
            sanitized_target = re.sub(r'[^\w\-_]', '_', raw_target)
            report_name = f"auto_{sanitized_target}"
            
            # target = config.args[0].split("/")[-1].replace(".py", "")
            # report_name = f"auto_{target}"
        else:
            report_name = "full_suite"
    if not os.path.exists("results"):
        os.makedirs("results")

    if hasattr(config.option, 'htmlpath') and not config.option.htmlpath:
            now = datetime.now().strftime("%Y%m%d_%H%M")
            name_tag = re.sub(r'[^\w\-_]', '_', report_name) if report_name else "general"
            # name_tag = report_name if report_name else "general"
            config.option.htmlpath = f"results/{now}_{name_tag}_report.html"
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

@pytest.hookimpl(hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    """Executes after all tests are done."""
    yield
    # Get the path of the report we just created
    report_path = getattr(session.config.option, 'htmlpath', None)
    
    if report_path and os.path.exists(report_path):
        try:
            shutil.copy(report_path, "results/latest_report.html")
            print(f"\n[STAMP] Quick link created: results/latest_report.html")
        except Exception as e:
            print(f"\n[ERROR] Could not create latest_report: {e}")
    else:
        if not report_path:
            print("\n[STAMP] No report path defined.")
        else:
            print(f"\n[STAMP] Report file not found at: {report_path}")