import requests
import os
import random
import json
import config_parser as conf
import allure



class Methods:
    server = os.getenv('SERVER', "")
    def set_headers(self,accessToken,x_token):
        headers = {
            'CF-Access-Client-Id': conf.cf_access_client_id,
            'CF-Access-Client-Secret': conf.cf_access_client_secret,
            'CLIENT': conf.get_client(),
            'PRETTYERRORS': '1',
            'Content-Type': 'application/json',
            'ACCESSTOKEN': conf.get_accesstoken(accessToken),
            'x-xsrf-token': conf.get_x_token(x_token)

        }
        return headers

    headers_base = {
        'CLIENT': conf.get_client(),
        'PRETTYERRORS': '1',
        'Content-Type': 'application/json',
        'CF-Access-Client-Id': conf.cf_access_client_id,
        'CF-Access-Client-Secret': conf.cf_access_client_secret

    }



    headers_new_user = {
        'CLIENT': '{"id":"android.mtvl.def","dtype":"phone","lang":"en_US","metric":"1","ccode":"BYR","locale":"en_US","os":"macos","osv":"10.12.2","did":"EFFBBF4C-96EC-42D7-87B3-F37B77D2F210","dname":"iPhone 6 Plus","decsep":".","csymbol":".","net":"wi-fi","screen":"400x500","timezone":"Europe/Minsk","push":"1","buildv":"6.18.5"}',
        'PRETTYERRORS': '1',
        'Content-Type': 'application/json',
        'CF-Access-Client-Id': conf.cf_access_client_id,
        'CF-Access-Client-Secret': conf.cf_access_client_secret

    }

    base_url = conf.get_base_url()
    email = conf.get_email('email')
    password = conf.get_password()


    @allure.step
    def send_post(self, payload, headers):
        body = json.dumps(payload)
        result = requests.post(self.base_url + '/graphql',
                               data=body,
                               headers=headers,
                               )
        print(self.base_url + '/graphql')
        return result





    @allure.step
    def post_buy_vip(self, payload, headers):
        return self.send_post(payload, headers)

    @allure.step
    def post(self, payload):
        headers = self.set_headers('accessToken', 'x-xsrf-token')
        return self.send_post(payload, headers)


    @allure.step
    def post_for_generation_new_user(self, payload):
        headers = self.headers_base
        return self.send_post(payload, headers)




    @allure.step
    def random_email(self):
        value = random.randint(20, 100000)
        return "test.autotester" + str(value) + "@yopmail.com"

    @allure.step
    def random_payment_email(self):
        value = random.randint(20, 100000)
        return "test.payments.autotest." + str(value) + "@yopmail.com"





