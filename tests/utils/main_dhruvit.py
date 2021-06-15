from selenium.webdriver.firefox.webdriver import WebDriver
from actions import click, delay, is_element_present, select_by_value, send_keys
from selenium import webdriver

driver = webdriver.Chrome("drivers/chromedriver")

# link : https://www.marktplatz-mittelstand.de/Firmeneintrag
# author : Manthan 
def unternehmensverzeichnis(driver : WebDriver):
    # Data
    email_data = "baap@gmail.com"
    password_data = "Baap@baap"
    gender = "Female"
    personal_title_textbox_data = "BaapDummy"
    personal_first_name_textbox_data = "Baap"
    personal_name_textbox_data = "Maa"
    personal_department_textbox_data = "Kachara"
    personal_function_textbox_data = "collecting Kachara"
    personal_telephone_textbox_data = "+49152901820"
    personal_phone_textbox_data = "+49152901821"
    company_name_textbox_data = "Baap Company"
    company_additional_textbox_data = "Baap Additional"
    company_street_textbox_data = "Enderstraße"
    company_houseNumber_textbox_data = "602"
    country = "Germany"
    company_postal_code_data = "01277"
    company_city_data = "Dresden"
    company_telephone_data = "+49152901822"
    company_website_data = "hhtps://www.baap.com"
    company_vat_data = ""

    # Logic for sleecting gender dropdown
    if gender.lower() == "Male".lower():
        personal_salutation_data = "Herr"
    elif gender.lower() == "Female".lower():
        personal_salutation_data = "Frau"
    else:
        personal_salutation_data = ""

    # Logic for selecting country else make it as blank
    if country.lower() == "Austria".lower():
        company_country_select_value = "AT"
    elif country.lower() == "Switzerland".lower():
        company_country_select_value = "CH"
    elif country.lower() == "Germany".lower():
        company_country_select_value = "DE"
    else:
        company_country_select_value = ""
    # Locators 
    cookie_accept_id = "cookieModalAccept"
    register_button_xpath = "//span[text() = 'Registrierung']"
    email_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Mail' or @id = 'Mail']"
    password_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Passwort' or @id = 'Passwort']"
    confirmPassword_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Passwort2' or @id = 'Passwort2']"
    personal_salutation_select_xpath = "//form[@id = 'EBID_CreateUser']//select[@name = 'Salutation']"
    personal_title_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name = 'Titel']"
    personal_first_name_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@id = 'Vorname']"
    personal_name_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@id = 'Name']"
    personal_department_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Abteilung']"
    personal_function_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Funktion']"
    personal_telephone_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'TelefonDurchwahl']"
    personal_phone_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Mobil']"
    company_name_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Firma']"
    company_additional_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Zusatz']"
    company_street_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Strasse']"
    company_houseNumber_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Hausnummer']"
    company_country_select_xpath = "//form[@id = 'EBID_CreateUser']//select[@name= 'Country']"
    company_postal_code_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'PLZ' or @id = 'CatchwordsZip']"
    company_city_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Ort' or @id = 'CatchwordsCity']"
    company_telephone_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Telefon' or @id = 'CatchwordsTelephone']"
    company_website_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'Url' or @id = 'CatchwordsHomepage']"
    company_vat_textbox_xpath = "//form[@id = 'EBID_CreateUser']//input[@name= 'VatNo' or @id = 'CatchwordsUStID']"

    term_condition_checkbox_id = "Registration_Legal"
    register_submit_button_id = "createruserButton"
    
    driver.get("https://www.unternehmensverzeichnis.org")
    # Click on the accept cookies button
    if is_element_present(driver , locator_value=cookie_accept_id , locator_name="cookie accept button" , id=True):
        click(driver , cookie_accept_id , "cookie accept button" , id = True)

    # Click on registration button
    delay()
    click(driver , register_button_xpath , "Registration button" , xpath= True)
    
    # Salutation
    delay()
    if personal_salutation_data != "":
        select_by_value(driver , locator_value= personal_salutation_select_xpath , locator_name="Personal Salutation Dropdown" , xpath= True , select_value= personal_salutation_data)

    # Title
    if personal_title_textbox_data != "":
        send_keys(driver , locator_value=personal_title_textbox_xpath , xpath=True , locator_name="Personal Title input text" , text=personal_title_textbox_data) 

    # First Name
    if personal_first_name_textbox_data != "":
        send_keys(driver , locator_value=personal_first_name_textbox_xpath , xpath=True , locator_name="Personal first name input text" , text=personal_first_name_textbox_data)
    elif personal_first_name_textbox_data == "":
        raise Exception("Personal First name is not present which is a mandatory field")

    # Name 
    if personal_name_textbox_data != "":
        send_keys(driver , locator_value=personal_name_textbox_xpath , xpath=True , locator_name="Personal name input text" , text=personal_name_textbox_data)
    elif personal_name_textbox_data == "":
        raise Exception("Personal Name is not present which is a mandatory field")

    # Department 
    if personal_department_textbox_data !="":
        send_keys(driver , locator_value=personal_department_textbox_xpath , xpath=True , locator_name="Personal department input text" , text=personal_department_textbox_data)

    # Function
    if personal_function_textbox_data != "":
        send_keys(driver , locator_value=personal_function_textbox_xpath , xpath=True , locator_name="Personal function input text" , text=personal_function_textbox_data)
    
    # Telephone
    if personal_telephone_textbox_data != "":
        send_keys(driver , locator_value=personal_telephone_textbox_xpath , xpath=True , locator_name="Personal Telephone number input text" , text=personal_telephone_textbox_data)

    # Phone Number
    if personal_phone_textbox_data != "":
        send_keys(driver , locator_value=personal_phone_textbox_xpath , xpath=True , locator_name="Personal Phone number input text" , text=personal_phone_textbox_data)
    
    # Comapany Name
    if company_name_textbox_data != "":
        send_keys(driver , locator_value=company_name_textbox_xpath , xpath=True , locator_name="Company name input text" , text=company_name_textbox_data)
    
    # Additive
    if company_additional_textbox_data != "":
        send_keys(driver , locator_value=company_additional_textbox_xpath , xpath=True , locator_name="Company additive input text" , text=company_additional_textbox_data)
    
    # Road
    if company_street_textbox_data != "":
        send_keys(driver , locator_value=company_street_textbox_xpath , xpath=True , locator_name="Company Street input text" , text=company_street_textbox_data)
    
    # House number 
    if company_houseNumber_textbox_data != "":
        send_keys(driver , locator_value=company_houseNumber_textbox_xpath , xpath=True , locator_name="Cpmpany House Number input text" , text=company_houseNumber_textbox_data)

    # Country
    if company_country_select_value != "":
        select_by_value(driver , locator_value=company_country_select_xpath , select_value=company_country_select_value , locator_name="Company Country Dropdown" , xpath=True )
    
    # Postal Code 
    if company_postal_code_data != "":
        send_keys(driver , locator_value=company_postal_code_textbox_xpath , xpath=True , locator_name="Company Postal Code input text" , text=company_postal_code_data)

    # State
    if company_city_data != "":
        send_keys(driver , locator_value=company_city_textbox_xpath , xpath=True , locator_name="Company City input text" , text=company_city_data)
    
    # Company Phone
    if company_telephone_data != "":
        send_keys(driver , locator_value=company_telephone_textbox_xpath , xpath=True , locator_name="Company Phone input text" , text=company_telephone_data)

    # Company Website URL
    if company_website_data != "":
        send_keys(driver , locator_value=company_website_textbox_xpath , xpath=True , locator_name="Comapny Website input text" , text=company_website_data)

    #  Vat number 
    if company_vat_data != "":
        send_keys(driver , locator_value=company_vat_textbox_xpath , xpath=True , locator_name="Comapnay Vat number input text" , text=company_vat_data)
    
    #  Email
    if email_data == "":
        raise Exception("Email is not present which is mandatory field")
    else:
        send_keys(driver , locator_value=email_textbox_xpath , xpath=True , locator_name="Email input text" , text=email_data)
    
    # password
    if password_data != "":
        send_keys(driver , locator_value=password_textbox_xpath , xpath=True , locator_name="Password input text" , text=password_data)
        send_keys(driver , locator_value=confirmPassword_textbox_xpath , xpath=True , locator_name="Confirm Password input text" , text=password_data)
    
    # Check the terms and cond and click on register
    delay()
    click(driver , locator_value=term_condition_checkbox_id , locator_name="Terms and Cond Check box" , id = True)
    click(driver , locator_value=register_submit_button_id , locator_name="Regiter User button" , id = True)

unternehmensverzeichnis(driver)