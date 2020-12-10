from django import forms
from .models import Feeding, Cat

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ('name', 'breed', 'description', 'age')