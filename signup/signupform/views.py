from django.shortcuts import render
from signupform.models import Email_input, Name_input


def home_view(request):
    emails_list = Email_input.objects.all()
    
    if request.method == 'POST':
        email = request.POST.get('email', None)
        email_object = Email_input(email=email)
        
        if email_object.email in [i.email for i in emails_list]:
            Email_input.objects.filter(email=email)[0].delete()
        else:
            name = request.POST.get('name', None)
            if name in [i.name for i in Name_input.objects.all()]:
                existing_name = Name_input.objects.filter(name=name)[0]
                existing_name.email_input_set.create(email=email)
                existing_name.save()
            else:
                name_object = Name_input(name=name)
                name_object.save()
                name_object.email_input_set.create(email=email)
                name_object.save()
        
    return render(request, 'home.html', {'emails':Email_input.objects.all()})

