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
        fake_settings_object.DJANGO_ONNOROKOM_SMS_SETTINGS = lambda: None
        setattr(fake_settings_object.DJANGO_ONNOROKOM_SMS_SETTINGS, 'DJANGO_ONNOROKOM_SMS_SETTINGS', {})
        fake_settings_object_list.append(fake_settings_object)
        return fake_settings_object_list

    def test_default_value(self):
        """Testing default values"""
        self.assertEqual(self.test_class_name.low_balance_warning_amount, 20)
        self.assertEqual(self.test_class_name.background_process, False)

    def test_check_proper_instance_type(self):
        """Testing check_proper_instance_type method"""
        self.assertEqual(self.test_class_name.check_proper_instance_type(23, int), 23)
        self.assertEqual(self.test_class_name.check_proper_instance_type('hello', str), 'hello')
        self.assertRaisesMessage(ValidationError, 'The value must be a str', self.test_class_name.check_proper_instance_type, value=23, instance_type=str)

    def test_get_gateway_credentials(self):
        """Testing get_gateway_credentials method"""
        test_settings_object_list = self.setUp()
        self.assertRaisesMessage(ValidationError, 'settings file must have a dictionary named DJANGO_ONNOROKOM_SMS_CREDENTIALS',
                                 self.test_class_name.get_gateway_credentials, key_name='mask_name', settings_object=test_settings_object_list[0])
        self.assertEqual(self.test_class_name.get_gateway_credentials('mask_name'), '')
