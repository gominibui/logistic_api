from django.db import models


class Order(models.Model):
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ]
    )

    def __str__(self):
        return f'Order {self.id}: {self.description}'
