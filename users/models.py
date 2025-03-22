from django.db import models


class ConfirmModel(models.Model):
    code = models.CharField(max_length=6)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='sms_code')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} - {self.user.username}'
