from django.forms import ModelForm

from core.testapp.models import Ifta


class CreateIFtaForm(ModelForm):
    class Meta:
        model = Ifta
        fields = [
            "name",
            "fiqh",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = list(self.fields["fiqh"].choices)
        if choices and choices[0][0] == "":
            choices[0] = ("", "Choose a Fiqh")
        self.fields["fiqh"].choices = choices
