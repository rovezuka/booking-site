from django.db.models import TextChoices


class UserType(TextChoices):
    SELLER = "Seller", "Продавец"
    BUYER = "Buyer", "Покупатель"
