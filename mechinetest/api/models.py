from django.db import models

# Create your models here.


class Item(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=100, null=False)
    MRP = models.FloatField(default=0)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return (self.ItemId)


class ItemUnits(models.Model):
    ItemUnitId = models.AutoField(primary_key=True)
    ItemId = models.ForeignKey(
        Item, null=False, on_delete=models.CASCADE, db_column="ItemId")
    UnitId = models.IntegerField(blank=False, null=False)
    NoOfUnits = models.FloatField(blank=False, null=False)
    Rate = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'itemunits'

    def __str__(self):
        return (self.ItemId)
