from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django_countries.fields import CountryField
               
               


detail_model="""  نحن نعتمد بشكل أساسي على التفكير الحر والإبداع المطلق والأفكار المبتكرة ونساعد على التفكير بشكل مختلف وبرؤية جديدة وتحقيق نتائج مثالية خالصة من خلال حرية التعبير، الإبداع هو وسيلتنا لتحقيق مهاراتنا"""


Position=[('موظف','موظف'),
          
          ('موظف','عميل'),


          ('صيانة','صيانة'),
          
          ]





class Mark_name(models.Model):
      #'name','model_made','mark_logo','detail',
      name=models.CharField(default="field",verbose_name='field', max_length=50)
      model_made=CountryField()
      mark_logo=models.ImageField(upload_to='mark_logo',verbose_name='mark logo',blank=True,null=True)
      detail=models.TextField(default=detail_model,verbose_name='details')
      

      def __str__(self):return self.name
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def country_made(self):return {'name':self.model_made.name,'flag':self.model_made.flag}
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Mark_name'
            verbose_name_plural = 'Mark_name'




class Car_Model(models.Model):
      #'belongs_to','name','car_img','speed','weight','color_code','detail'
      belongs_to=models.ForeignKey(Mark_name, related_name='belongs_to',blank=True,null=True, on_delete=models.CASCADE)
      name=models.CharField(default="model name",verbose_name='Elantra', max_length=50)
      car_img=models.ImageField(upload_to='car_image',verbose_name='car_image',blank=True,null=True)
      speed=models.IntegerField(default=120,verbose_name='speed in (Km/H)')
      weight=models.IntegerField(default=5,verbose_name='weight in (Toon)')
      color_code=models.CharField(default="#ff0000",verbose_name='color code(in Hex)', max_length=50)
      detail=models.TextField(default=detail_model,verbose_name='details')

      def __str__(self):return self.name
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Car_Model'
            verbose_name_plural = 'Car_Model'






class Car_name_with_panel(models.Model):
      #'hierd_car','panel_code'
      hierd_car=models.ForeignKey(Car_Model, related_name='hire_car',blank=True,null=True, on_delete=models.CASCADE)
      panel_code=models.CharField(default="152|ت ح م",verbose_name='panel code', max_length=15)

      def __str__(self):return self.panel_code
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Car_name_with_panel'
            verbose_name_plural = 'Car_name_with_panel'



   



class User_model(models.Model):
      #'user_key','name','phone','user_img','address','user_type'
      user_key=models.ForeignKey(User, related_name='user_key_1',blank=True,null=True, on_delete=models.CASCADE)
      name=models.CharField(default='mansor zaher',verbose_name='name', max_length=50)
      phone=PhoneNumberField(verbose_name='phone number',default="+201501029717")
      user_img=models.ImageField(upload_to='user_img',verbose_name='user image',blank=True,null=True)
      address=models.CharField(default='mansor zaher',verbose_name='name', max_length=40)
      user_type=models.CharField(default=Position[0],verbose_name='type',choices=Position, max_length=10)



      def __str__(self):
            return self.name
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'User_model'
            verbose_name_plural = 'User_model'



               
               
               
               



class Employee(models.Model):
      #'user_key','emp_email','salary'
      user_key=models.OneToOneField(User_model, related_name='user_key_2',blank=True,null=True, on_delete=models.CASCADE)
      emp_email=models.EmailField(default="myname@carserve.com",verbose_name='employee email', max_length=25)
      salary=models.PositiveIntegerField(default=10000,verbose_name="salary")



      def __str__(self):return self.user_key.name
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Employee'
            verbose_name_plural = 'Employee'



               
               
               
               



class Customer(models.Model):
      #'user_key','title','detail',
      user_key=models.OneToOneField(User_model, related_name='user_key_3',blank=True,null=True, on_delete=models.CASCADE)
      title=models.CharField(default="طلب ايجار سيارة",verbose_name='عنوان الطلب', max_length=50)
      detail=models.TextField(default=detail_model,verbose_name='تفاصيل الطلب')

      def __str__(self):return self.user_key.name
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Customer'
            verbose_name_plural = 'Customer'



               
               
               
               



class Fix_center(models.Model):
      user_key=models.OneToOneField(User_model, related_name='user_key_4',blank=True,null=True, on_delete=models.CASCADE)
      fixing_car_code=models.ForeignKey(Car_name_with_panel, related_name='fix_center_fix',blank=True,null=True, on_delete=models.CASCADE)
      title=models.CharField(default="تصليح كابوت أمامي",verbose_name='field', max_length=50)
      detail=models.TextField(default=detail_model,verbose_name='تفاصيل الطلب')

      def __str__(self):return self.title
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Fix_center'
            verbose_name_plural = 'Fix_center'



               
               
               
               


            
               
               
               




               
               
               



class Contract_model(models.Model):
      customer=models.ForeignKey(Customer, related_name='customer_hire',blank=True,null=True, on_delete=models.CASCADE)
      #fix_center=models.ForeignKey(Fix_center, related_name='fix_center_fix',blank=True,null=True, on_delete=models.CASCADE)
      
      made_in=models.DateTimeField(auto_now_add=True)
      detail=models.TextField(default=detail_model,max_length=500,verbose_name='تفاصيل العقد')


      def __str__(self):
            return self.customer.user_key.name
      
      def print_model_1(self):pass
      
      def print_model_2(self):pass
      
      def action_1(self):pass
      
      def action_2(self):pass
      
      def action_3(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Contract_model'
            verbose_name_plural = 'Contract_model'



               
               