import os
from django.template import Template, Context
from django.conf import settings
from django.core.mail import send_mail

def send_passenger_complaint_email(complain_details: dict):
    context = Context({
        "user_phone_number": complain_details.get('user_phone_number', ''),
        "passenger_name": complain_details.get('passenger_name', ''),
        "train_no": complain_details.get('train_no', ''),
        "train_name": complain_details.get('train_name', ''),
        "pnr": complain_details.get('pnr', ''),
        "berth": complain_details.get('berth', ''),
        "coach": complain_details.get('coach', ''),
        "complain_id": complain_details.get('complain_id', ''),
        "created_at": complain_details.get('created_at', ''),
        "start_date_of_journey": complain_details.get('start_date_of_journey', ''),
    })

    template_path = os.path.join(settings.BASE_DIR, "items", "templates", "complaint_creation_email_template.txt")

    if os.path.exists(template_path):
        with open(template_path, "r") as f:
            template_string = f.read()
    else:
        template_string = "Passenger Complaint Submitted\nComplaint ID: {{ complain_id }}"

    template = Template(template_string)
    message = template.render(context)

    send_mail(
        subject="Passenger Complaint Received",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[complain_details.get('to_email')],
        fail_silently=False,
    )