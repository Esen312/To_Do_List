from django.db import models

class Task(models.Model):
    CHOICES = [
            ('YES', 'Done'),
            ('PL', 'Scheduled'),
            ('NOT', 'Canceled'),
    ]
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=50, choices=CHOICES)
    created = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']