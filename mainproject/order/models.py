from django.db import models
from products.models import *
from accounts.models import Customer



# class Restaurant(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20, blank=True)
#     email = models.EmailField()
#     owner_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[("pending", "Pending"), ("completed", "Completed"), ("cancelled", "Cancelled")])

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"

# OrderItem model (represents a specific dish in an order)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField()
    price_at_time_of_order = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.dish.name} x {self.quantity} for Order #{self.order.id}"



class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reviews")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Review by {self.customer} for {self.restaurant.name}"