from rest_framework import serializers
from .models import PassengerComplaint
import datetime

class PassengerComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerComplaint
        fields = '__all__'

    # -------- Field-Level Validation --------
    def validate_user_phone_number(self, value):
        if not value.isdigit() or len(value) not in [10, 11, 12, 13, 14, 15]:
            raise serializers.ValidationError("Enter a valid phone number.")
        return value

    def validate_pnr(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("PNR should be exactly 10 characters.")
        return value

    def validate_train_no(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Train number must be numeric.")
        return value

    def validate_start_date_of_journey(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Start date of journey cannot be in the past.")
        return value

    # -------- Object-Level Validation --------
    def validate(self, attrs):
        if attrs.get('coach') and not attrs.get('berth'):
            raise serializers.ValidationError("If coach is provided, berth must also be provided.")
        return attrs
