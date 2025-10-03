from .models import *
from django import forms

#class de tout les articles(BD,film,animée,serie)
class QRcodeAdminForm(forms.ModelForm):
    class Meta:
        model = QRcode
        fields = '__all__'