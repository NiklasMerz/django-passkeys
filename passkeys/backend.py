from django.contrib.auth.backends import ModelBackend


class PasskeyModelBackend(ModelBackend):
    def authenticate(self, request, username='',password='', **kwargs):
        if username!='' and password !='':
            return super().authenticate(request,username=username,password=password, **kwargs)
        if len(request.POST["passkeys"])>5:
            from .FIDO2 import auth_complete
            return auth_complete(request)