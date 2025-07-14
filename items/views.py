from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PassengerComplaint
from .serializers import PassengerComplaintSerializer


@api_view(['POST'])
def submit_complaint(request):
    serializer = PassengerComplaintSerializer(data=request.data)
    if serializer.is_valid():
        complaint = serializer.save()

        # Prepare context with individual fields for the email template
        context = {
            'complain_id': complaint.id,
            'created_at': complaint.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'passenger_name': complaint.passenger_name,
            'user_phone_number': complaint.user_phone_number,
            'train_no': complaint.train_no,
            'train_name': complaint.train_name,
            'start_date_of_journey': complaint.start_date_of_journey,
            'coach': complaint.coach,
            'berth': complaint.berth,
            'pnr': complaint.pnr,
            'description': complaint.description,
            'train_depo': complaint.train_depo,
        }

        # Render the email body using the template
        message = render_to_string('email/complaint_email.txt', context)

        # Send the email
        send_mail(
            subject='Passenger Complaint Submitted',
            message=message,
            from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings.py
            recipient_list=['kajalkhatri9373@gmail.com'],  # Update if needed
            fail_silently=False,
        )

        return Response({'message': 'Complaint submitted successfully.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
