from rest_framework import exceptions
from django.conf import settings
import jwt
def isAuthorized(request):
    auth=request.session.get('Authorization')
    token = auth
    #auth=request.COOKIES['jwt']
    #auth=bytes(auth[2:-1],encoding='utf-8')
    print(auth,'auth')
    #token = auth.decode('utf-8')
    print(type(token),'token yoe')
    if token:
        #try:
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms='HS256')
            username = payload['username']
            print(username,'username')
            return payload['username']
            # except:
            #     raise exceptions.AuthenticationFailed('unauthenticated')
