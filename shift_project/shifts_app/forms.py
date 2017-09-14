from django import forms
from django.forms import fields, models, formsets, widgets
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.conf import settings
from bootstrap3_datetime.widgets import DateTimePicker
from shifts_app.shift import Shift 
from shifts_app.run import Run
from shifts_app.group import Post


class ShiftForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Shift
        fields = '__all__'
        labels = {'start_datetime': ('Start (YYYY-MM-DD : 00:00)'), 'end_datetime': ('End (YYYY-MM-DD : 00:00)')}

    def __init__(self, *args, **kwargs):
        super(ShiftForm, self).__init__(*args, **kwargs)
        self.fields['start_datetime'].widget = AdminSplitDateTime()
        self.fields['end_datetime'].widget = AdminSplitDateTime()
    
    def clean(self):
        start_datetime = self.cleaned_data.get("start_datetime")
        end_datetime = self.cleaned_data.get("end_datetime")
        if end_datetime < start_datetime:
            msg = u"End date should be greater than start date."
            self._errors["end_datetime"] = self.error_class([msg])

class RunForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Run
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(RunForm, self).__init__(*args, **kwargs)
        self.fields['start_datetime'].widget = AdminSplitDateTime()
        self.fields['end_datetime'].widget = AdminSplitDateTime()    

class PostForm(forms.Form):
    user_id = fields.IntegerField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].error_messages = {'required': 'Enter your User ID'}


# class PostCreate(forms.Form):
#     runs = forms.ModelChoiceField(queryset=Run.objects.none(), widget=forms.CheckboxSelectMultiple(), empty_label=None)
#     class Meta:
#         model = Post
#         fields = '__all__'
#     def __init__(self, *args, **kwargs):
#         queryset = kwargs.pop('queryset', None)
#         super(PostCreate, self).__init__(*args, **kwargs)
#         if queryset:
#             self.fields['runs'].queryset = queryset
# def get_ordereditem_formset(form, formset=models.BaseInlineFormSet, **kwargs):
#     return models.inlineformset_factory(Order, OrderedItem, form, formset, **kwargs)
