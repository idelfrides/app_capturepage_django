from django.forms import ModelForm
from .models import LeadsEmail


class LeadsEmailForm(ModelForm):
    class Mera:
        model = LeadsEmail
        fields = ['email']