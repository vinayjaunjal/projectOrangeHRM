import time


from pageObjects.LoginPage import Login

from utilities.readproperties import ReadValue


class Test_Url_Login:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()

    def test_Url_001(self, setup):
        self.driver = setup
        time.sleep(2)
        if self.driver.title == "OrangeHRM":
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\ProjectOrangeHRM\\Screenshots\\test_Url_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\ProjectOrangeHRM\\Screenshots\\test_Url_001_fail.png")
            assert False

    def test_login_002(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(self.username)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        if self.lp.login_status() == True:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\ProjectOrangeHRM\\Screenshots\\test_login_002_pass.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_logout_Button()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\ProjectOrangeHRM\\Screenshots\\test_login_002_fail.png")
            assert False
