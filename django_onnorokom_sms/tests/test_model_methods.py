from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_onnorokom_sms.models import DjangoOnnorokomSMSModel


class DjangoOnnorokomSMSModelTestCases(TestCase):
    model = DjangoOnnorokomSMSModel

    def setUp(self):
        test_user_one = get_user_model().objects.create(username='test_user_one', email='test_user_one@example.com', password='superacces123one')
        self.model.objects.create(message_text='Greater than 10 characters', sent_by=test_user_one, sent_to='01XXXXXXXXX')
        self.model.objects.create(message_text='Less', sent_by=test_user_one, sent_to='01XXXXXXXXX')

    def test_model_str_method(self):
        self.assertEqual(str(get_object_or_404(self.model, pk=1)), 'Greater th')
        self.assertEqual(str(get_object_or_404(self.model, pk=2)), 'Less')
