
from selenium.webdriver.common.by import By

class DashboardLocators:
    VENDOR_ID = (By.ID, "vendor_id_drp")  # Vendor dropdown
    SUBMIT_BUTTON = (By.ID, "submit-button")  # Submit button
    HEADER = (By.XPATH, "//div[@class='Areas_headind']/h2[normalize-space(text())='Dashboard']")
    # More specific locators
    MODAL_HEADER = (By.XPATH, "//h3[text()='Available Cars']/ancestor::div[contains(@class,'modal-header')]")
    CLOSE_BUTTON = (By.XPATH,
                    "//h3[text()='Available Cars']/ancestor::div[contains(@class,'modal-header')]//button[contains(@class,'close')]")
    # Unique locator for the "OK" button inside the popup
    OK_BUTTON = (By.XPATH,
                 "//div[contains(@class,'sa-confirm-button-container')]//button[contains(@class,'confirm') and text()='OK']")


