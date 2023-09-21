from django.shortcuts import render, redirect
from django.contrib import messages
from realtors.models import Realtor
from django.core.mail import send_mail
from .models import Contact
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.decorators import login_required



@login_required
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']
    print(realtor_email)
    print(realtor_email)
    print(realtor_email)
    print(realtor_email)
    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)
    
    a=f"Inquiry has been made about {listing} "
    b=f"BY {name} "
    c=f"Contact Number {phone} "
    d=f"Message {message}."
    mail_content=f"{a},{b},{c},{d}"

    
    sender_address = 'saxenachitransh1610@gmail.com'
    sender_pass = 'majorproject@2021'
    receiver_address = realtor_email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A new enquiry has been made.'
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("saxenachitransh1610@gmail.com","majorproject@2021")

    server.sendmail("chitranshm1710@gmail.com",realtor_email,mail_content)
    server.quit()

    
    # Saving into database
    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
    contact.save()
    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)
