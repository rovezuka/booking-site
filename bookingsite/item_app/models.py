from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100) # имя
    description = models.TextField() # описание
    quantity = models.PositiveIntegerField(default=0) # доступное количество

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Предметы"

class Reservation(models.Model):
    user = models.ForeignKey(
        "user_app.User", on_delete=models.SET_NULL, related_name="items", null=True)
    items = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    booking_at = models.DateTimeField(auto_now_add=True)
    num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f' {self.items.name} забронирован {self.user.email}'

    class Meta:
        verbose_name_plural = 'Бронирование'


