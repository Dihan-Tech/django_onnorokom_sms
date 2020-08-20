from django.conf import settings
from django.core.exceptions import ValidationError
try:
    from zeep import Client
except ImportError:
    print('Zeep is not installed. Please install zeep. To install it please run pip install zeep')
from .cleaners import check_proper_instance_type
from .defaults import default_values
import math


class SMSGateway:
    """OnnorokomSMS has supported 2 types of SMS sending and 1 API for SMS gateway balence check.
       This class holds all those 3 types of methods to perform those API based actions."""

    def get_gateway_credentials(self, key_name, settings_object=None):
        """This method returns the asked key_name value if exists on the settings file. Raise
           ValidationError if not existed"""
        if settings_object is None:
            settings_object = settings
        if hasattr(settings_object, 'DJANGO_ONNOROKOM_SMS_CREDENTIALS'):
            if key_name in settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS:
                if key_name == 'mask_name':
                    return settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS[key_name]
                elif key_name == 'campaign_name':
                    return settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS[key_name]
                else:
                    if settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS[key_name] == '':
                        raise ValidationError(str(key_name) + ' can not be null')
                    else:
                        return settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS[key_name]
            else:
                raise ValidationError(str(key_name) + ' must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary')
        else:
            raise ValidationError('settings file must have a dictionary named DJANGO_ONNOROKOM_SMS_CREDENTIALS')

    def check_sms_balance(self):
        """This method is responsible for checking the balance of the SMSGateway. This returns
           a float representation of the current balance of the associated gateway account"""
        balance = self.client.service.GetCurrentBalance(self.apiKey)
        return balance

    def is_low_balance(self):
        """This method check the balance and compare if the balance is below the low balance warning
           amount and return True if it is otherwise False. You have to set 'low_balance_warning_amount'
           on the DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary otherwise the default will be counted.
           The default value is 20"""
        if hasattr(settings, 'DJANGO_ONNOROKOM_SMS_SETTINGS'):
            if 'low_balance_warning_amount' in settings.DJANGO_ONNOROKOM_SMS_SETTINGS:
                default_values['low_balance_warning_amount'] = check_proper_instance_type(settings.DJANGO_ONNOROKOM_SMS_SETTINGS['low_balance_warning_amount'], int)
        balance = self.check_sms_balance()
        if int(math.ceil(float(balance))) <= default_values['low_balance_warning_amount']:
            return True
        else:
            return False

    # Send a single SMS
    def send_single_sms(self, smsText, recipientNumber, mask_name=None, campaign_name=None, smsType='TEXT'):
        if mask_name is None:
            mask_name = self.maskName
        if campaign_name is None:
            campaign_name = self.campaignName
        result = self.client.service.NumberSms(self.apiKey, smsText, recipientNumber, smsType, mask_name, campaign_name)
        return result

    # Send multiple SMS
    def send_multiple_sms(self, smsText, numberList, mask_name=None, campaign_name=None, smsType='TEXT'):
        if mask_name is None:
            mask_name = self.maskName
        if campaign_name is None:
            campaign_name = self.campaignName
        numberList = ",".join(numberList)
        result = self.client.service.OneToMany(self.username, self.password, smsText, numberList, smsType, mask_name, campaign_name)
        return result

    def __init__(self):
        self.url = self.get_gateway_credentials('url')
        self.client = Client(self.url)
        self.apiKey = self.get_gateway_credentials('api_key')
        self.username = self.get_gateway_credentials('username')
        self.password = self.get_gateway_credentials('password')
        self.maskName = self.get_gateway_credentials('mask_name')
        self.campaignName = self.get_gateway_credentials('campaign_name')
