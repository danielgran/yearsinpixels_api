from urllib.parse import urlencode
from urllib.request import urlopen
import json

API_URL = "https://www.google.com/recaptcha/api/siteverify"


class GoogleCaptcha:
    """Verifies an google captcha works as well with v2 and v3 but for testing i will choose v2"""
    def __init__(self, secret):
        self.secret = secret

    def verify_captcha(self, token):
        params = urlencode({
            'secret': self.secret,
            'response': token
        })
        # print params
        data = urlopen(API_URL, params.encode('utf-8')).read()
        result = json.loads(data)
        success = result.get('success')

        if success:
            return True
        else:
            return False