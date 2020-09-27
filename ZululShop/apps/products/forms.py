from django import forms

class ProductCategory(forms.Form):
    vegetables = 'vegetables'
    fruits = 'fruits'
    something_unusual = 'something unusual'
    CHOICES = (
        (vegetables, 'vegetables'), 
        (fruits, 'fruits'), 
        (something_unusual, 'something unusual'), 
    )

    category = forms.ChoiceField(choices=CHOICES)