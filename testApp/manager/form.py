from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from manager.models import Manager, Company

class CompanyForm(forms.ModelForm) :
    # model.pyですでに定義されていたから使わない
    