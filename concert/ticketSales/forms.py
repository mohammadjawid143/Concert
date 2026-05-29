from django import forms
from ticketSales.models import concertModel


class SearchForm(forms.Form):
    SearchText = forms.CharField(max_length=100, label="", required=False)


class concertFrom(forms.ModelForm):
    class Meta:
        model = concertModel
        fields = ['name', 'SingarName', 'lenth', 'poster', 'price']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}))
    SingarName = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100'}))
    lenth = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input100'}))
    poster = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'input100'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input100'}))
