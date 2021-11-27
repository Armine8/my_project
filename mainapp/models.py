from django.db import models

class Product(models.Model):
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    receipt_date = models.DateTimeField(
        verbose_name='дата поступления',
        auto_now_add=True
    )

    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    unit = models.CharField(
        verbose_name='единица измерения',
        max_length=10,
    )

    provider = models.CharField(
        verbose_name='поставщик',
        max_length=50,
    )

    def __str__(self):
        return self.name



