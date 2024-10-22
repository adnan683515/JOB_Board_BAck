from rest_framework import serializers
from job.serializers import job_serializers,CompanySerializers
from .models import Apply
from job.models import JOB


class ApplySerializers(serializers.ModelSerializer):

    
    class Meta:
        model = Apply
        fields="__all__"
        read_only_fields=['user',]
        

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


from auth_app.serializers import user_serializer
class applyserilizers_seconde(serializers.ModelSerializer):
    job = job_serializers(read_only=True)
    user =user_serializer(read_only=True)
    class Meta:
        model = Apply
        fields = "__all__"
        
        

    
    
    
    
    
    
    
    


   