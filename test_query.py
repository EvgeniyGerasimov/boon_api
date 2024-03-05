import methods.query_body as payload
from methods.methods import Methods
from methods.data import query_schema
from jsonschema import validate
import pprint
import allure
import pytest



@allure.feature('Test query')
class TestUserQuery(Methods):

    @allure.story('Test validation email with invalid data')
    @pytest.mark.parametrize('email', payload.Invalid_email)
    def test_validation_email_with_invalid_data(self, email):
        body = payload.email_validation_body(email)
        response = self.post_for_generation_new_user(body)
        assert response.status_code == 200
        pprint.pprint(response.json())
        assert response.json()["data"]["viewer"]["validateEmail"] == None
        assert response.json()["errors"][0]["message"] == ' Your email seems incorrect'

    @allure.story('Test validation email with valid data')
    def test_validation_email_with_valid_data(self):
        email = "test.test@gmail.com"
        body = payload.email_validation_body(email)
        response = self.post_for_generation_new_user(body)
        assert response.status_code == 200
        assert response.json()["data"]["viewer"]["validateEmail"] == True


    @allure.story('Test view lesson structure')
    def test_lesson_structure(self):
        response = self.post(payload.LESSON_STRUCTURE)
        assert response.status_code == 200
        pprint.pprint(response.json())
        validate(instance=response.json(), schema=query_schema.LESSON_STRUCTURE)

    @allure.story('Test quiz detale ')
    def test_quiz_detale(self):
        response = self.post(payload.Q)
        assert response.status_code == 200
        pprint.pprint(response.json())
        validate(instance=response.json(), schema=query_schema.QUIZ_DETALE)


    @allure.story('Test quiz statistic ')
    def test_quiz_statistic(self):
        response = self.post(payload.Q_STAT)
        assert response.status_code == 200
        pprint.pprint(response.json())
        validate(instance=response.json(), schema=query_schema.QUIZ_STAT)

    @allure.story('Test onbording photo')
    def test_onbording_photo(self):
        response = self.post(payload.ONBORDING_PHOTO)
        assert response.status_code == 200
        pprint.pprint(response.json())
        validate(instance=response.json(), schema=query_schema.ONBORDING_PHOTO)

    @allure.story('Test onbording questions')
    def test_onbording_questions(self):
        response = self.post(payload.ONBORDING_QUESTIONS)
        assert response.status_code == 200
        pprint.pprint(response.json())
        validate(instance=response.json(), schema=query_schema.ONBOARDING_QUESTIONS)

    @allure.story('Test onbording questions')
    @pytest.mark.parametrize('plan', payload.plans)
    def test_plan_vip(self, plan):
        response = self.post(plan)
        assert response.status_code == 200
        pprint.pprint(response.json())
        validate(instance=response.json(), schema=query_schema.PLANS_VIP)









