from django import forms
from . import models



class ProjectCreateForms(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category','title','description']
        widgets = {

            'description': forms.Textarea(),
            'category': forms.Select(),
            'title': forms.Textarea()

        }

class ProjectUpdateForms(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category','title','status']
        widgets = {

            'status': forms.Select(),
            'category': forms.Select(),
            'title': forms.Textarea()

        }
