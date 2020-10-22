# -*- coding:utf-8 -*-

import requests
import json
import pytest
from loguru import logger
import os
import allure

class Test_Mobile():

    # 封装公共数据
    def common(self, phone):
        url = "http://apis.juhe.cn/mobile/get"
        data = {
            "key" : "4391b7dd8213662798c3ac3da9f54ca8",
            "phone" : phone
        }
        res = requests.get(url=url, params=data).json()
        allure.attach("附加内容: " + str(res))
        return res


    @allure.feature("手机号码归属地")
    def test_2(self):
        assert self.common("18844077709")['resultcode'], "200"


if __name__ == '__main__':
    # pytest.main(["-sv", "common_data.py"])
    pytest.main(['-s', 'common_data.py', '--alluredir', './temp'])
    os.system('allure generate ./temp -o ./report --clean')