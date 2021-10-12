from django import forms
#from .models import webProjectAppModel
# form inputs created and taken directly form here in forms.py

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.ImageField(help_text="Enter 6 digits roll number")
    password = forms.CharField(widget= forms.PasswordInput())
    
"""

# from models.py
# inputs taken from models.py

# import webProjectAppModel from models.py
from .models import webProjectAppModel

# create a modelForm
class webProjectAppModel(forms.ModelForm):

    # specify the name of the model to use
    class Meta:
        model = webProjectAppModel
        fields = "__all__"
"""