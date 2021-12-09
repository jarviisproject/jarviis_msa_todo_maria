from django.db import models
from event.models import User


class Satisfaction(models.Model):
    use_in_migrations = True
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    #accept #reject

    def __str__(self):
        return f'[{self.pk}] \n {self.user} \n {self.created} \n {self.type}\n' \
               f'{self.result} 등 입력 완료'

    class Meta:
        db_table = 'satisfaction'

