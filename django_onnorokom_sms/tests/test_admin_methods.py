from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince as djtimesince
from django.utils.timezone import now
from django_onnorokom_sms.models import DjangoOnnorokomSMSModel
from django_onnorokom_sms.admin import DjangoOnnorokomSMSModelAdmin


class DjangoOnnorokomSMSAdminTestCases(TestCase):
    model = DjangoOnnorokomSMSModel
    admin_class = DjangoOnnorokomSMSModelAdmin

    def setUp(self):
        self.creation_time_list = []
        test_user_one = get_user_model().objects.create(username='test_user_one', email='test_user_one@example.com', password='superacces123one')
        test_sms_object_one = self.model.objects.create(message_text='Greater than 10 characters', sent_by=test_user_one, sent_to='01XXXXXXXXX')
        self.creation_time_list.append(test_sms_object_one.created_at)
        test_sms_object_two = self.model.objects.create(message_text='Less', sent_by=test_user_one, sent_to='01XXXXXXXXX')
        self.creation_time_list.append(test_sms_object_two.created_at)

    def test_sms_time(self):
        self.assertEqual(self.admin_class.sms_time(self=None, obj=self.model.objects.get(id=1)), str(djtimesince(self.creation_time_list[0], now()).encode('utf8').replace(b'\xc2\xa0', b' ').decode('utf8')) + ' ago')
        self.assertEqual(self.admin_class.sms_time(self=None, obj=self.model.objects.get(id=2)), str(djtimesince(self.creation_time_list[1], now()).encode('utf8').replace(b'\xc2\xa0', b' ').decode('utf8')) + ' ago')
