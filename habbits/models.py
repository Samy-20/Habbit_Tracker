from django.db import models

# Create your models here.

class habbit(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    def _str_(self):
        return self.title
    
class HabbitLog(models.Model):
    habbit = models.ForeignKey(habbit, on_delete=models.CASCADE, related_name="logs")
    completed_on = models.DateField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["habbit", "completed_on"],
                name="unique_habit_per_day"
            )
        ]

    def __str__(self):
        return f"{self.habbit.title} - {self.completed_on}"