from django import forms

class BinaryForm(forms.Form):
    binary = forms.CharField(
        label='Número binario',
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 101101'})
    )

    def clean_binary(self):
        b = self.cleaned_data['binary'].strip()
        if not b:
            raise forms.ValidationError("El campo no puede estar vacío.")
        if any(c not in '01' for c in b):
            raise forms.ValidationError("Sólo se permiten los dígitos 0 y 1.")
        return b
