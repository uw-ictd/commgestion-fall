from django import forms


class UserSearchTimeForm(forms.Form):
    from_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'id': "datepicker-from",
            'placeholder': 'Start Date',
        })
    )

    to_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'id': "datepicker-to",
            'placeholder': 'End Date',
        })
    )
