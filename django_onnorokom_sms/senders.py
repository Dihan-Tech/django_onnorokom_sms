from django.core.exceptions import ValidationError
from .scripts import SMSGateway
from .defaults import default_values
from .cleaners import (get_request_user, check_proper_instance_type)


def send_django_onnorokom_sms(request, message_text, sent_to, sms_purpose=None, mask_name=None, campaign_name=None, sms_type=None):
    """This function will be used by user to send SMS. Optional fields are assigned as None. If not provided then
       optional arguments will use default values.
       If sent_to is a list then call send_multiple_sms method otherwise call send_single_sms method"""
    sent_by = get_request_user(request)
    message_text = check_proper_instance_type(message_text, str)
    if len(message_text) > default_values['message_characters_limit']:
        raise ValidationError('message_text can not be exceed 160 characters')
    if isinstance(sent_to, list):
        for index, item in enumerate(sent_to):
            sent_to[index] = check_proper_instance_type(item, str)
    else:
        sent_to = check_proper_instance_type(sent_to, str)
    if sms_purpose is not None:
        sms_purpose = check_proper_instance_type(sms_purpose, str)
    if mask_name is not None:
        mask_name = check_proper_instance_type(mask_name, str)
    if campaign_name is not None:
        campaign_name = check_proper_instance_type(campaign_name, str)
    if sms_type is not None:
        sms_type = check_proper_instance_type(sms_type, str)
    if isinstance(sent_to, list):
        return SMSGateway().send_multiple_sms(message_text, sent_to, mask_name, campaign_name, sms_type)
    else:
        return SMSGateway().send_single_sms(message_text, sent_to, mask_name, campaign_name, sms_type)
