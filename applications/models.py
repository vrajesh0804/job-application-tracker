from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("not_applied", "Not Applied"),
        ("applied", "Applied"),
        ("interview", "Interview"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("on_hold", "On Hold"),
    ]

    role_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    hr_name = models.CharField(max_length=150, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="not_applied"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role_name} - {self.company_name}"