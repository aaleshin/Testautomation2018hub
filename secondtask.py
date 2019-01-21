import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Before starting the test, copy chromedriver from http: // www.seleniumhq.org / download / and enter correct PATH.!!

driver = selenium.webdriver.Chrome("D:\\downloads\\avtotests\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://planner-sandbox.dev.thumbtack.net")
driver.find_element_by_css_selector('#id_username').send_keys('gerardkunze')
driver.find_element_by_css_selector('#id_password').send_keys('123456')
driver.find_element_by_tag_name('button').click()
driver.find_element_by_xpath('//a[@class="navbar__link"]//span[@class="avatar avatar_size_m"]').click()
driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[2]/ul/li[4]/a').click()
driver.find_element_by_css_selector('div.buttons_wrapper > div > a').click()
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div[1]/div/div[1]/div/div[1]/select')))
driver.find_element_by_css_selector('div.modal-body > div > div.vacation-type-block.row > div > div.vacation-type-select > select').click()
driver.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[1]/div/div[1]/select/option[5]').click()
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@placeholder="QALead or DevLead, PM and Department Head"]')))
driver.find_element_by_css_selector('div.employees-filter__filter-first-priority-approver.approvers-multiselect > span > span.selection > span > ul > li > input').click()
driver.find_element_by_css_selector('div.employees-filter__filter-first-priority-approver.approvers-multiselect > span > span.selection > span > ul > li > input').send_keys('aleshin')
actions = ActionChains(driver).send_keys(Keys.ENTER).perform()
driver.find_element_by_css_selector('div.form-actions > button.btn.btn-primary.js-submit-request-button').click()
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div > div.modal-footer > div > button.btn.btn-primary.js-continue-request-button')))
driver.find_element_by_css_selector('div > div.modal-footer > div > button.btn.btn-primary.js-continue-request-button').click()
driver.get("https://planner-sandbox.dev.thumbtack.net/employees/")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, 'nameFilter')))
driver.find_element_by_id('nameFilter').send_keys('aleshin')
driver.find_element_by_css_selector('body.page:nth-child(2) div.page__inner:nth-child(1) div.content div.main div.toolbar.js-toolbar:nth-child(2) div.toolbar__group:nth-child(2) div.btn-group.radio-group.radio-group_type_button label.radio.radio_type_button:nth-child(2) > span.btn.btn-default').click()
driver.find_element_by_xpath('//button[@class="btn btn-default js-toggle-department"]').click()
driver.find_element_by_xpath('//div[@class="checkbox-filter__options-list"]//div[9]//div[1]//label[1]//i[1]').click()
driver.find_element_by_xpath('//button[@class="btn btn-default js-toggle-skills"]').click()
driver.find_element_by_xpath('//input[@placeholder="Type to find skill"]').send_keys("Automated testing")
actions = ActionChains(driver).send_keys(Keys.ENTER).perform()
driver.find_element_by_xpath('//div[@class="filter-menu skill-filter"]//button[@class="btn btn-sm btn-primary js-apply"][contains(text(),"Apply")]').click()
driver.find_element_by_xpath('//a[@class="navbar__link"]//span[@class="avatar avatar_size_m"]').click()
driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[2]/ul/li[3]/a').click()
driver.find_element_by_xpath('//button[@class="btn btn-large btn-info add-goal-btn js-add-goal-btn"]').click()
driver.find_element_by_xpath('//div[@class="col-sm-5"]//input[@placeholder="@TODO"]').send_keys("For DS!")
driver.find_element_by_xpath('//textarea[@placeholder="Describe the goal"]').send_keys("Make DS great again!")


driver.find_element_by_xpath('//*[@id="goalsInProgress"]/div[1]/button[1]').click()
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div[1]/div[2]/div[1]/div[3]/button[1]').click()
driver.find_element_by_xpath('//div[@class="goal-actions open"]//li[@title="Delete"]').click()
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[@class="dscrd-btn btn btn-primary js-goal-undo-delete-goal"]')))
driver.find_element_by_xpath('//button[@class="dscrd-btn btn btn-primary js-goal-undo-delete-goal"]').click()
driver.quit()
