from django import forms
from .models import Video


# define Video model form used to add new videos
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'url', 'notes']

# define search form that includes only a search textbox
class SearchForm(forms.Form):
    search_term = forms.CharField()