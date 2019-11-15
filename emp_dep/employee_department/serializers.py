# from rest_framework import serializers
# from .models import Employee

# class EmployeeSerializer(serializers.Serializer):
#     e_id = serializers.IntegerField()
#     name = serializers.CharField()
#     contact = serializers.IntegerField()
#     salary = serializers.FloatField()
#     role = serializers.CharField()
#     department = serializers.IntegerField()

#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)



from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('e_id', 'name', 'contact', 'salary', 'role', 'department')

        def create(self, validated_data):
            return self.model.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.e_id = validated_data.get('e_id', instance.e_id)
            instance.name = validated_data.get('name', instance.name)
            instance.contact = validated_data.get('contact', instance.contact)
            instance.salary = validated_data.get('salary', instance.salary)
            instance.role = validated_data.get('role', instance.role)
            instance.department = validated_data.get('department', instance.department)

            instance.save()
            return instance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('d_id', 'd_name')
