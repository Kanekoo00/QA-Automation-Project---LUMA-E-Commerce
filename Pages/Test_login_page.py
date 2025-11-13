from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui


class LoginPage:
    Email_input = (By.NAME, "j_username")
    Password_input = (By.NAME, "j_password")
    Signin_button = (By.CSS_SELECTOR, "button.btn.btn-default.scf-login")
    User_icon = (By.CSS_SELECTOR, ".panel.header .greet.welcome")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

    def open(self):
        self.driver.get(
            "https://luma.enablementadobe.com/content/luma/us/en/community/signin.html")

    def enter_email(self, email):
        email_input = self.wait.until(
            EC.visibility_of_element_located(self.Email_input))
        email_input.send_keys(email)

        time.sleep(5)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.Password_input))
        password_input.send_keys(password)

        time.sleep(5)

    def click_login(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        signin_button = self.wait.until(
            EC.element_to_be_clickable(self.Signin_button))
        self.driver.execute_script("arguments[0].click();", signin_button)

    # def handle_native_popup(self):
    #     """Handle popup alert atau save-password dialog OS-level."""
    #     try:
    #         # Tunggu sejenak biar popup muncul
    #         time.sleep(10)
    #         self.driver.switch_to.window(self.driver.current_window_handle)
    #         pyautogui.press("enter")
    #         time.sleep(0.5)
    #         print("✅ Popup handled (pressed Enter).")
    #     except Exception as e:
    #         print(f"⚠️ No popup detected or could not handle it: {e}")

    def close_cookie_popup(self):
        try:
            cookie_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.scf-cookie-accept, button.cm-btn-success"))
            )
            cookie_btn.click()
        except:
            pass

    def get_welcome_text(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.User_icon)).text
        except:
            return ""
