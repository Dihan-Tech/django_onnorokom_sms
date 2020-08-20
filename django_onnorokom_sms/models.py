from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince as djtimesince
from django.utils.timezone import now


# Create your models here.
class DjangoOnnorokomSMSModel(models.Model):
    """This class holds the data of each sent email. message_text is for the text details of the message,
       sent_by is an instance of the Auth User Model of the application. created_at holds the time
       when the message has sent. sent_to is a text which helds the data of a signle of multiple receipts
       number, mask_name and campaign_name holds the corresponding data if nothing used then it will be
       null. sms_purpose is the topics on which that SMS has sent. It is a text field. If not sent then it
       will be null. Only is_active True messages will be shown on List. response_code holds the response of the
       OnnorokomSMS APIs. is_success will be True if the message delivered sucessfully"""
    RESPONSE_CODES = (
        ('1900', 'Success'),
        ('1901', 'Parameter content missing'),
        ('1902', 'Invalid user/pass'),
        ('1903', 'Not enough balance'),
        ('1905', 'Invalid destination number'),
        ('1906', 'Operator Not found'),
        ('1907', 'Invalid mask Name'),
        ('1908', 'Sms body too long'),
        ('1909', 'Duplicate campaign Name'),
        ('1910', 'Invalid message'),
        ('1911', 'Too many Sms Request. Please try less than 500 in one request'),
        ('2000', 'Unmatched response code'),
    )
    message_text = models.TextField(verbose_name='Message Text', null=True, blank=True)
    sent_by = models.ForeignKey(get_user_model(), related_name='django_onnorokom_sms_sender',
                                on_delete=models.CASCADE, db_index=True, verbose_name='SMS Sent By')
    sent_to = models.TextField(verbose_name='Receipents', null=False, blank=False)
    sms_purpose = models.TextField(verbose_name='SMS Purpose', null=True, blank=True)
    mask_name = models.CharField(max_length=255, db_index=True, null=True, blank=True, verbose_name='Mask Name')
    campaign_name = models.CharField(max_length=255, db_index=True, null=True, blank=True, verbose_name='Campaign Name')
    response_code = models.CharField(max_length=80, verbose_name='Response Code', choices=RESPONSE_CODES)
    is_success = models.BooleanField(verbose_name='Status', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Django OnnorokomSMS'
        verbose_name_plural = 'Django OnnorokomSMSs'
        ordering = ['-created_at']

    def __str__(self):
        """Returns the first 10 characters of message body detail if it is greater than 10 if less and return
           the whole message body detail as text"""
        if len(self.message_text) >= 10:
            return self.message_text[:10]
        else:
            return self.message_text

    def get_timesince(self):
        """This method returns the time difference between today and the SMS sent time"""
        return djtimesince(self.created_at, now()).encode('utf8').replace(b'\xc2\xa0', b' ').decode('utf8')

    def clean(self):
        if self.response_code.count('/') == 0:

        super().clean()
