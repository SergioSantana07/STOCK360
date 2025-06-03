from django import forms
from . import models

class InflowForm(forms.ModelForm):

   class Meta:
        model = models.Inflow
        fields = ['supplier','product','quantity','description',]
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # 'expiration_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
            # 'expiration_date': 'Validade',
        }