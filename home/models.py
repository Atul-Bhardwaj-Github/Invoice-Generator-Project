from django.db import models

# Create your models here.

class Client(models.Model):
    # [company_name,gst_no,country,state,address,created_at]
    company_name=models.CharField( max_length=50)
    gst_no=models.CharField( max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField( max_length=50)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} --{self.gst_no}"

class Services(models.Model):
    # [client,description,description,quantity,amount,delivered_at]
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    description=models.TextField()
    quantity=models.IntegerField()
    amount=models.IntegerField()
    total_amount=models.IntegerField()
    delivered_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" {self.description[:20]}"
    
    
class Service_Provider(models.Model):
    # [client,company_name,handled_by,email,phone_no,account_no,ifsc_code,bank_name,gst_no,delivered_at,]
    
    client=models.OneToOneField(Client, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    handled_by=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    phone_no=models.IntegerField()
    account_no=models.IntegerField()
    ifsc_code=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    gst_no=models.CharField(max_length=50)
    delivered_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" {self.company_name}--{self.handled_by}"