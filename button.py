from appium import webdriver
from selenium.webdriver.common.by import By


class Menu:

    def GetMenuTitle(self):  # 首页标题
        MenuTitle = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout[ "
                                                                "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                                                "1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
        return MenuTitle

    def GetMenuMessageInto(self):  # 首页消息按钮
        MessageInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout[ "
                                                                  "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]")
        return MessageInto

    def GetMenuFriendInto(self):  # 首页好友按钮
        FriendInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.view.ViewGroup[2]")
        return FriendInto

    def GetMenuTrainingGoalsInto(self):  # 首页修改训练按钮
        TrainingGoalsInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.view.ViewGroup["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout[1]")
        return TrainingGoalsInto

    def GetMenuMonthGoals(self):  # 首页月骑行目标数据（float）
        MonthGoals = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.TextView[4]")
        return MonthGoals

    def GetMenuFirstData(self):  # 首页第一天数据
        FirstData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "2]/android.widget.FrameLayout["
                                                                "1]/androidx.recyclerview.widget.RecyclerView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return FirstData

    def GetMenuSecondData(self):  # 首页第二条数据
        SecondData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "2]/android.widget.FrameLayout["
                                                                 "1]/androidx.recyclerview.widget.RecyclerView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "2]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.LinearLayout[1]")
        return SecondData

    def GetMenuThirData(self):  # 首页第三条数据
        ThirdData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "2]/android.widget.FrameLayout["
                                                                "1]/androidx.recyclerview.widget.RecyclerView["
                                                                "1]/android.widget.LinearLayout["
                                                                "3]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout[1]")
        return ThirdData

    def GetMenuFirstTraining(self):  # 首页第一条训练
        FirstTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.view.ViewGroup["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "2]/android.widget.FrameLayout["
                                                                    "1]/androidx.recyclerview.widget.RecyclerView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.LinearLayout[1]")
        return FirstTraining

    def GetMenuSecondTraining(self):  # 首页第二条训练
        SecondTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.FrameLayout["
                                                                     "1]/androidx.recyclerview.widget.RecyclerView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.RelativeLayout["
                                                                     "1]/android.widget.LinearLayout[1]")
        return SecondTraining

    def GetMenuThirdTraining(self):  # 首页第三条训练
        ThirdTraining = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.view.ViewGroup["
                                                                    "1]/android.widget.ScrollView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "2]/android.widget.FrameLayout["
                                                                    "1]/androidx.recyclerview.widget.RecyclerView["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "3]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.LinearLayout[1]")
        return ThirdTraining


class Message:
    def GetMeaagaeBack(self):  # 消息页返回按钮
        MessageBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.LinearLayout[1]")
        return MessageBack

    def GetMessageRead(self):  # 信息已读按钮
        MessageRead = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.RelativeLayout["
                                                                  "1]/android.widget.RelativeLayout[1]")
        return MessageRead


