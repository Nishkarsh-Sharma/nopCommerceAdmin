import time

from selenium import webdriver
import pytest
import undetected_chromedriver as uc

@pytest.fixture()

def setup(request):
        # Apply the Monkey Patch to prevent OS errors
        uc.Chrome.__del__ = lambda self: None

        # Configure and launch the stealth driver
        ops = uc.ChromeOptions()
        ops.headless = False
        #driver = uc.Chrome(options=ops, version_main=147)
        # 3. THE XDIST RACE CONDITION FIX
        driver = None
        for attempt in range(3):  # Try up to 3 times
                try:
                        # Try to launch the browser
                        driver = uc.Chrome(options=ops, version_main=147)
                        break  # If it works, instantly break out of the loop!

                except Exception as e:
                        # If it hits the FileExistsError collision...
                        if attempt == 3:
                                raise e  # If it fails 3 times, actually throw the error

                        # Wait 2 seconds to let the other worker finish patching the file!
                        print(f"\n[Worker Collision] Retrying driver launch in 2 seconds...")
                        time.sleep(2)

        # Optional: Add an implicit wait so you don't have to use time.sleep() as much
        #driver = webdriver.Chrome()
        driver.implicitly_wait(10)



        def teardown():
                try:
                        driver.quit()
                except():
                        pass
        request.addfinalizer(teardown)

        return driver

#### To generate HTML Reports

# Hook for adding environment info in HTML Report
def pytest_metadata(metadata):
    # 1. Add your custom information
    metadata['Project Name'] = 'nop Commerce'
    metadata['Module'] = 'Customers'
    metadata['Tester'] = "Youtube Expert"

    # 2. Delete default information you don't want to see
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    #metadata.pop("Packages", None) # Optional: cleans up the report even more!


