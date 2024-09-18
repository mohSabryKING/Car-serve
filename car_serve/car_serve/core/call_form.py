from django import forms
from .models import *

              
              
              



class User_model_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = User_model
            fields = ()



               
            
              
              
              



class Employee_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Employee
            fields = ()



               
            
              
              
              



class Customer_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Customer
            fields = ()



               
            
              
              
              



class Fix_center_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Fix_center
            fields = ()



               
            
              
              
              



class Car_name_with_panel_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Car_name_with_panel
            fields = ()



               
            
              
              
              



class Mark_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Mark_name
            fields = ()



               
            
              
              
              



class Car_model_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Car_Model
            fields = ()



               
            
              
              
              



class Contract_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)  
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
         self.fields["field_model"].widget.attrs.update({"class": "item_img",'onClick':'get_item_img("id_field_model","show_field_model");'})
      

      class Meta:
            model = Contract_model
            fields = ()



               
            