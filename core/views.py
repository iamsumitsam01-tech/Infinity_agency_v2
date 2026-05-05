from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import quote
from django.core.mail import send_mail
from .models import Service, Project, Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator




def home(request):
    return render(request, 'index.html')

def service(request):
    services = Service.objects.all()
    print(services)
    return render(request, 'service.html', {
        'services': services
    })

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def contact(request):
    if request.method == "POST":

        # ✅ GET DATA
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_message = request.POST.get('message')   # ✅ rename

        # ✅ SAVE IN DATABASE
        Contact.objects.create(
            name=name,
            email=email,
            message=user_message
        )

        # ✅ SEND EMAIL
        send_mail(
            "New Lead from Website",
            f"Name: {name}\nEmail: {email}\nMessage: {user_message}",
            settings.EMAIL_HOST_USER,
            ["iamsumitsam01@gmail.com"],  # 🔥 put your real email
            fail_silently=True
        )

        # ✅ SUCCESS MESSAGE
        messages.success(request, "Message sent successfully!")

        return redirect('contact')   # ✅ important

    return render(request, 'contact.html')

def update_status(request, id, status):
    contact = get_object_or_404(Contact, id=id)
    contact.status = status
    contact.save()
    return redirect('crm')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('crm')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def admin_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def crm(request):

    # 🔍 GET ALL CONTACTS
    contacts = Contact.objects.all()

    # 🔎 SEARCH
    query = request.GET.get('q')
    if query:
        contacts = contacts.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query)
        )

    # 🎯 STATUS FILTER
    status = request.GET.get('status')
    if status:
        contacts = contacts.filter(status=status)

    # 📊 ANALYTICS (IMPORTANT → BEFORE PAGINATION)
    total = Contact.objects.count()
    new = Contact.objects.filter(status='new').count()
    contacted = Contact.objects.filter(status='contacted').count()
    closed = Contact.objects.filter(status='closed').count()

    conversion_rate = int((closed / total) * 100) if total > 0 else 0

    # 📄 PAGINATION (AFTER FILTERS)
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    # 📦 SEND TO TEMPLATE
    context = {
        'contacts': contacts,
        'total': total,
        'new': new,
        'contacted': contacted,
        'closed': closed,
        'conversion_rate': conversion_rate
    }

    return render(request, 'crm.html', context)

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('crm')


import csv
from django.http import HttpResponse

def export_contacts(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Message', 'Status'])

    contacts = Contact.objects.all()

    for c in contacts:
        writer.writerow([c.name, c.email, c.message, c.status])

    return response

@login_required
def checkout(request):
    return render(request,
"checkout.html")

@login_required
def success(request):
    return render(request,
"success.html")