dismiss_button = "//button[@aria-label='Close Welcome Banner']/span[1]"
account_button = "//span[contains(text(), 'Account')]"
login_button = "//*[@role='menu']"
email_field = "//input[@name='email']"
password_field = "//input[@name='password']"
login_confirm_button = "//button[@id='loginButton']"
invalid_email_password_message = "//*[contains(text(), 'Invalid email or password')]"

# Home Page
your_basket_button = "//*[contains(text(), ' Your Basket')]"
items_on_page = "//button[@aria-label='Add to Basket']"
# only_one_item_element = "//*[text()='Only 1 left']/../../div/button"
only_one_item_element = "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile[4]/div/mat-card/div[3]/button"

# Basket Page
delete_item_buttons = "//button[@class='mat-focus-indicator mat-icon-button mat-button-base']"
basket_button = "//*[@routerlink='/basket']"
element_for_check = "//*[text()=' Best Juice Shop Salesman Artwork ']"

#Side Navigation
customer_feedback_button = "//*[text()=' Customer Feedback ']//.."
side_navigation_button = "//*[@aria-label='Open Sidenav']"
about_us_button = "//span[contains(text(), 'About Us')]"

# About US
twiter_button = "//*[@class='mat-focus-indicator mat-raised-button mat-button-base mat-accent']"

# Customer Feedback
comment_field_form = "//*[@aria-label='Field for entering the comment or the feedback']"
slider = "//*[@class='mat-slider-thumb-label']"
captcha = "//*[@aria-label='CAPTCHA code which must be solved']"
captcha_result_form = "//*[@aria-label='Field for the result of the CAPTCHA code']"
submit = "//*[@type='submit']"
thank_you_for_your_feedback ="//*[text()='Thank you for your feedback.']"