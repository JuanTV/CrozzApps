from django.forms import ModelForm
from autos.models import Make


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

# this is only used if decide to use the longer way of defining the make views in views.py, check: https://github.com/csev/dj4e-samples/blob/main/autos/views.py for reference.