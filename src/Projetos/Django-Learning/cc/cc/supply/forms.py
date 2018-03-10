from django import forms

class MyModelForm(ModelForm):
    class Meta:
        model = Supply
        fields = ['vehicleType']