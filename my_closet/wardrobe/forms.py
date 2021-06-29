from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            "name": "Item Name",
            "description": "Item Description",
            "image": "Image of Item",
            "tag": "Make sure to select Top, Bottom, Dress, Shoes, or Outerwear",
            "sell": "For Sale?"
        }