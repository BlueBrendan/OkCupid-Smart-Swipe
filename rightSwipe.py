import time

# def waitForMessageBox(driver):
#     time.sleep(0.25)
#     try:
#         driver.find_element_by_class_name('connection-view-container-close-button')
#         return
#     except:
#         waitForMessageBox(driver)

def rightSwipe(driver):
    time.sleep(0.25)
    pillButtons = driver.find_element_by_class_name("profile-userinfo-buttons")
    likeButton = pillButtons.find_element_by_id("like-button")
    likeButton.click()
    # waitForMessageBox(driver)
    # closeButton = driver.find_element_by_class_name('connection-view-container-close-button')
    # closeButton.click()
    time.sleep(0.25)
    # return to discover
    driver.get("https://www.okcupid.com/discover")