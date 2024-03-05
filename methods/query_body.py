#Data for parametrs



Invalid_email = (("test"),("test. @yopmail.com"),("test.yopmail.com"),)

Invalid_login_data = (("","111111"),("test.autotesterAPIbase@yopmail.com",""),("test.autotesterAPIbase@yopmail.com","11"),("test.payment17yopmail.com","111111"),)

Incorrect_pass = (("111122", "1111@@", "password.mismatch"), ("1111", "1111","password.length"), ("1111!№", "1111!№", "password.special"))

#Query body


LOGIN_USER = {
  "query": "mutation LoginComponentMutation($input_0:GenerateAccessTokenMutationInput!) {generateAccessToken(input:$input_0) {viewer {xsrfToken profile {email}} errors {key,message}}}",
  "variables": "{\"input_0\": {\"email\":\"test.payment17@yopmail.com\",\"password\":\"11111111\",\"clientMutationId\":\"0\"}}"
}

LOGIN_USER_BASE = {
  "query": "mutation LoginComponentMutation($input_0:GenerateAccessTokenMutationInput!) {generateAccessToken(input:$input_0) {viewer {xsrfToken profile {email}} errors {key,message}}}",
  "variables": "{\"input_0\": {\"email\":\"test.autotesterAPIbase@yopmail.com\",\"password\":\"11111111\",\"clientMutationId\":\"0\"}}"
}

def login_with_invalid_data(email, password):

  INVALID_LOGIN_DATA = {
    "query": "mutation LoginComponentMutation($input_0:GenerateAccessTokenMutationInput!) {generateAccessToken(input:$input_0) {viewer {xsrfToken} errors {key,message}}}",
    "variables": "{\"input_0\": {\"email\":\"" + email + "\",\"password\":\"" + password + "\",\"clientMutationId\":\"0\"}}"
    }
  return INVALID_LOGIN_DATA


REGISTRATION_WITH_USED_EMAIL = {
  "query": "mutation CreateUser($user: UserRegistrationMutationInput!){userRegistration(input: $user){errors{key message}viewer{profile{id sex lookingFor firstName email fullYears city{name}} searchSettings {lookingFor sex ageFrom ageTo isMetric distance heightFrom heightTo cityId}  xsrfToken}}}",
  "variables": "{\"user\":{\"firstName\":\"TestAutoReply\",\"email\":\"test.payment17@yopmail.com\",\"cityId\":\"Y2l0eTo2MTc2\",\"sex\":\"female\",\"lookingFor\":\"male\",\"birthdate\":\"1991-03-24\",\"clientMutationId\":\"998\"}}"
}
def email_validation_body(email):
  mail = email
  EMAIL_VALIDATION = {
    "query":"query validationEmail{\n\tviewer{validateEmail(email:\""+str(mail)+ "\")}}","operationName":"validationEmail","variables":{}}
  return EMAIL_VALIDATION

def login_body(email):
  mail = email
  input_var = "{\"input\": {\"clientMutationId\": \"abcde\", \"email\":\""+str(mail)+ "\" , \"password\": \"11111111\"}}"
  LOGIN  = {
    "query": "mutation generateAccessToken($input: GenerateAccessTokenMutationInput!){generateAccessToken(input:$input){ errors {key message}  viewer{accessToken ip profile{id email}}}} ",
    "variables": input_var
  }
  return LOGIN

def registration_body(email):
  mail = str(email)
  print(mail)
  input_var = {"input": {"email":mail,"clientMutationId": "abcde","gender": "male","age": "20-30", "utmLabels":"{\"utm_source\":\"not_set\",\"utm_term\":\"analytic_disabled\",\"initial_utm_source\":\"not_set\",\"initialClickDt\":\"1682058470091\",\"clickDt\":\"1682058470091\"}", "uuid":"" }}
  REGISRTRATION  = {
    "query": "mutation userRegistration($input: UserRegistrationMutationInput!){userRegistration(input:$input){ errors {key message} profileCreated viewer{accessToken xsrfToken ip profile{id email}}}} ",
    "variables": input_var
  }
  return REGISRTRATION

def registration_body_with_invalid_email(email):
  mail = email
  REGISRTRATION_WITH_INVALID_EMAIL = {
  "query": "mutation CreateUser($user: UserRegistrationMutationInput!){userRegistration(input: $user){errors{key message}viewer{profile{id sex lookingFor firstName email fullYears city{name}} searchSettings {lookingFor sex ageFrom ageTo isMetric distance heightFrom heightTo cityId}  xsrfToken}}}",
  "variables": "{\"user\":{\"firstName\":\"TestAutoReply\",\"email\":\""+str(mail)+ "\",\"cityId\":\"Y2l0eTo2MTc2\",\"sex\":\"female\",\"lookingFor\":\"male\",\"birthdate\":\"1991-03-24\",\"clientMutationId\":\"998\"}}"
}

  return REGISRTRATION_WITH_INVALID_EMAIL

FINISH_REGISTRATION = {
    "query": "mutation finishRegistrationMutation($input: FinishRegistrationMutationInput!){finishRegistration(input:$input){clientMutationId errors {key message} viewer{accessToken xsrfToken profile{id isVip email}}}} ",
    "variables": "{\"input\":{}}"
  }
NOTIFICATION_ON = {
  "query":"mutation updateUserPreferences ($input: UpdateUserPreferencesMutationInput!) {\nupdateUserPreferences(input: $input) {\n  errors{key message}\n  \n\tviewer{profile{preferences{emailNotifications pushNotifications}}\n\t\t\n\t}\n}\n}\n\n\n","operationName":"updateUserPreferences",
  "variables":{"input":{"clientMutationId": "kgljyu", "emailNotifications":True, "pushNotifications": True}}
 }

