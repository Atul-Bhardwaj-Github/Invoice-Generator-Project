from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

from django.contrib import messages

# Create your views here.


def userlogin(request):
    if request.method=="POST":
        userName=request.POST.get('username')
        password=request.POST.get('password')

        Users=User()

        if User.objects.filter(username=userName).exists():
            # print("User verified")

            user=authenticate(username=userName,password=password)

            if user is None:
                # print("Invalid Password")
                messages.info(request, "Wrong Password")
                return redirect("/")
            else:
                login(request, user)
                print("Welcome",userName)
                return redirect("/home")

        else:
            messages.info(request, "Wrong Username")
            print("user not found")
            return redirect("/")
        


    form=UserLogin()
    context={
        "form":form
    }
    return render (request,"userlogin.html",context)


# --------------------------------------------------------------------------------------------------------------------


@login_required(login_url="/")
def home(request):
    return render(request,"index.html")



# --------------------------------------------------------------------------------------------------------------------



@login_required(login_url="/")
def logout_view(request):
    logout(request)
    return redirect("/")



# --------------------------------------------------------------------------------------------------------------------



@login_required(login_url="/")
def add_Client_Services(request):
    if request.method=="POST":
        if request.POST.get("company_name")!=None:

            company_name=request.POST.get("company_name")
            gst_no=request.POST.get("gst_no")
            country=request.POST.get("country")
            state=request.POST.get("state")
            address=request.POST.get("address")
            print(company_name,gst_no,country,state,address)

            clientObj=Client(company_name=company_name,gst_no=gst_no,country=country,state=state,address=address)
            clientObj.save()

        else:        
            client=Client.objects.get(id=request.POST.get("client"))
            description=request.POST.get("description")
            quantity=request.POST.get("quantity")
            amount=request.POST.get("amount")
            total_amount=int(quantity)*int(amount)
            print(client,description,quantity,amount,total_amount)

            serviceObj=Services(client=client,description=description,quantity=quantity,amount=amount)
            serviceObj.total_amount=int(quantity)*int(amount)
            serviceObj.save()
        print(request)

    clientform=Client_form()
    servicesform=Services_form()
    context={
        "user":request.user,
        "client_form":clientform,
        "services_form":servicesform
    }
    return render(request,"add_Client.html",context)




# --------------------------------------------------------------------------------------------------------------------



@login_required(login_url="/")
def serviceProvider(request):
    # ["client","company_name","handled_by","email","phone_no","account_no","ifsc_code","bank_name","gst_no"]
    if request.method=="POST":
        client=Client.objects.get(id=request.POST.get("client"))
        company_name=request.POST.get("company_name")
        handled_by=request.POST.get("handled_by")
        email=request.POST.get("email")
        phone_no=request.POST.get("phone_no")
        account_no=request.POST.get("account_no")
        ifsc_code=request.POST.get("ifsc_code")
        bank_name=request.POST.get("bank_name")
        gst_no=request.POST.get("gst_no")

        service_Provider=Service_Provider(client=client,company_name=company_name,handled_by=handled_by,email=email,phone_no=phone_no,account_no=account_no,ifsc_code=ifsc_code,bank_name=bank_name,gst_no=gst_no)
        service_Provider.save()

        return redirect("/serviceProvider")
        


    serviceProviders=Service_Provider.objects.all()
    form=Services_ProviderForm()

    context={
        "form":form,
        "serviceProviders":serviceProviders
    }
    return render(request,"serviceProvider.html",context)



@login_required(login_url="/")
def delete(request,id):
    obj=Service_Provider.objects.get(id=id)
    obj.delete()
    return redirect("/serviceProvider/")


@login_required(login_url="/")
def edit(request,id):

    if request.method=="POST":
        print(request.POST.get("handled_by"))

        obj=Service_Provider.objects.get(id=id)

        obj.client = Client.objects.get(id=request.POST.get("client"))
        obj.company_name = request.POST.get("company_name")
        obj.handled_by = request.POST.get("handled_by")
        obj.email = request.POST.get("email")
        obj.phone_no = request.POST.get("phone_no")
        obj.account_no = request.POST.get("account_no")
        obj.ifsc_code = request.POST.get("ifsc_code")
        obj.bank_name = request.POST.get("bank_name")
        obj.gst_no = request.POST.get("gst_no")

        obj.save()


        return redirect("/serviceProvider")

    context={
        "x":[1,2,3,4],
        "form":Services_ProviderForm(id)
    }
    return render(request,"edit.html",context)

# Inline formset factory



@login_required(login_url="/")
def display_clients(request):
    clients=Client.objects.all()
    context={
        "clients":clients
    }
    return render (request,"allList.html", context)

@login_required(login_url="/")
def All_report(request):
    clientobj=Client.objects.all

    context={
        "clientobj":clientobj,

    }
    return render(request,"All_report.html",context)


@login_required(login_url="/")
def delete_client (request,id):
    client=Client.objects.get(id=id)
    client.delete()
    return redirect(f"/allClient")


@login_required(login_url="/")
def edit_client (request,id):
    if request.method=="POST":
        client=Client.objects.get(id=id)

        client.company_name=request.POST.get("company_name")
        client.gst_no=request.POST.get("gst_no")
        client.country=request.POST.get("country")
        client.state=request.POST.get("state")
        client.address=request.POST.get("address")

        client.save()

        return redirect(f"/allClient")

    context={
        "form":Client_form(id),
        "address":Client.objects.get(id=id).address
    }
    return render(request,"edit.html",context)



@login_required(login_url="/")
def report(request,id):
    clientobj=Client.objects.get(id=id)
    try:
        service_providerObj=Service_Provider.objects.get(client_id=id)
    except:
        service_providerObj={"key":"value"}

    try:
        servicesobj=Services.objects.filter(client_id=id)
    except:
        servicesobj={"key":"value"}

    

    context={
        "clientobj":clientobj,
        "service_providerObj":service_providerObj,
        "servicesobj":servicesobj,
        # "servicetotal":total,
        # "GST": total*18/100,
        # "withGST":total+(total*18/100)
    }
    total=0
    for x in servicesobj:
        total+=x.amount*x.quantity
        context[f"serv{x.id}"]=x.amount*x.quantity
    context["servicetotal"]=total
    context["GST"]=total*18/100
    context["withGST"]=total+(total*18/100)

   
    return render(request,"report.html",context)



@login_required(login_url="/")
def show(request,id):
    clientobj=Client.objects.get(id=id)
    try:
        service_providerObj=Service_Provider.objects.get(client_id=id)
    except:
        service_providerObj={"key":"value"}

    try:
        servicesobj=Services.objects.filter(client_id=id)
    except:
        servicesobj={"key":"value"}

    

    context={
        "clientobj":clientobj,
        "service_providerObj":service_providerObj,
        "servicesobj":servicesobj,
    }

    return render(request,"show.html",context)


