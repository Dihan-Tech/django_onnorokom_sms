"""This file holds the default configuration values for OnnorokomSMS
   This limit is defined by OnnorokomSMS. As more than 160 characters
   it will count 2 sms"""
default_values = {
    'low_balance_warning_amount': 20,
    'background_process': False,
    'message_characters_limit': 160,
}
