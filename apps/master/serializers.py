from rest_framework import serializers
from apps.master.models import Master
from apps.master.permissions import UserPermission
from apps.users.models import User


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = [
            'first_name',
            'last_name',
            'description',
            'status',
            'gender',
            'languages',
            'experiance',
            'age'
        ]


class MasterRegisterSerializer(serializers.Serializer):
    permission_classes = [UserPermission]

    first_name = serializers.CharField(max_length=30, write_only=True)
    last_name = serializers.CharField(max_length=30, write_only=True)
    description = serializers.CharField(max_length=250, write_only=True)
    master_status = serializers.CharField(write_only=True)
    work_hours = serializers.CharField(write_only=True)
    language = serializers.CharField(max_length=30, write_only=True)
    experiance = serializers.CharField(max_length=20, write_only=True)
    gender = serializers.CharField(write_only=True)
    age = serializers.IntegerField()

    def validate(self, attrs):
        request = self.context.get('request')
        user_id = request.user.id
        user_instance = User.objects.get(id=user_id)
        master = Master(
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
            master_status=attrs['master_status'],
            description=attrs['description'],
            gender=attrs['gender'],
            work_hours=attrs['work_hours'],
            languages=attrs['language'],
            experiance=attrs['experiance'],
            age=attrs['age'],
            user=user_instance
        )
        master.save()
        return attrs


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMTE3NjI4LCJpYXQiOjE3MDIxMTA0MjgsImp0aSI6IjRiMDk1YWE3YTFhNDQyNWQ5MGUwNzBmYjMxOGEyNDk1IiwidXNlcl9pZCI6MX0.deUUkzsAzGOnSX8F2n6mB-RcSd0bI3Ju-4yNAsA5JIE

class MasterRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = [
            'first_name',
            'last_name',
            'description',
            'languages',
            'salon_id',
            'experiance',
            'age',
        ]
