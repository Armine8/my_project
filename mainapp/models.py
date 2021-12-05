from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Category(models.Model):
    value = models.CharField(max_length=20)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    # objects = models.Manager()
    # on_site = CurrentSiteManager('site')


    def __str__(self):
        return self.value


class CustomQuerySet(models.QuerySet):
    def value_filter(self):
        return self.filter(value='value1')


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

    def value_filter(self):
        return self.get_queryset().value_filter()


class Product(models.Model):
    value = models.CharField(max_length=20)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    category1 = models.ManyToManyField(Category, related_name='category1')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)


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
        return self.value



