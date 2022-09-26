class BasePageLocators:
    dismiss_button = "//button[@aria-label='Close Welcome Banner']/span[1]"
    account_button = "//span[contains(text(), 'Account')]"
    login_button = "//*[@role='menu']"
    email_field = "//input[@name='email']"
    password_field = "//input[@name='password']"
    login_confirm_button = "//button[@id='loginButton']"
    invalid_email_password_messsage = "//*[contains(text(), 'Invalid email or password.')]"