from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "role_name",
            "company_name",
            "hr_name",
            "link",
            "date",
            "status",
        ]

        widgets = {
            "role_name": forms.TextInput(attrs={"placeholder": "Backend Developer"}),
            "company_name": forms.TextInput(attrs={"placeholder": "Company name"}),
            "hr_name": forms.TextInput(attrs={"placeholder": "HR name"}),
            "link": forms.URLInput(attrs={"placeholder": "https://example.com/job"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(),
        }