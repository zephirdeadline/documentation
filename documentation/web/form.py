from django.forms import ModelForm
from web.models import doc


class DocForm(ModelForm):
    class Meta:
        model = doc
        exclude = ['date']
