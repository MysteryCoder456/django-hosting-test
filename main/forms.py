from django import forms


class CreateListForm(forms.Form):
    id = forms.IntegerField(label="List ID")
    name = forms.CharField(label="Name", max_length=200)
    complete = forms.BooleanField(required=False)