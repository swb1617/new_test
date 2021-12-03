"""
user:石文斌
time：2021/11/15

"""
import time
import unittest
from button import *
from appium import webdriver


class test_DATA(unittest.TestCase):

    def setUp(self) -> None:  # 执行方法前准备工作
        self.driver.implicitly_wait(15)  # 稳定元素
        print("...........开始.............")

    def tearDown(self) -> None:  # 执行方法后工作
        print("...........结束..............")

    @classmethod
    def setUpClass(cls) -> None:  # 执行测试类前准备工作
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'test01',
            'appPackage': 'com.igpsport.globalapp',
            'appActivity': 'com.igpsport.globalapp.activity.v3.SplashActivity',
            'noReset': True,
            'newCommandTimeout': 6000,
            # 更换底层驱动
            'automationName': 'UiAutomator2',
            'unicodeKeyboard': True,  # 修改手机的输入法
            'resetKeyboard': True
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def SwipeDown(self):  # 定义下滑动方法
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.5
        y1, y2 = height * 0.35, height * 0.7
        time.sleep(3)
        self.driver.swipe(x1, y1, x2, y2, 1000)

    def SwipeUp(self):  # 定义上滑动方法
        size = self.driver.get_window_size()  # 获取手机屏幕尺寸
        width = size['width']
        height = size['height']
        x1 = x2 = width * 0.5
        y1, y2 = height * 0.89, height * 0.86
        time.sleep(3)
        self.driver.swipe(x1, y1, x2, y2, 1000)  # 滑动方法

    def test_MenuMessage(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuMessageInto(self).click()
        Message.GetMessageRead(self).click()
        Message.GetMeaagaeBack(self).click()

    def test_MenuGoals(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuTrainingGoalsInto(self).click()
        Me.GetMeUserGoalsText(self).click()
        Me.GetMeUserGoalsSave(self).click()
        Me.GetMeUserDetailsBack(self).click()

    def test_ChangeMapStyle(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataMapStyleInto(self).click()
        Data.GetDataMapStyleMode(self).click()
        Data.GetDataMapStyleSave(self).click()
        Data.GetDataBack(self).click()

    def test_OpenMapGoals(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataMapStyleInto(self).click()
        Data.GetDataMapStyleGoals(self).click()
        Data.GetDataMapStyleSave(self).click()
        Data.GetDataBack(self).click()

    def test_SaveMyLine(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataMenuInfo(self).click()
        Data.GetDataMenuToSaveMyLine(self).click()
        time.sleep(3)
        Data.GetDataBack(self).click()

    @unittest.skip("部分手机保存活动不同")
    def test_ExportData(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataMenuInfo(self).click()
        Data.GetDataMenuToExportFile(self).click()
        Data.GetDataExportDataTcx(self).click()
        Data.GetDataExportDataDowload(self).click()
        Data.GetDataExportDataSave(self).click()  # 荣耀手机的view
        time.sleep(3)
        Data.GetDataExportDataBack(self).click()
        Data.GetDataBack(self).click()

    def test_DataEdit(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataMenuInfo(self).click()
        Data.GetDataMenuToEditActivity(self).click()
        Data.GetDataEditText(self).click()
        Data.GetDataEditSave(self).click()
        Data.GetDataBack(self).click()

    @unittest.skip("删除数据")
    def test_DeleteData(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataMenuInfo(self).click()
        Data.GetDataMenuToDeleteData(self).click()
        Data.GetDataDeleteDataOk(self).click()
        time.sleep(3)

    def test_ShareWatermark(self):
        Tap.GetToHome(self).click()
        Menu.GetMenuFirstData(self).click()
        time.sleep(3)
        Data.GetDataShare(self).click()
        time.sleep(1)
        Data.GetDataShareWatermarkPhoto(self).click()
        Data.GetDataWatermarkPhotoTrack(self).click()
        Data.GetDataWatermarkPhotoAlt(self).click()
        Data.GetDataWatermarkPhotoData(self).click()
        Data.GetDataWatermarkPhotoBack(self).click()
        Data.GetDataShareBack(self).click()
        Data.GetDataBack(self).click()

    def test_Calendar(self):
        Tap.GetToActivity(self).click()
        Activity.GetActivityCalendarInfo(self).click()
        Activity.GetActivityCalendarBack(self).click()

    def test_ActivityShare(self):
        Tap.GetToActivity(self).click()
        Activity.GetActivityShareInfo(self).click()
        time.sleep(1)
        Activity.GetActivityShareSave(self).click()
        Activity.GetActivityShareBack(self).click()

    def test_StatisicData(self):
        Tap.GetToActivity(self).click()
        Activity.GetActivityDataStatisicInfo(self).click()
        time.sleep(1)
        Activity.GetActivityDataStatisicBack(self).click()

    def test_PersonalRecords(self):
        Tap.GetToActivity(self).click()
        Activity.GetActivityPersonalRecordsInfo(self).click()
        Activity.GetActivityPersonalRecordsShare(self).click()
        Activity.GetActivityPersonalRecordsShareBack(self).click()
        Activity.GetActivityPersonalRecordsBack(self).click()

    def test_MeSettingHR(self):
        Tap.GetToMe(self).click()
        Me.GetMEUserDetailsInfo(self).click()
        Me.GetMeSettingHRInfo(self).click()
        Me.GetMeSettingHR(self).click()
        Me.GetMeSettingHRBack(self).click()
        Me.GetMeUserDetailsBack(self).click()

    def test_MeSettingPower(self):
        Tap.GetToMe(self).click()
        Me.GetMEUserDetailsInfo(self).click()
        Me.GetMeSettingPowerInfo(self).click()
        Me.GetMeSettingPower(self).click()
        Me.GetMeSettingPowerBack(self).click()
        Me.GetMeUserDetailsBack(self).click()

    def test_AboutUs(self):
        Tap.GetToMe(self).click()
        Me.GetMeAboutUs(self).click()
        time.sleep(3)
        Me.GetMeAboutUsBack(self).click()

    def test_FeedBack(self):
        QuestionName = 'test'
        Tap.GetToMe(self).click()
        Me.GetMeAfterSaleServiceInfo(self).click()
        time.sleep(2)
        Me.GetMeAfterSaleServiceFeedBack(self).click()
        time.sleep(1)
        Me.GetMeFeedBackQuestionType(self).click()
        Me.GetMeFeedBackQuestionList(self).click()
        Me.GetMeFeedBackQuestionText(self).click()
        Me.GetMeFeedBackQuestionText(self).send_keys(QuestionName)
        time.sleep(1)
        Me.GetMeFeedBackTLEText(self).send_keys(123456)
        time.sleep(1)
        Me.GetMeFeedBackPictureAdd(self).click()
        time.sleep(1)
        Me.GetMeFeedBackPictureChoose(self).click()
        time.sleep(1)
        Me.GetMeFeedBackPictureSave(self).click()
        time.sleep(1)
        Me.GetMeFeedBackSubmit(self).click()
        time.sleep(1)
        Me.GetMeAfterSaleServiceBack(self).click()

    def test_ActivityChangeGoals(self):
        MonthlyGoals = 520
        Tap.GetToActivity(self).click()
        Activity.GetActivityCalendarInfo(self).click()
        Activity.GetActivityCalendarGoalsEdit(self).click()
        Activity.GetActivityCalendarGoalsEditText(self).click()
        Activity.GetActivityCalendarGoalsEditText(self).clear()
        Activity.GetActivityCalendarGoalsEditText(self).send_keys(MonthlyGoals)
        Activity.GetActivityCalendarGoalsEditSave(self).click()
        Activity.GetActivityCalendarBack(self).click()

    @unittest.skip("compose测试")
    def test_ComposeTest(self):
        Tap.GetToDevice(self).click()
        ComposeTest.GetDeviceRoutesAdd(self).click()
        time.sleep(3)
        # Compose.GetDeviceCreateRoutes(self).click()
        ComposeTest.GetDeviceFirstRoutes(self).click()

    def test_MenuChangeGoals(self):
        MonthlyGoals = 888
        Tap.GetToHome(self).click()
        OldGoals = Menu.GetMenuMonthGoals(self).text
        Menu.GetMenuTrainingGoalsInto(self).click()
        Me.GetMeUserGoalsText(self).click()
        Me.GetMeUserGoalsText(self).clear()
        Me.GetMeUserGoalsText(self).send_keys(MonthlyGoals)  # id定位
        Me.GetMeUserGoalsSave(self).click()
        Me.GetMeUserDetailsBack(self).click()
        NewGoals = Menu.GetMenuMonthGoals(self).text
        RealGoals = OldGoals - NewGoals
        print(RealGoals)
        # self.assertEqual()

    def test_MeChangeGoals(self):
        MonthlyGoals = 666
        Tap.GetToMe(self).click()
        Me.GetMEUserDetailsInfo(self).click()
        Me.GetMeUserGoalsEdit(self).click()
        Me.GetMeUserGoalsText(self).click()
        Me.GetMeUserGoalsText(self).clear()
        Me.GetMeUserGoalsText(self).send_keys(MonthlyGoals)  # id定位
        Me.GetMeUserGoalsSave(self).click()
        Me.GetMeUserDetailsBack(self).click()

    def test_LanguageChange(self):
        Tap.GetToMe(self).click()
        Me.GetMeAccountSettingInfo(self).click()
        Me.GetMeLanguageSetting(self).click()
        self.SwipeUp()
        time.sleep(1)
        Me.GetMeLanguageSettingSave(self).click()
        OldLanguage = Me.GetMeLanguageMessage(self).text
        Me.GetMeAccountSettingSave(self).click()
        Tap.GetToMe(self).click()
        Me.GetMeAccountSettingInfo(self).click()
        NewLanguage = Me.GetMeLanguageMessage(self).text
        Me.GetMeAccountSettingBack(self).click()
        self.assertEqual(OldLanguage, NewLanguage)

    def test_MeNotification(self):
        Tap.GetToMe(self).click()
        Me.GetMeNotification(self).click()
        time.sleep(3)
        Me.GetMeNotificationBack(self).click()


if __name__ == '__main__':
    unittest.main()
