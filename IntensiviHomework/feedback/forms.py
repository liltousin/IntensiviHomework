from django import forms

from . import models


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Feedback
        fields = (model.text.field.name,)
        labels = {
            model.text.field.name: 'Отзыв',
        }
        help_texts = {
            model.text.field.name: 'Напишите отзыв',
        }
        widgets = {model.text.field.name: forms.Textarea(attrs={"rows": "5"})}
