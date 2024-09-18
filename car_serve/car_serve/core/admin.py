from django.contrib import admin

from .models import *

class Admin_x0(admin.ModelAdmin):pass

admin.site.register(User_model,Admin_x0)




 

class Admin_x1(admin.ModelAdmin):pass

admin.site.register(Employee,Admin_x1)




 

class Admin_x2(admin.ModelAdmin):pass

admin.site.register(Customer,Admin_x2)




 

class Admin_x3(admin.ModelAdmin):pass

admin.site.register(Fix_center,Admin_x3)




 

class Admin_x4(admin.ModelAdmin):pass

admin.site.register(Car_name_with_panel,Admin_x4)




 

class Admin_x5(admin.ModelAdmin):pass

admin.site.register(Mark_name,Admin_x5)




 

class Admin_x6(admin.ModelAdmin):pass

admin.site.register(Car_Model,Admin_x6)




 

class Admin_x7(admin.ModelAdmin):pass

admin.site.register(Contract_model,Admin_x7)




 