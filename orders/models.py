from django.db import models
from inside.models import SanPham
from django.db import models
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Textarea

class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(SanPham, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


# class Comment(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('True','True'),
#         ('False','False'),
#     )
#     product = models.ForeignKey(SanPham, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     subject = models.CharField(max_length=50, blank=True)
#     comment = models.CharField(max_length=250, blank=True)
#     rate = models.IntegerField(default = 1)
#     ip = models.CharField(max_length=20, blank = True)
#     status = models.CharField(max_length=10, choices=STATUS, default= 'New')
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.subject

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['subject', 'comment', 'rate']

