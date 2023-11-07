from django import forms

from apps.movies.models import MoviesModel, RoomsModel


class MoviesForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Title")
    director = forms.CharField(max_length=100, label="Director")
    casting = forms.CharField(max_length=100, label="Casting")
    duration = forms.CharField(max_length=100, label="Duration")
    rating = forms.IntegerField()

    class Meta:
        model = MoviesModel
        fields = ("title", "director", "casting", "duration", "category", "rating")


class RoomsForm(forms.ModelForm):
    name = forms.CharField(label="Room")
    seats = forms.IntegerField(label="Seats")
    price = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = RoomsModel
        fields = ("name", "seats", "price")