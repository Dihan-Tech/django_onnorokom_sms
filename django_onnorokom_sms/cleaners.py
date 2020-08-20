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


def check_proper_instance_type(value, instance_type):
    """Return the value if desired instance meet otherwise raise ValidationError"""
    if isinstance(value, instance_type):
        return value
    else:
        raise ValidationError('The value must be a ' + instance_type.__name__)


def clean_response_code(response_code):
    """Clean and prepare response code receives from OnnorokomSMS API"""
    if response_code.count('||') == 0:
        return '2000'
    if response_code.count('/') == 0:
        return response_code.partition('||')[0]
    else:
        for i in range(len(response_code.partition('/'))):
            result = response_code.partition('/')[i].partition('||')[0]
        return result
