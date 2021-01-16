from rest_framework import serializers
from .models import Student,Stage
from rest_framework.validators import UniqueTogetherValidator


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stage
        fields='__all__'

class DynamicFieldModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldModelSerializer,self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for remove_field in existing - allowed:
                self.fields.pop(remove_field)
        
    pass

class StudentSerializer(DynamicFieldModelSerializer):
    #stage = StageSerializer(read_only=True)
    def create(self, data):  #override the create of the current with the super with my data
#        data.update({'stage_id':3})
        data.update({'stage_id':data.get('stage').get('id')})
        data.pop('stage')

        return super(StudentSerializer, self).create(data)

    def update(self, instance, data):  #override the create of the current with the super with my data
        #data.update({'stage_id':data.get('stage').get('id')})
        instance.stage = data.get('stage') #data.get('stage').get('id')
        data.pop('stage')
        instance.save()    
        
        return instance #super(StudentSerializer, self).update(instance, data)

#python magic function for validation
    def validate_sage(self, value):
        if value<1:
            raise serializers.ValidationError('Name shouldn\'t be less than 1, you entered:'+ str(value))
        return value


    class Meta:
        #another way to validate using the builtin validators
        validators=[UniqueTogetherValidator(queryset=Student.objects.all(),fields=['sage','sname'])] #another way to validate using the builtin validators
        model=Student
        
        fields='__all__'




''' Task:
1. add field name= password
2. Post, to enter the password
3. Retrieve don't return the password
'''

