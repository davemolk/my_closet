from django import forms

from .models import Clothing

class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = '__all__'
        labels = {
            "name": "Item Name",
            "description": "Item Description",
            "image": "Image of Item",
            "sell": "For Sale?"
        }