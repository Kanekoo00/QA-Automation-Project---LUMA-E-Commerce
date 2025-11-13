import time
import pytest
from Pages.Test_login_page import LoginPage
from Utils.driver_setup import get_driver
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.mark.manual
@pytest.mark.smoke
def test_login_valid_user():
    """
    Manual test to verify valid login once.
    This test will be excluded from automation runs.
    """
    driver = get_driver()
    login_page = LoginPage(driver)

    # Tunggu halaman load
    login_page.open()
    time.sleep(2)
    login_page.close_cookie_popup()
    login_page.click_login()
    login_page.handle_chrome_popup()
    welcome_text = login_page.get_welcome_text()

    assert "Welcome" in welcome_text, "Login failed or welcome text not found!"

    driver.quit()