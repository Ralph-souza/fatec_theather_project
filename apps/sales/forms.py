from django import forms

from apps.sales.models import SalesModel


class SalesForm(forms.ModelForm):
    movie = forms.ModelChoiceField(queryset=SalesModel.objects.all(), label="Movie")
    room = forms.ModelChoiceField(queryset=SalesModel.objects.all(), label="Room")
    price = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = SalesModel
        fields = ("movie", "room", "price")
        read_only_fields = ("created_at",)