NOTIFICATION_OFF = {
  "query":"mutation updateUserPreferences ($input: UpdateUserPreferencesMutationInput!) {\nupdateUserPreferences(input: $input) {\n  errors{key message}\n  \n\tviewer{profile{preferences{emailNotifications pushNotifications}}\n\t\t\n\t}\n}\n}\n\n\n","operationName":"updateUserPreferences",
  "variables":{"input":{"clientMutationId": "kgljyu", "emailNotifications": False, "pushNotifications": False}}
 }

SAVE_ANSWER = {
  "query":"mutation quizAnswerMutation ($input: QuizAnswerMutationInput!) {quizAnswerMutation(input: $input) {\n  errors{key message} isQuizAttemptCompleted}} ",
  "variables":{"input":{"clientMutationId": "kgljyu", "userId":"dXNlcjox", "questionId": "cXVpei5xdWVzdGlvbi50eXBlOjI=","answerIds":["cXVlc3Rpb24uYW5zd2VyLnR5cGU6Nw="]}}
 }

def change_email(email):
  mail = email
  input_var = "{\"input\": {\"email\":\""+str(mail)+ "\" ,\"clientMutationId\": \"abcde\"}}"
  EMAIL  = {
    "query": "mutation changeEmail($input: ChangeEmailMutationInput!){changeEmail(input:$input){ errors {key message}  viewer{profile{email}}}} ",
    "variables": input_var
  }
  return EMAIL

def change_pass(new_pass, old_pass):

  input_var = "{\"input\": {\"newPassword\":\""+str(new_pass)+ "\" ,\"newPasswordConfirm\":\""+str(new_pass)+ "\" ,\"password\":\""+str(old_pass)+ "\" ,\"clientMutationId\": \"abcde\"}}"
  PASSWORD  = {
    "query": "mutation changePassword($input: ChangePasswordMutationInput!){changePassword(input:$input){ errors {key message}  viewer{profile{email}}}} ",
    "variables": input_var
  }
  return PASSWORD

LESSON_STRUCTURE = {
  "query":"query{viewer {sections{id name lessons{id name finalAssessment{id viewerRelated{isCompleted}} subLessons{id name isCompleted quizzes{id viewerRelated{isCompleted}}}}}}}\n\n\n",
  "variables": "{\"input\":{}}"
}


Q = {
  "query":"query  {node(id: \"cXVpei50eXBlOjE=\") {__typename... on  Quiz{name type questions{id questionType text{id content} note{id rightNote wrongNote} answers{id text isRightAnswer}}}}}"
}

ONBORDING_PHOTO = {
  "query":"query{viewer {onboardingImages{questionId url }}}\n\n\n",
  "variables": "{\"input\":{}}"
}

ONBORDING_QUESTIONS = {"query":"query{viewer{onboardingQuestions{id text title  section  note answers{text picture emoji picture alignment eventPropValue} subQuestions{text id title modifier identifier event eventProp section }}}}"}

SECTION = {
  "query":"query  {node(id: \"c3ViLmxlc3Nvbjox\") {__typename ... on  SubLesson{ name id}}}\n","operationName":"Operations"
}

Q_STAT = {
  "query":"query {viewer {profile { statistics(quizId:\"cXVpei50eXBlOjc=\"){percQuestionsAnsweredOnFirstTry}}}}"
}

BUY_VIP = {"query":"\nmutation buyVip($input: BuyVipMutationInput!) {buyVip(input: $input) {errors {key message}viewer{profile{email vip{isActive}}}eventId amountReceived threeDSecureData {order}needThreeDSecure}}","operationName":"buyVip","variables":{"input":{"gateway":"sticky","currencyCode":"usd","productId":"7days_vip_plan_7","threeDInput":{},"creditCardInput":{"number":"4242424242424242","cvc":"234","expMonth":"11","expYear":"2027","cardholderName":"some name","addressZip":"zip"}}}}

CANSEL_VIP =  {"query":"mutation CancelVip($input: CancelVipMutationInput!) {\ncancelVip(input: $input) {errors{key message}viewer{profile {email vip{isActive isCanceled}}}}}\n","operationName":"CancelVip","variables":{"input":{"clientMutationId":"3c0ccaba-f531-a2cd-8a0d-fdd3c3649fd8"}}}

PLANS_VIP_HP = {"query":"query  {viewer {profile{id email plans (placement:home_page) {id,planId,gateway,type,purchaseType,priceLevel,currency,price,priceRecurring,fullPrice,discountPercent,needShowDiscount,durationText,titleText}}}}",
             "variables":{}}
PLANS_VIP_PAY_PAGE = {"query":"query  {viewer {profile{id email plans (placement:payment_page) {id,planId,gateway,type,purchaseType,priceLevel,currency,price,priceRecurring,fullPrice,discountPercent,needShowDiscount,durationText,titleText}}}}",
             "variables":{}}
PLANS_EX_POP_UP = {"query":"query  {viewer {profile{id email plans (placement:exit_pop_up) {id,planId,gateway,type,purchaseType,priceLevel,currency,price,priceRecurring,fullPrice,discountPercent,needShowDiscount,durationText,titleText}}}}",
             "variables":{}}

plans = ((PLANS_VIP_HP),(PLANS_VIP_PAY_PAGE),(PLANS_EX_POP_UP))