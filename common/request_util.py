import json
import requests


class RequestUtil:

    ses = requests.session()

    def send_request(self, method, url, data=None, **kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            res = self.ses.request(method=method, url=url, params=data, **kwargs)
        elif method == "post":
            if data:
                data = json.dumps(data)
            res = self.ses.request(method=method, url=url, data=data, **kwargs)
        else:
            pass
        return res
