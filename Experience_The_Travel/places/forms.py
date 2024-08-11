from django import forms
from .models import Typology


class PlaceFilterForm(forms.Form):
    DESTINATION_TYPES = (
        ('', 'All'),
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('forest', 'Forest'),
    )
    
    DIFFICULTY_LEVELS = (
        ('easy', 'Easy'),
        ('difficult','Difficult'),
        ('challenging','Challenging'),
        ('medium','Medium'),
    )

    DURATIONS = (
        ('5 days', '5 days'),
        ('10 days', '10 days'),
        ('15 days', '15 days'),
        ('1 week', '1 week'),
    )

    destination_type = forms.ChoiceField(choices=DESTINATION_TYPES, required=False)
    typologies = forms.ModelMultipleChoiceField(queryset=Typology.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    # duration = forms.MultipleChoiceField(choices=DURATIONS, widget=forms.CheckboxSelectMultiple, required=False)
    # difficulty = forms.MultipleChoiceField(choices=DIFFICULTY_LEVELS, widget=forms.CheckboxSelectMultiple, required=False)
    # duration = forms.ChoiceField(choices=DURATIONS, required=False)
    # difficulty = forms.ChoiceField(choices=DESTINATION_TYPES, required=False)
    duration = forms.ChoiceField(choices=DURATIONS, widget=forms.RadioSelect, required=False)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_LEVELS, widget=forms.RadioSelect, required=False)