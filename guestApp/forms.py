from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Nazwa',
                                })
                            )
    comment = forms.CharField(max_length=120,
                            widget=forms.Textarea(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Komentarz',
                                })
                            )
    Botcatcher = forms.CharField(required = False,
                                widget=forms.TextInput(attrs={
                                    'type' : 'hidden',
                                    })
                                )