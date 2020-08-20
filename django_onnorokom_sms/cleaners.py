from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser


def get_clean_request_object(request):
    """Receives HttpRequest object and check if it is really belongs to HttpRequest class. If not then
       raise ValidationError"""
    if isinstance(request, HttpRequest):
        return request
    else:
        raise ValidationError('request must be a Django HttpRequest object')


def get_request_user(request):
    """Receives a Django HttpRequest object and return the user object if found. If no user object has found then it
       returns None instead"""
    if request is None:
        return None
    else:
        request = get_clean_request_object(request)
        if hasattr(request, 'user'):
            """Check if it is an Anonymous user"""
            if isinstance(request.user, AnonymousUser):
                return None
            else:
                if isinstance(request.user, get_user_model()):
                    return request.user
                else:
                    raise ValidationError('The request.user object seems to be tempered')
        else:
            return None
