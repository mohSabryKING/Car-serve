from rest_framework import serializers

from .models import *








class ModelName_ser0(serializers.ModelSerializer):

      
      class Meta:
            model = User_model
            fields = ('','','','','')









class ModelName_ser1(serializers.ModelSerializer):

      
      class Meta:
            model = Employee
            fields = ('','','','','')









class ModelName_ser2(serializers.ModelSerializer):

      
      class Meta:
            model = Customer
            fields = ('','','','','')









class ModelName_ser3(serializers.ModelSerializer):

      
      class Meta:
            model = Fix_center
            fields = ('','','','','')









class ModelName_ser4(serializers.ModelSerializer):

      
      class Meta:
            model = Car_name_with_panel
            fields = ('','','','','')









class Mark_name_ser(serializers.ModelSerializer):

      
      class Meta:
            model = Mark_name
            fields = ('','','','','')









class Car_Model_ser(serializers.ModelSerializer):

      
      class Meta:
            model = Car_Model
            fields = ('','','','','')









class Contract_ser(serializers.ModelSerializer):

      
      class Meta:
            model = Contract_model
            fields = ('','','','','')



