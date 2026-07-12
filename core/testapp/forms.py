from django.forms import ModelForm
from core.testapp.models import Ifta


class CreateIFtaForm(ModelForm):
    class Meta:
        model = Ifta
        fields = [
           'name',
           'fiqh'
        ]