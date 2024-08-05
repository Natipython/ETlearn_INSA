from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.

def main(request):
    return render(request, 'index.html', {})
def courses(request):
    course=Course.objects.all()
    return render(request, 'courses.html', {
        "courses": course
    })
def login(request):
    return render(request, 'login.html', {})




"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyB3wn8tCgLUZpKDC5UA04cDlxQXrv5ErYY")


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

)

chat_session = model.start_chat()
def ai_response(input):
    response = chat_session.send_message(input)
    return response.text


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def room(request, course):
    
    if request.method == 'POST':
        input_dat = request.POST.get('input_data')
        print(input_dat)
        res = ai_response(input_dat)
        response_data = {'message': res}
        return JsonResponse(response_data)
    message = ""
    if course.lower() in ["financing", "digital marketing", "front-end development", "computer science"]:
        message = f"{course} is coming soon! If you have any question about this course, Feel free to ask our AI."
    else:
        message = f"This course is not provided by us!"
    return render(request, 'room.html', {
        'msg': message,
        'course': course
    })


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            instance = form.save(commit=False)  
            sender_email = form.cleaned_data["gmail"]
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            subject = "Customer FeedBack Notice: " + subject
            recipient_list = ["nathnaelmogespy@gmail.com","nikodagm7@gmail.com"]
            send_mail(
                subject,
                f"Customer Name: {name}\n\n{message}",
                sender_email,
                recipient_list,
            )
            instance.save()  
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "contact.html", {

        "form": form,

        })



