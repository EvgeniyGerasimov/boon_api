import pprint
import methods.query_body as payload
from methods.methods import Methods
from methods.data import mutation_schema
from jsonschema import validate
import allure


@allure.feature('Test mutation')
class TestUserMutation(Methods):

    @allure.story('Test login user')
    def test_login_user(self):
        email = self.email
        body = payload.login_body(email)
        response = self.post_for_generation_new_user(body)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["generateAccessToken"]["viewer"]["profile"]["email"] == email
        assert response.json()["data"]["generateAccessToken"]["errors"] == None


    @allure.story('Test registration')
    def test_registration(self):
        email = self.random_email()
        body = payload.registration_body(email)
        response = self.post_for_generation_new_user(body)
        pprint.pprint(response.json())
        pprint.pprint(response.cookies.get(name='ACCESSTOKEN'))
        assert response.status_code == 200
        assert response.json()["data"]["userRegistration"]["viewer"]["profile"]["email"] == email
        assert response.json()["data"]["userRegistration"]["errors"] == None
        validate(instance=response.json(), schema=mutation_schema.USER_CREATED)

    @allure.story('Test user notification on')
    def test_notification_on(self):
        body = payload.NOTIFICATION_ON
        response = self.post(body)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["updateUserPreferences"]["viewer"]["profile"]["preferences"]["emailNotifications"] == True
        assert response.json()["data"]["updateUserPreferences"]["viewer"]["profile"]["preferences"]["pushNotifications"] == True
        assert response.json()["data"]["updateUserPreferences"]["errors"] == None



    @allure.story('Test user change email with incorrect data')
    def test_change_email_with_incorrect_data(self):
        email_new = 'test'
        body = payload.change_email(email_new)
        response = self.post(body)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["changeEmail"]["errors"][0]["message"] == 'Please, enter correct Email address'


    @allure.story('Test user change password')
    def test_change_password(self):
        pass_new = '11111111'
        pass_old = '11111111'
        body = payload.change_pass(pass_new, pass_old)
        response = self.post(body)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["changePassword"]["errors"] == None


    @allure.story('Test user change password with incorrect data')
    def test_change_password_with_incorrect_data(self):
        pass_new = '222222'
        pass_old = '11111111'
        body = payload.change_pass(pass_new, pass_old)
        response = self.post(body)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["changePassword"]["errors"][0]["message"] == "Use lowercase latin letters and numbers, 8-10 symbols"

    # TODO refactor test for stability
    # @allure.story('Test quiz answer  save')
    # def test_quiz_answer_save(self):
    #     body = payload.SAVE_ANSWER
    #     response = self.post(body)
    #     pprint.pprint(response.json())
    #     assert response.status_code == 200

    @allure.story('Test user buy vip')
    def test_buy_vip(self, generateNewPaymentUser):
        body = payload.BUY_VIP
        headers = generateNewPaymentUser
        response = self.post_buy_vip(body, headers)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["buyVip"]["viewer"]["profile"]["vip"]["isActive"] == True
        assert response.json()["data"]["buyVip"]["errors"] == None
        body = payload.CANSEL_VIP
        response = self.post_buy_vip(body, headers)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["cancelVip"]["errors"] == None



    @allure.story('Test user change email')
    def test_change_email(self, generateNewPaymentUser):
        email_new = self.random_email()
        body = payload.change_email(email_new)
        headers = generateNewPaymentUser
        response = self.post_buy_vip(body, headers)
        pprint.pprint(response.json())
        assert response.status_code == 200
        assert response.json()["data"]["changeEmail"]["viewer"]["profile"]["email"] == email_new
        assert response.json()["data"]["changeEmail"]["errors"] == None




