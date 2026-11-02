from django import forms
from .models import Service, Customer, Channel


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "customer",
            "channel",
            "service_type",
            "protocol",
            "public_ip",
            "port",
            "mode",
            "status",
            "notes",
        ]
        widgets = {
            "customer": forms.Select(attrs={"class": "form-select", "id": "id_customer"}),
            "channel": forms.Select(attrs={"class": "form-select", "id": "id_channel"}),
            "service_type": forms.Select(attrs={"class": "form-select"}),
            "protocol": forms.Select(attrs={"class": "form-select"}),
            "public_ip": forms.TextInput(attrs={"class": "form-control"}),
            "port": forms.NumberInput(attrs={"class": "form-control"}),
            "mode": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Customer name"})
        }


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Channel name"})
        }