class Data:
    def GetDataBack(self):  # 详情页返回按钮
        DataBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout[1]")
        return DataBack

    def GetDataShare(self):  # 详情也分享按钮
        DataShare = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.RelativeLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.ImageView[2]")
        return DataShare

    def GetDataShareBack(self):  # 详情页分享返回按钮
        DataShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.ImageView[1]")
        return DataShareBack

    def GetDataShareWatermarkPhoto(self):  # 详情页分享水印照片按钮
        DataShareWatermarkPhoto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout[2]")
        return DataShareWatermarkPhoto

    def GetDataWatermarkPhotoBack(self):  # 水印照片返回按钮
        DataWatermarkPhotoBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return DataWatermarkPhotoBack

    def GetDataWatermarkPhotoData(self):  # 水印照片第一tap
        DataWatermarkPhotoData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.HorizontalScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return DataWatermarkPhotoData

    def GetDataWatermarkPhotoAlt(self):  # 水印照片第二tap
        DataWatermarkPhotoAlt = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.ScrollView["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.HorizontalScrollView["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout[2]")
        return DataWatermarkPhotoAlt

    def GetDataWatermarkPhotoTrack(self):  # 水印照片第三tap
        DataWatermarkPhotoTrack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.FrameLayout["
                                                                              "1]/android.widget.ScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.HorizontalScrollView["
                                                                              "1]/android.widget.LinearLayout["
                                                                              "1]/android.widget.LinearLayout[3]")
        return DataWatermarkPhotoTrack

    def GetDataMenuInfo(self):  # 详情页菜单按钮
        DataMenuInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.ImageView[3]")
        return DataMenuInfo

    def GetDataName(self):  # 详情页数据名称
        DataName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "2]/android.widget.LinearLayout["
                                                               "2]/android.widget.TextView[2]")
        return DataName

    def GetDataDistance(self):  # 详情页里程
        DataDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.ScrollView["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "2]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/androidx.recyclerview.widget.RecyclerView["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.TextView[1]")
        return DataDistance

    def GetDataMapStyleInto(self):  # 详情页切换地图样式按钮
        DataMapStyleInto = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.ImageView[1]")
        return DataMapStyleInto

    def GetDataMapStyleMode(self):  # 地图样式Dark
        DataMapStyleMode = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "4]/android.widget.ImageView[1]")
        return DataMapStyleMode

    def GetDataMapStyleSave(self):  # 保存地图样式
        DataMapStyleSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.Button[1]")
        return DataMapStyleSave

    def GetDataMapStyleGoals(self):  # 公里点打开关闭按钮
        DataMapStyleGoals = self.driver.find_element(by=By.XPATH,
                                                     value="//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Switch[1]")
        return DataMapStyleGoals

    def GetDataMenuToEditActivity(self):  # 修改活动名称
        DataEditActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.TextView[1]")
        return DataEditActivity

    def GetDataMenuToSaveMyLine(self):  # 保存到我的线路
        DataMenuToSaveMyLine = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[2]")
        return DataMenuToSaveMyLine

    def GetDataMenuToSendFriend(self):  # 发送给好友
        DataMenuToSendFriend = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[3]")
        return DataMenuToSendFriend

    def GetDataMenuToExportFile(self):  # 保存数据到文件
        DataMenuToExportFile = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[4]")
        return DataMenuToExportFile

    def GetDataMenuToDeleteData(self):  # 删除数据按钮
        DataMenuToDeleteData = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.TextView[5]")
        return DataMenuToDeleteData

    def GetDataEditText(self):  # 数据修改名字文本框
        DataEditActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.RelativeLayout[2]")
        return DataEditActivity

    def GetDataEditSave(self):  # 数据修改名字保存
        DataEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.view.ViewGroup["
                                                                   "1]/android.widget.FrameLayout["
                                                                   "1]/android.widget.LinearLayout["
                                                                   "1]/android.widget.RelativeLayout["
                                                                   "1]/android.widget.TextView[3]")
        return DataEditSave

    def GetDataSendToFriendText(self):  # 好友id输入框
        DataSendToFriendText = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout[1]")
        return DataSendToFriendText

    def GetDataSendToFriend(self):  # 发送给好友按钮
        DataSendToFriend = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/androidx.recyclerview.widget.RecyclerView["
                                                                       "1]/android.widget.RelativeLayout["
                                                                       "1]/android.widget.TextView[2]")
        return DataSendToFriend

    def GetDataSendMessageBack(self):  # 消息界面返回
        DataSendMessageBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.FrameLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.view.ViewGroup["
                                                                          "1]/androidx.recyclerview.widget"
                                                                          ".RecyclerView["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "1]/android.widget.LinearLayout["
                                                                          "2]/android.widget.RelativeLayout["
                                                                          "1]/android.widget.LinearLayout[1]")
        return DataSendMessageBack

    def GetDataSendMessageFriendName(self):  # 消息界面好友的名字
        DataSendMessageFriendName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout[1]")
        return DataSendMessageFriendName

    def GetDataSendFriendName(self):  # 发送给好友的名字
        DataSendFriendName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
        return DataSendFriendName

    def GetDataExportDataBack(self):  # 数据导出返回
        DataExportDataBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return DataExportDataBack

    def GetDataExportDataFit(self):  # fit文件格式
        DataExportDataFit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return DataExportDataFit

    def GetDataExportDataGpx(self):  # gpx格式
        DataExportDataGpx = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "2]/android.widget.LinearLayout[1]")
        return DataExportDataGpx

    def GetDataExportDataTcx(self):  # 数据导出界面tcx文件格式
        DataExportDataTcx = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/androidx.recyclerview.widget.RecyclerView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "3]/android.widget.LinearLayout[1]")
        return DataExportDataTcx

    def GetDataExportDataDowload(self):  # 数据导出下载按钮
        DataExportDataDowload = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.Button[2]")

        return DataExportDataDowload

    def GetDataExportDataSave(self):  # 数据导出保存
        DataExportDataSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/androidx.drawerlayout.widget"
                                                                         ".DrawerLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "2]/android.widget.Button[1]")
        return DataExportDataSave

    def GetDataDeleteDataOk(self):
        DataDeleteDataOk = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "2]/android.widget.Button[2]")
        return DataDeleteDataOk


