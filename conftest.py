import pytest
import methods.query_body as payload
from methods.methods import Methods
import config_parser as conf







@pytest.fixture(scope="function")
def generateNewPaymentUser():
    m = Methods()
    email = m.random_payment_email()
    print(email)
    body = payload.registration_body(email)
    response = m.post_for_generation_new_user(body)
    token = response.cookies.get(name='ACCESSTOKEN')
    x_token = response.json()["data"]["userRegistration"]["viewer"]["xsrfToken"]
    headers = {
        'CLIENT': conf.get_client(),
        'PRETTYERRORS': '1',
        'Content-Type': 'application/json',
        'ACCESSTOKEN': token,
        'x-xsrf-token': x_token,
        'CF-Access-Client-Id': conf.cf_access_client_id,
        'CF-Access-Client-Secret': conf.cf_access_client_secret

    }
    return headers


