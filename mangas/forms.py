from django import forms

from mangas.models import Manga



class MangaForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MangaForms, self).__init__(*args, **kwargs)
        self.fields['nombreM'].widget.attrs={
            'class': 'form-control col-md'
        }
        self.fields['autorM'].widget.attrs={
            'class': 'form-control col-md'
        }
        self.fields['descriptionM'].widget.attrs={
            'class': 'form-control col-md'
        }
        self.fields['generoM'].widget.attrs={
            'class': 'form-control col-md'
        }

        self.fields['manga_sta'].widget.attrs={
            'class': 'form-control col-md'
        }

        self.fields['rateM'].widget.attrs={
            'class': 'form-control col-md'

        }


        self.fields['volumen'].widget.attrs = {
            'class': 'form-control col-md'
        }

        self.fields['capitulos'].widget.attrs = {
            'class': 'form-control col-md'
        }

        self.fields['portadaManga'].widget.attrs = {
            'class': 'form-control col-md'
        }

    class Meta:
        model= Manga
        fields=('nombreM' , 'autorM', 'descriptionM', 'generoM', 'manga_sta', 'rateM',  'volumen','capitulos', 'portadaManga')
