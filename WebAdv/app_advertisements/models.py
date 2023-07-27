from django.db import models

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add - работает 1 раз
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Advertisement'
    def __str__(self):
        return f'{self.title}, {self.description}, {self.price}, {self.auction}'