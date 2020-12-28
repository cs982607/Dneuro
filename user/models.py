import time, hmac, base64, hashlib, requests, json, datetime
from random             import randint

from django.db          import models
from django.utils       import timezone

from model_utils.models import TimeStampedModel

from my_settings        import (
    SMS_ACCESS_KEY_ID,
    SMS_SERVICE_SECRET,
    SMS_SEND_PHONE_NUMBER
)

class Country(models.Model):
    name_kor = models.CharField(max_length=45)
    name_eng = models.CharField(max_length=45, null=True)

    class Meta:
        db_table='countries'

class User(models.Model):
    email    = models.EmailField(max_length=45)
    password = models.CharField(max_length=200, null=True)
    sex      = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
    country  = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True)
    kakao_id = models.CharField(max_length=45, null=True)

    class Meta:
        db_table='users'

class AuthSms(TimeStampedModel):
    phone_number = models.CharField(verbose_name='휴대폰번호',primary_key=True, max_length=11)
    auth_number  = models.IntegerField(verbose_name='인증번호')

    class Meta:
        db_table='auth_numbers'

    def save(self, *args, **kwargs):
        self.auth_number = randint(100000, 1000000)
        super().save(*args, **kwargs)
        self.send_sms() # 인증번호 SMS전송

    def send_sms(self):
        url     = 'https://sens.apigw.ntruss.com'
        uri     = '/sms/v2/services/ncp:sms:kr:262709820617:test/messages'
        api_url = url + uri

        body    = {
            "type"        : "SMS",
            "contentType" : "COMM",
            "from"        : "01041361668",
            "content"     : "[테스트] 인증 번호 [{}]를 입력해주세요.".format(self.auth_number),
            "messages"    : [{"to" : self.phone_number}]
        }

        timeStamp      = str(int(time.time() * 1000))
        access_key     = SMS_ACCESS_KEY_ID
        string = "POST" + " " + uri + "\n" + timeStamp + "\n" + access_key
        signature      = self.make_signature(string)

        headers = {
            "Content-Type"             : "application/json; charset=UTF-8",
            "x-ncp-apigw-timestamp"    : timeStamp,
            "x-ncp-iam-access-key"     : access_key,
            "x-ncp-apigw-signature-v2" : signature
            }

        res = requests.post(api_url, data = json.dumps(body), headers=headers)

        res.request
        res.status_code
        res.raise_for_status()


    def make_signature(self,string):
        secret_key    = bytes(SMS_SERVICE_SECRET, 'UTF-8')
        message       = bytes(string, 'UTF-8')
        signingKey    = hmac.new(secret_key, message, digestmod = hashlib.sha256).digest()
        signature     = base64.b64encode(signingKey).decode('UTF-8')

        return signature

    @classmethod
    def check_auth_number(cls, p_num, c_num):
        time_limit    = timezone.now() - datetime.timedelta(minutes = 5)
        result        = cls.objects.filter(
                            phone_number  = p_num,
                            auth_number   = c_num,
                            modified__gte = time_limit
                        )
        if result:
            return True
        return False



