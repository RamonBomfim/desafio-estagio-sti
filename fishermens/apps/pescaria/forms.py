from django.forms import ModelForm, DateInput, TimeInput
from .models import Fishing


class DateInput(DateInput):
    input_type = 'date'


class TimeInput(TimeInput):
    input_type = 'time'


class Fisheries(ModelForm):
    class Meta:
        model = Fishing
        widgets = {
            'fishing_day': DateInput(),
            'fishing_hour': TimeInput(),
        }
        fields = '__all__'