class Activity:
    def GetActivityTotalDistance(self):  # 活动界面总计里程
        ActivityTotalDistance = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.TextView[1]")
        return ActivityTotalDistance

    def GetActivityCalendarInfo(self):  # 活动界面日历入口
        ActivityCalendarInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return ActivityCalendarInfo

    def GetActivityShareInfo(self):  # 活动界面分享入口
        ActivityShareInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[2]")
        return ActivityShareInfo

    def GetActivityDataStatisicInfo(self):  # 活动界面数据管理入口
        ActivityDataStatisicInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "3]/android.widget.LinearLayout[1]")
        return ActivityDataStatisicInfo

    def GetActivityDataStatisicBack(self):  # 活动界面数据管理入口
        ActivityDataStatisicBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.FrameLayout["
                                                                               "1]/android.widget.LinearLayout["
                                                                               "1]/android.widget.RelativeLayout["
                                                                               "1]/android.widget.LinearLayout[1]")
        return ActivityDataStatisicBack

    def GetActivityPersonalRecordsInfo(self):  # 活动界面个人记录入口
        ActivityPersonalRecordsInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "3]/android.widget.LinearLayout[2]")
        return ActivityPersonalRecordsInfo

    def GetActivityCalendarBack(self):  # 日历界面返回
        ActivityCalendarBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return ActivityCalendarBack

    def GetActivityCalendarGoalsEdit(self):  # 编辑月骑行目标按钮
        ActivityCalendarGoalsEdit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.FrameLayout["
                                                                                "1]/android.widget.LinearLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.RelativeLayout["
                                                                                "1]/android.widget.RelativeLayout[1]")
        return ActivityCalendarGoalsEdit

    def GetActivityCalendarGoalsEditText(self):  # 骑行目标输入框
        ActivityCalendarGoalsEditText = self.driver.find_element(by=By.ID, value="com.igpsport.globalapp:id/et_goal")
        return ActivityCalendarGoalsEditText

    def GetActivityCalendarGoalsEditSave(self):  # 骑行目标保存
        ActivityCalendarGoalsEditSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.FrameLayout["
                                                                                    "1]/android.widget.RelativeLayout["
                                                                                    "1]/android.widget.Button[1]")
        return ActivityCalendarGoalsEditSave

    def GetActivityShareBack(self):  # 活动界面分享返回
        ActivityShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareBack

    def GetActivityShareSave(self):  # 活动界面分享保存
        ActivityShareSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return ActivityShareSave

    def GetActivityPersonalRecordsBack(self):  # 个人纪录返回
        ActivityPersonalRecordsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.FrameLayout["
                                                                                  "1]/android.widget.LinearLayout["
                                                                                  "1]/android.widget.RelativeLayout["
                                                                                  "1]/android.widget.LinearLayout[1]")
        return ActivityPersonalRecordsBack

    def GetActivityPersonalRecordsShare(self):  # 个人记录分享
        ActivityPersonalRecordsShare = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.FrameLayout["
                                                                                   "1]/android.widget.LinearLayout["
                                                                                   "1]/android.widget.RelativeLayout["
                                                                                   "1]/android.widget.RelativeLayout["
                                                                                   "1]")
        return ActivityPersonalRecordsShare

    def GetActivityPersonalRecordsShareBack(self):  # 个人记录分享返回
        ActivityPersonalRecordsShareBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget.FrameLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout["
                                                                                       "1]/android.widget"
                                                                                       ".RelativeLayout["
                                                                                       "1]/android.widget"
                                                                                       ".LinearLayout[1]")
        return ActivityPersonalRecordsShareBack


