from django import forms

from models import Atividade

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        
        
    # def clean_name(self):
    #     data = self.cleaned_data
        
    #     if TodoList.objects.filter (
    #         name=data['name']
    #     ).exists():
    #         raise forms.ValidationError (
    #             u'Nome ja existe'
    #         )
            
    #     return data['name']
        
        