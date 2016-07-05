import os
from appium import webdriver

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

@given('I click on the add contact button')
def step_impl(context):
  button_one = context.driver.find_element_by_class_name("android.widget.Button")
  button_one.click()

@when('I enter a name and email')
def step_impl(context):
  text_fields = context.driver.find_elements_by_class_name("android.widget.EditText")
  text_fields[0].send_keys("Some Name")
  text_fields[2].send_keys("Some@example.com")

@then('I click the Save button')
def step_impl(context):
  context.driver.find_element_by_class_name("android.widget.Button").click()
