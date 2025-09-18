from django import forms
from .models import Tool, Rental

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ["name", "description", "price_per_day", "available"]

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ["start_date", "end_date"]
