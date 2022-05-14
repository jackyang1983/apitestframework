import json

import requests
import json

from common.request_util import RequestUtil


class TestLogin:

    def test_01_login(self):
        data = {
            "j_username": "admin",
            "j_password": "admin",
            "from": "%2F",
            "Submit": "%E7%99%BB%E5%BD%95"
        }
        res0 = RequestUtil().send_request(method="get", url="http://localhost:8080/login?from=%2F")
        res1 = RequestUtil().send_request(method="post", url="http://localhost:8080/j_spring_security_check", data=data)
        print(res0.status_code)
        print(res1.)
