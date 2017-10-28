from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from AuthenticationSystem.settings import EMAIL_HOST
from rest_framework_jwt.settings import api_settings
import jwt

class resetPass(APIView):
    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404()

    def post(self, request):
        print("ResetPassword entered")
        received = request.data

        usr = self.get_object(email=received["email"])
        email_subject = 'Password Reset'
        email_sender = EMAIL_HOST
        email_receiver = [usr.email]
        # ----------------dont forget to activate server-------------------
        # python -m smtpd -n -c DebuggingServer localhost:1025
        # link to be offered part is the part in which the link is inserted
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(usr)
        token = jwt_encode_handler(payload)
        # -----------------------------------------------------------------
        Link = "http://127.0.0.1:4200/changePassword/?token=" + token + "/"
        email_content = "Click on This link to Proceed:\n\n" + Link + "\n\nWe hope we made you comfortable\n\nASU Racing Team"
        send_mail(email_subject, email_content, email_sender, email_receiver, fail_silently=False, )
        return Response(token)


class changePass(APIView):
    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404()

    def post(self, request):
        print("changePassword entered")
        received = request.data
        token = received["token"]
        dataRec = jwt.decode(token, verify=False)
        usr = self.get_object(email=dataRec["email"])
        if received["password"] == received["passwordConfirm"]:
            usr.set_password(received["password"])
            usr.save()
            return Response(dataRec)
        else:
            return Response(token)
        return Response(dataRec)

# tare2ty ele m4 3agba magdy XD
# import string
# import random

# tare2ty ele m4 3agba magdy XD
# def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# tare2ty ele m4 3agba magdy XD
# TmpPass = id_generator()
# usr.set_password(TmpPass)
# usr.save()
