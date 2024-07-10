from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import  *


class UserLogin (AuthenticationForm,forms.ModelForm):
    
    class Meta:
        model=User
        fields=["username","password"]

    labels={
        "username":"UserID",
        "password":"Password"
    }

    def __init__(self,*args,**kwargs):
        super(UserLogin,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['class']='form-control'



class Client_form(forms.ModelForm):
    class Meta:
        model=Client
        fields=["company_name","gst_no","country","state","address"]

    labels={
        "company_name":"Company Name",
        "gst_no":"GST Number",
        "country":"Country",
        "state":"State",
        "address":"address"
    }

    def __init__(self,id=None,*args,**kwargs):
        super(Client_form,self).__init__(*args,**kwargs)

        self.fields['company_name'].widget.attrs['class']='form-control'
        self.fields['gst_no'].widget.attrs['class']='form-control'
        self.fields['country'].widget.attrs['class']='form-control'
        self.fields['state'].widget.attrs['class']='form-control'
        self.fields['address'].widget.attrs['class']='form-control'

        if id !=None:
            self.fields['company_name'].widget.attrs['value']=Client.objects.get(id=id).company_name
            self.fields['gst_no'].widget.attrs['value']=Client.objects.get(id=id).gst_no
            self.fields['country'].widget.attrs['value']=Client.objects.get(id=id).country
            self.fields['state'].widget.attrs['value']=Client.objects.get(id=id).state
            self.fields['address'].widget.attrs['id']="address"



class Services_form(forms.ModelForm):
    class Meta:
        model=Services
        fields=["client","description","quantity","amount"]

    labels={
        "client":"Client",
        "description":"Description",
        "quantity":"Quantity",
        "amount":"Unit Amount"
    }

    def __init__(self,*args,**kwargs):
        super(Services_form,self).__init__(*args,**kwargs)

        self.fields['client'].widget.attrs['class']='form-control'
        self.fields['description'].widget.attrs['class']='form-control'
        self.fields['quantity'].widget.attrs['class']='form-control'
        self.fields['amount'].widget.attrs['class']='form-control'



class Services_ProviderForm(forms.ModelForm):
    class Meta:
        model=Service_Provider
        fields=["client","company_name","handled_by","email","phone_no","account_no","ifsc_code","bank_name","gst_no"]


    def __init__(self,id=None,*args,**kwargs):
        super(Services_ProviderForm,self).__init__(*args,**kwargs)

        self.fields['client'].widget.attrs['class']='form-control'
        self.fields['company_name'].widget.attrs['class']='form-control'
        self.fields['handled_by'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['phone_no'].widget.attrs['class']='form-control'
        self.fields['account_no'].widget.attrs['class']='form-control'
        self.fields['ifsc_code'].widget.attrs['class']='form-control'
        self.fields['bank_name'].widget.attrs['class']='form-control'
        self.fields['gst_no'].widget.attrs['class']='form-control'

        if id != None:
            self.fields['client'].widget.attrs['value']=Service_Provider.objects.get(id=id).client
            self.fields['company_name'].widget.attrs['value']=Service_Provider.objects.get(id=id).company_name
            self.fields['handled_by'].widget.attrs['value']=Service_Provider.objects.get(id=id).handled_by
            self.fields['email'].widget.attrs['value']=Service_Provider.objects.get(id=id).email
            self.fields['phone_no'].widget.attrs['value']=Service_Provider.objects.get(id=id).phone_no
            self.fields['account_no'].widget.attrs['value']=Service_Provider.objects.get(id=id).account_no
            self.fields['ifsc_code'].widget.attrs['value']=Service_Provider.objects.get(id=id).ifsc_code
            self.fields['bank_name'].widget.attrs['value']=Service_Provider.objects.get(id=id).bank_name
            self.fields['gst_no'].widget.attrs['value']=Service_Provider.objects.get(id=id).gst_no



