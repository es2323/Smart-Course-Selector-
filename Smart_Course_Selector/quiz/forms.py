from django import forms
from .models import Answer

class QuizForm(forms.Form):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(attrs={"class": "hidden peer"}),  # Tailwind-styled buttons
        empty_label=None
    )

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if question is not None:
            self.fields['answer'].queryset = question.answers.all()  # Use the corrected related_name
            self.fields['answer'].label = question.text
        else:
            self.fields['answer'].label = "No question available!"

