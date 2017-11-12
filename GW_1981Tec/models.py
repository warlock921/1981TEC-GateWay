from django.db import models
from django.utils import timezone

class System_config(models.Model):

	system_switch = models.BooleanField()
	system_language = models.CharField(max_length=200)
	system_name = models.CharField(max_length=200)
	system_register_switch = models.BooleanField()
	system_admin_email = models.EmailField()
	system_programing_language = models.CharField(max_length=45)
	system_upload_size = models.IntegerField()
	#系统上线时间
	system_online_time = models.DateTimeField(default=timezone.now)
	#系统维护时间
	system_maintain_time = models.DateTimeField(default=timezone.now)
	system_server = models.CharField(max_length=45)
	system_upfile_path = models.CharField(max_length=200)


    class Meta:
        verbose_name = "System_config"
        verbose_name_plural = "System_configs"

    def __str__(self):
        return "系统设置"


class System_plate(models.Model):

	system_plate_name = models.CharField(max_length=45)
	system_plate_index = models.IntegerField()
	system_plate_switch = models.BooleanField()

    class Meta:
        verbose_name = "System_plate"
        verbose_name_plural = "System_plates"

    def __str__(self):
        return self.system_plate_name

class User_login(models.Model):

	user_login_name = models.CharField(max_length=45)
	user_login_password = models.CharField(max_length=45)
	user_login_password_salt = models.CharField(max_length=200)
	user_login_age = models.IntegerField()
	user_login_sex = models.CharField(max_length=45)
	user_login_idcard = models.IntegerField(max_length=18)
	user_login_address = models.CharField(max_length=200)
	user_login_phone = models.IntegerField(max_length=11)
	user_login_time = models.DateTimeField(default=timezone.now)
	user_login_register_time = models.DateTimeField(default=timezone.now)
	user_login_out_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "User_login"
        verbose_name_plural = "User_logins"

    def __str__(self):
        return self.user_login_name

class MODELNAME(models.Model):

    class Meta:
        verbose_name = "MODELNAME"
        verbose_name_plural = "MODELNAMEs"

    def __str__(self):
        pass
    
    
    
    

