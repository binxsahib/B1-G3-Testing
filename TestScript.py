import random
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.common.by import By

rand = random.randint(0, 100)
report = Report()

# driver = webdriver.Edge(executable_path="D:\\PyProjects\\WebDrivers\\edgedriver_win64\\msedgedriver.exe")

driver = webdriver.Edge(
    executable_path="D:\\PyProjects\\WebDrivers\\edgedriver_win64\\msedgedriver.exe")
report.setup(
    report_folder=r'Reports',
    module_name='Device',
    release_name='Test V1',
    selenium_driver=driver
)

driver.get('http://127.0.0.1:8000/')

# Test Case 1

try:
    report.write_step(
        'Go To Register Page',
        status=report.status.Start,
        test_number=1
    )

    # / html / body / header / ul / li[2] / a
    login = driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
    #login = driver.find_element_by_name("signup").click()
    results = driver.current_url
    assert "http://127.0.0.1:8000/register/" == results
    time.sleep(2)
    report.write_step(
        'Successfully Open to the Registration Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Open Registration Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 2

# driver.get('http://127.0.0.1:8000/')

try:
    report.write_step(
        'Register',
        status=report.status.Start,
        test_number=2
    )

    # / html / body / header / ul / li[2] / a
    # driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('zionBaba')
    driver.find_element(By.XPATH, '//*[@id="id_first_name"]').send_keys('Zion')
    driver.find_element(By.XPATH, '//*[@id="id_last_name"]').send_keys('Baba')
    driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys('zion@uap-bd.edu')
    driver.find_element(By.XPATH, '//*[@id="id_password1"]').send_keys('booleanFlag0')
    driver.find_element(By.XPATH, '//*[@id="id_password2"]').send_keys('booleanFlag0')
    driver.find_element(By.XPATH, '//*[@id="register"]/form/button').click()
    #login = driver.find_element_by_name("signup").click()
    assert driver.title == 'Welcome To My Shop'
    time.sleep(2)
    report.write_step(
        'Successfully Registered',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Register',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 3

try:
    report.write_step(
        'Profile',
        status=report.status.Start,
        test_number=3
    )

    driver.find_element(By.XPATH,"//a[contains(text(),'Profile')]").click()
    assert driver.title == 'Title'
    time.sleep(2)
    report.write_step(
        'Profile Visited',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to load Profile',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


# Test Case 4

try:
    report.write_step(
        'Back to the Home',
        status=report.status.Start,
        test_number=4
    )

    driver.back()
    assert driver.title == 'Welcome To My Shop'
    time.sleep(2)
    report.write_step(
        'Back in Home',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to load Home',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 5

try:
    report.write_step(
        'Product Landing Page',
        status=report.status.Start,
        test_number=5
    )

    driver.find_element(By.XPATH,"//a[contains(text(),'Product')]").click()
    assert driver.title == 'Title'
    time.sleep(2)
    report.write_step(
        'Product Landing Page Showed',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to load Product Landing Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 6

try:
    report.write_step(
        'Back to the Home',
        status=report.status.Start,
        test_number=6
    )

    driver.back()
    assert driver.title == 'Welcome To My Shop'
    time.sleep(2)
    report.write_step(
        'Back to the Home Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to load Home Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )


# Test Case 7

try:
    report.write_step(
        'Change Password',
        status=report.status.Start,
        test_number=7
    )

    driver.find_element(By.XPATH, "//a[contains(text(),'Change Password')]").click()
    driver.find_element(By.XPATH, '//*[@id="id_old_password"]').send_keys('booleanFlag0')
    driver.find_element(By.XPATH, '//*[@id="id_new_password1"]').send_keys('booleanFlag1')
    driver.find_element(By.XPATH, '//*[@id="id_new_password2"]').send_keys('booleanFlag1')
    driver.find_element(By.XPATH, '//*[@id="password-change"]/form/button').click()
    time.sleep(4)

    report.write_step(
        'Password Changed',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error while changing password',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 8

try:
    report.write_step(
        'Log Out',
        status=report.status.Start,
        test_number=8
    )

    driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/logout/"
    time.sleep(2)

    report.write_step(
        'Logged Out',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error while logging out',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 9

try:
    report.write_step(
        'Home PAGE',
        status=report.status.Start,
        test_number=9
    )

    driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/"
    time.sleep(2)

    report.write_step(
        'Home Page Loaded',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error while loading Home Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 10

try:
    report.write_step(
        'Password Reset',
        status=report.status.Start,
        test_number=10
    )

    driver.find_element(By.XPATH, "//a[contains(text(),'Password Reset')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/password-reset/"
    time.sleep(2)

    report.write_step(
        'Password Reset Page Landed',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error while loading password reset page loading',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 11

try:
    report.write_step(
        'Password Reset Attempt',
        status=report.status.Start,
        test_number=11
    )

    driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys('jacob@uap-bd.edu')
    driver.find_element(By.XPATH, '//*[@id="password-change"]/form/button').click()
    assert driver.current_url == "http://127.0.0.1:8000/password-reset/done/"
    time.sleep(2)

    report.write_step(
        'Password Reset Success!',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error!',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 12
driver.get('http://127.0.0.1:8000/')

try:
    report.write_step(
        'Go to Log In Page',
        status=report.status.Start,
        test_number=12
    )

    # / html / body / header / ul / li[2] / a
    driver.find_element(By.XPATH,"//a[contains(text(),'Log In')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/login/"
    time.sleep(2)
    report.write_step(
        'Successfully Open to the Log In Page',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Failed to Open Log-In Page',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 13

try:
    report.write_step(
        'Log In with New Pass',
        status=report.status.Start,
        test_number=13
    )

    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('zionBaba')
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('booleanFlag1')
    driver.find_element(By.XPATH, '//*[@id="login"]/form/button').click()
    assert driver.current_url == "http://127.0.0.1:8000/"
    time.sleep(2)

    report.write_step(
        'Log In Success!',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error!',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Test Case 14

try:
    report.write_step(
        'Exit',
        status=report.status.Start,
        test_number=14
    )

    driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()
    assert driver.current_url == "http://127.0.0.1:8000/logout/"
    time.sleep(2)

    report.write_step(
        'Exit Success!',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Error!',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status=report.status.Warn,
        screenshot=True
    )

# Report Generation
report.generate_report()
driver.quit()

print("Device Rental System Testing Completed.")