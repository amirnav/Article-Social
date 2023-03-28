from django import forms
from django.core.validators import ValidationError

from post.models import contact_us,article


#class ContactusForm(forms.Form):
#    name = forms.CharField(widget=forms.TextInput,required=True,label="First Name",max_length=30)
#    l_name=forms.CharField(widget=forms.TextInput,required=False,label="Last Name",max_length=50)
#    phone=PhoneNumberField(blank=True)
#    Email=forms.EmailField(label="Email")
#    title = forms.CharField(widget=forms.TextInput,label="Title Subject",max_length=200)
#    description = forms.CharField(widget=forms.Textarea,label="Message")
#
#    def clean(self):
#        name=self.cleaned_data.get("name")
#        l_name=self.cleaned_data.get("text")
#        if name == l_name:
#            raise ValidationError("Name and last name are same",code="text_name_same")

class ContactusForm(forms.ModelForm):
    class Meta:
        model=contact_us
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your name",
                "style":""
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your last name",
                "style": ""
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your last phone",
                "style": ""
            }),
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your title",
                "style": ""
            }),
            "Email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your Email",
                "style": ""
            }),
         
        }

class add_article(forms.ModelForm):
    class Meta:
        model=article
        fields=['title','body','image','slug',]
        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter title",
                "style":""
            }),

        }
