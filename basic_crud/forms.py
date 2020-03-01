from django import forms
from django.forms import ModelForm
from .models import Detail


class UserDetails(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['fullname', 'email', 'phone']
        labels = {
            'fullname': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number'
        }

    def __init__(self, *args, **kwargs):
        super(UserDetails, self).__init__(*args, **kwargs)
        # for select type it show - ---- so to eliminate that

        # self.fields['fieldname'].empty_label = "Select"
        # for making field not required
        self.fields['phone'].required = False


# class UserDetails(forms.Form):
#     name = forms.CharField(max_length=50,
#                            widget=forms.TextInput(
#                                attrs={"placeholder": "Input your Name",
#                                       "class": "form-control"}
#                            ))
#     email = forms.EmailField(max_length=200,
#                              widget=forms.EmailInput(
#                                  attrs={"class": "form-control",
#                                         "placeholder": "Input Email"}
#                              ))
#     phone = forms.CharField(max_length=20,
#                             widget=forms.NumberInput(
#                                 attrs={"class": "form-control",
#                                        "placeholder": "Input your phone number"}
#                             ))
