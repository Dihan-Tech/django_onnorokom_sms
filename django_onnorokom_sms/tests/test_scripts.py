from django.test import TestCase
from django.core.exceptions import ValidationError
from django_onnorokom_sms.scripts import SMSGateway


class SMSGatewayClassTestCases(TestCase):
    """Testing SMSGateway class methods"""
    test_class_name = SMSGateway()

    def setUp(self):
        """Construct a fake settings object"""
        fake_settings_object_list = []
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object_list.append(fake_settings_object)
        #  Setting DJANGO_ONNOROKOM_SMS_SETTINGS keyword to the fake_settings_object
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS = lambda: None
        setattr(fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS, 'DJANGO_ONNOROKOM_SMS_CREDENTIALS', {})
        fake_settings_object_list.append(fake_settings_object)
        #  Setting DJANGO_ONNOROKOM_SMS_CREDENTIALS all keywords with null data
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS = lambda: None
        setattr(fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS, 'DJANGO_ONNOROKOM_SMS_CREDENTIALS', {})
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['url'] = ''
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['api_key'] = ''
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['username'] = ''
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['password'] = ''
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['mask_name'] = ''
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['campaign_name'] = ''
        fake_settings_object_list.append(fake_settings_object)
        #  Setting DJANGO_ONNOROKOM_SMS_CREDENTIALS all keywords with fake data
        fake_settings_object = type('test', (object,), {})()
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS = lambda: None
        setattr(fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS, 'DJANGO_ONNOROKOM_SMS_CREDENTIALS', {})
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['url'] = 'https://onnorokomsms.net'
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['api_key'] = 'example_api_key'
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['username'] = 'example_username'
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['password'] = 'example_password'
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['mask_name'] = 'example_mask_name'
        fake_settings_object.DJANGO_ONNOROKOM_SMS_CREDENTIALS.DJANGO_ONNOROKOM_SMS_CREDENTIALS['campaign_name'] = 'example_campagin_name'
        fake_settings_object_list.append(fake_settings_object)
        return fake_settings_object_list

    def test_get_gateway_credentials(self):
        """Testing get_gateway_credentials method"""
        test_settings_object_list = self.setUp()
        self.assertRaisesMessage(ValidationError, 'settings file must have a dictionary named DJANGO_ONNOROKOM_SMS_CREDENTIALS',
                                 self.test_class_name.get_gateway_credentials, key_name='mask_name', settings_object=test_settings_object_list[0])
        self.assertRaisesMessage(ValidationError, 'url must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary',
                                 self.test_class_name.get_gateway_credentials, key_name='url', settings_object=test_settings_object_list[1].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'api_key must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary',
                                 self.test_class_name.get_gateway_credentials, key_name='api_key', settings_object=test_settings_object_list[1].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'username must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary',
                                 self.test_class_name.get_gateway_credentials, key_name='username', settings_object=test_settings_object_list[1].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'password must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary',
                                 self.test_class_name.get_gateway_credentials, key_name='password', settings_object=test_settings_object_list[1].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'mask_name must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary',
                                 self.test_class_name.get_gateway_credentials, key_name='mask_name', settings_object=test_settings_object_list[1].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'campaign_name must have to be on DJANGO_ONNOROKOM_SMS_CREDENTIALS dictionary',
                                 self.test_class_name.get_gateway_credentials, key_name='campaign_name', settings_object=test_settings_object_list[1].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'url can not be null',
                                 self.test_class_name.get_gateway_credentials, key_name='url', settings_object=test_settings_object_list[2].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'api_key can not be null',
                                 self.test_class_name.get_gateway_credentials, key_name='api_key', settings_object=test_settings_object_list[2].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'username can not be null',
                                 self.test_class_name.get_gateway_credentials, key_name='username', settings_object=test_settings_object_list[2].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertRaisesMessage(ValidationError, 'password can not be null',
                                 self.test_class_name.get_gateway_credentials, key_name='password', settings_object=test_settings_object_list[2].DJANGO_ONNOROKOM_SMS_CREDENTIALS)
        self.assertEqual(self.test_class_name.get_gateway_credentials('mask_name', settings_object=test_settings_object_list[2].DJANGO_ONNOROKOM_SMS_CREDENTIALS), '')
        self.assertEqual(self.test_class_name.get_gateway_credentials('campaign_name', settings_object=test_settings_object_list[2].DJANGO_ONNOROKOM_SMS_CREDENTIALS), '')
        self.assertEqual(self.test_class_name.get_gateway_credentials('url', settings_object=test_settings_object_list[3].DJANGO_ONNOROKOM_SMS_CREDENTIALS), 'https://onnorokomsms.net')
        self.assertEqual(self.test_class_name.get_gateway_credentials('api_key', settings_object=test_settings_object_list[3].DJANGO_ONNOROKOM_SMS_CREDENTIALS), 'example_api_key')
        self.assertEqual(self.test_class_name.get_gateway_credentials('username', settings_object=test_settings_object_list[3].DJANGO_ONNOROKOM_SMS_CREDENTIALS), 'example_username')
        self.assertEqual(self.test_class_name.get_gateway_credentials('password', settings_object=test_settings_object_list[3].DJANGO_ONNOROKOM_SMS_CREDENTIALS), 'example_password')
        self.assertEqual(self.test_class_name.get_gateway_credentials('mask_name', settings_object=test_settings_object_list[3].DJANGO_ONNOROKOM_SMS_CREDENTIALS), 'example_mask_name')
        self.assertEqual(self.test_class_name.get_gateway_credentials('campaign_name', settings_object=test_settings_object_list[3].DJANGO_ONNOROKOM_SMS_CREDENTIALS), 'example_campagin_name')
