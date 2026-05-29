from django.shortcuts import render
from site_model.models import site_setting
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import ContactMessage

# Create your views here.

def Contact_Us(request):
    about = site_setting.objects.all()
    
    context = {
        'About':about
    }
    return render(request,'site_model/Contact_Us.html',context)


def sent_message(request):
    if request.method == 'POST':
        # form data...................
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save data to databse
        contact_message = ContactMessage(
            name=name,
            surname=surname,
            email=email,
            subject=subject,
            message=message
        )
        contact_message.save()

        
        return JsonResponse({
                        'status': 'success',
                        'text': 'Successfully your massage sent!',
                        'confirm_button_text':'Ok',
                        'icon':'success'
                    })
    return render(request, 'site_model/Contact_Us.html')


def messages(request):
    Message = ContactMessage.objects.all()
    context = {
        'messages':Message
    }
    print(Message)
    return render(request,'site_model/messages.html',context)


from django.shortcuts import get_object_or_404, redirect
from .models import ContactMessage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def delete_message(request, message_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to delete messages.")
    
    message = get_object_or_404(ContactMessage, id=message_id)
    

    message.delete()

    return redirect('message')