class Tap:
    def GetToHome(self):
        ToHome = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout["
                                                             "1]/android.widget.LinearLayout["
                                                             "1]/android.widget.FrameLayout[2]/android.view.ViewGroup["
                                                             "1]/android.widget.FrameLayout[1]")
        return ToHome

    def GetToActivity(self):
        ToActivity = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "2]/android.view.ViewGroup["
                                                                 "1]/android.widget.FrameLayout[2]")
        return ToActivity

    def GetToDevice(self):
        ToDevice = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "2]/android.view.ViewGroup["
                                                               "1]/android.widget.FrameLayout[3]")
        return ToDevice

    def GetToMe(self):
        ToMe = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout["
                                                           "1]/android.widget.LinearLayout["
                                                           "1]/android.widget.FrameLayout[2]/android.view.ViewGroup["
                                                           "1]/android.widget.FrameLayout[4]")
        return ToMe


class Me:
    def GetMeUserName(self):
        MeUserName = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.FrameLayout["
                                                                 "1]/android.view.ViewGroup["
                                                                 "1]/android.widget.ScrollView["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.RelativeLayout["
                                                                 "1]/android.widget.LinearLayout["
                                                                 "1]/android.widget.TextView[1]")
        return MeUserName

    def GetMeUserId(self):
        MeUserId = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.FrameLayout[1]/android.view.ViewGroup["
                                                               "1]/android.widget.ScrollView["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.RelativeLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.LinearLayout["
                                                               "1]/android.widget.TextView[2]")
        return MeUserId

    def GetMEUserDetailsInfo(self):
        MeUserDetailsInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.view.ViewGroup["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return MeUserDetailsInfo

    def GetMeSettingHRInfo(self):
        MeSettingHRInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout[8]")
        return MeSettingHRInfo

    def GetMeSettingHR(self):
        MeSettingHR = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.FrameLayout["
                                                                  "1]/android.widget.LinearLayout["
                                                                  "2]/android.widget.RelativeLayout["
                                                                  "2]/android.widget.Button[1]")
        return MeSettingHR

    def GetMeSettingHRBack(self):
        MeSettingHRBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.LinearLayout[1]")
        return MeSettingHRBack

    def GetMeSettingPowerInfo(self):
        MeSettingPowerInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.ScrollView["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout[9]")
        return MeSettingPowerInfo

    def GetMeSettingPower(self):
        MeSettingPower = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "2]/android.widget.RelativeLayout["
                                                                     "2]/android.widget.Button[1]")
        return MeSettingPower

    def GetMeSettingPowerBack(self):
        MeSettingPowerBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return MeSettingPowerBack

    def GetMeAccountSettingInfo(self):
        MeAccountSettingInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.view.ViewGroup["
                                                                           "1]/android.widget.ScrollView["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "3]/android.widget.RelativeLayout[2]")
        return MeAccountSettingInfo

    def GetMeLanguageMessage(self):
        MeLanguageMessage = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.TextView[2]")
        return MeLanguageMessage

    def GetMeRidingRankInfo(self):
        MeRidingRankInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.view.ViewGroup["
                                                                       "1]/android.widget.ScrollView["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "3]/android.widget.RelativeLayout[3]")
        return MeRidingRankInfo

    def GetMeAfterSaleServiceInfo(self):
        MeAfterSaleServiceInfo = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.view.ViewGroup["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "3]/android.widget.RelativeLayout[4]")
        return MeAfterSaleServiceInfo

    def GetMeNotification(self):
        MeNotification = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.FrameLayout["
                                                                     "1]/android.view.ViewGroup["
                                                                     "1]/android.widget.ScrollView["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "1]/android.widget.LinearLayout["
                                                                     "3]/android.widget.RelativeLayout[5]")
        return MeNotification

    def GetMeAboutUs(self):
        MeAboutUs = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.FrameLayout["
                                                                "1]/android.view.ViewGroup["
                                                                "1]/android.widget.ScrollView["
                                                                "1]/android.widget.LinearLayout["
                                                                "1]/android.widget.LinearLayout["
                                                                "3]/android.widget.RelativeLayout[7]")
        return MeAboutUs

    def GetMeUserDetailsBack(self):
        MeUserDetailsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout[1]")
        return MeUserDetailsBack

    def GetMeUserGoalsEdit(self):
        MeUserGoalsEdit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.ScrollView["
                                                                      "1]/android.widget.LinearLayout["
                                                                      "1]/android.widget.RelativeLayout[10]")
        return MeUserGoalsEdit

    def GetMeUserGoalsText(self):
        MeUserGoalsText = self.driver.find_element(by=By.ID, value="com.igpsport.globalapp:id/et_goal")
        return MeUserGoalsText

    def GetMeUserGoalsSave(self):
        MeUserGoalsSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.FrameLayout["
                                                                      "1]/android.widget.RelativeLayout["
                                                                      "1]/android.widget.Button[1]")
        return MeUserGoalsSave

    def GetMeAboutUsBack(self):
        MeAboutUsBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.FrameLayout["
                                                                    "1]/android.widget.LinearLayout["
                                                                    "1]/android.widget.RelativeLayout["
                                                                    "1]/android.widget.ImageView[1]")
        return MeAboutUsBack

    def GetMeNotificationBack(self):
        MeNotificationBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.LinearLayout["
                                                                         "1]/android.widget.FrameLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.RelativeLayout["
                                                                         "1]/android.widget.LinearLayout[1]")
        return MeNotificationBack

    def GetMeAfterSaleServiceBack(self):
        MeAfterSaleServiceBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.RelativeLayout["
                                                                             "1]/android.widget.LinearLayout[1]")
        return MeAfterSaleServiceBack

    def GetMeAfterSaleServiceFeedBack(self):
        MeAfterSaleServiceFeedBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.FrameLayout["
                                                                                 "1]/android.widget.RelativeLayout["
                                                                                 "1]/android.widget.LinearLayout["
                                                                                 "1]/android.widget.RelativeLayout[5]")
        return MeAfterSaleServiceFeedBack

    def GetMeFeedBackQuestionType(self):
        MeFeedBackQuestionType = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.ScrollView["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/android.widget.TextView[2]")
        return MeFeedBackQuestionType

    def GetMeFeedBackQuestionList(self):
        MeFeedBackQuestionList = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.FrameLayout["
                                                                             "1]/android.widget.LinearLayout["
                                                                             "1]/androidx.recyclerview.widget"
                                                                             ".RecyclerView["
                                                                             "1]/android.widget.LinearLayout[1]")
        return MeFeedBackQuestionList

    def GetMeFeedBackQuestionText(self):
        MeFeedBackQuestionText = self.driver.find_element(by=By.ID, value="com.igpsport.globalapp:id/etProblem")
        return MeFeedBackQuestionText

    def GetMeFeedBackTLEText(self):
        MeFeedBackTLEText = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.ScrollView["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.EditText[2]")
        return MeFeedBackTLEText

    def GetMeFeedBackSubmit(self):
        MeFeedBackSubmit = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.FrameLayout["
                                                                       "1]/android.widget.LinearLayout["
                                                                       "1]/android.widget.Button[1]")
        return MeFeedBackSubmit

    def GetMeAccountSettingBack(self):
        MeAccountSettingBack = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.LinearLayout[1]")
        return MeAccountSettingBack

    def GetMeAccountSettingSave(self):
        MeAccountSettingSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.LinearLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.FrameLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout["
                                                                           "1]/android.widget.RelativeLayout[1]")
        return MeAccountSettingSave

    def GetMeLanguageSetting(self):
        MeLanguageSetting = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.FrameLayout["
                                                                        "1]/android.widget.RelativeLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.LinearLayout["
                                                                        "1]/android.widget.RelativeLayout[1]")
        return MeLanguageSetting

    def GetMeLanguageSettingSave(self):
        MeLanguageSettingSave = self.driver.find_element(by=By.XPATH, value="//android.widget.FrameLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.FrameLayout["
                                                                            "1]/android.widget.LinearLayout["
                                                                            "1]/android.widget.RelativeLayout["
                                                                            "1]/android.widget.Button[2]")
        return MeLanguageSettingSave


class Compose:
    def GetDeviceRoutesAdd(self):
        DeviceRoutesAdd = self.driver.find_element(by=By.XPATH,
                                                   value="//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[4]")
        return DeviceRoutesAdd

    def GetDeviceCreateRoutes(self):
        DeviceCreateRoutes = self.driver.find_element(by=By.XPATH,
                                                      value="//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]")
        return DeviceCreateRoutes

    def GetDeviceFirstRoutes(self):
        DeviceFirstRoutes = self.driver.find_element(by=By.XPATH,
                                                     value="//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView[1]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]")
        return DeviceFirstRoutes
