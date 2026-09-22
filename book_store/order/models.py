from django.db import models


STATUS = {
    "tan": "Tanlamoqda",
    "jar": "Jarayonda",
    "bekor": "Bekor qilingan",
    "yet": "Yetkazib berilgan"
}


class Order(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.CharField(choices=STATUS, default="tan")
    address = models.CharField(max_length=255)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("main.Book", on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

