from django.contrib import admin
from .models import PassengerComplaint

@admin.register(PassengerComplaint)
class PassengerComplaintAdmin(admin.ModelAdmin):
    list_display = ['passenger_name', 'train_no', 'created_at']  # customize as needed
