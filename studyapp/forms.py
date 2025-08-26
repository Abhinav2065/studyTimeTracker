# studyapp/forms.py
from django import forms
from .models import Subject, Chapter

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']  # Only show the name field, user is set automatically

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['subject', 'name']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show subjects that belong to the current user
        self.fields['subject'].queryset = Subject.objects.filter(user=user)       