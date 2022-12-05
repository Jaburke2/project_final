from django.contrib import admin
from . import models 
from  embed_video.admin  import  AdminVideoMixin
from .models  import Post, Profile, Cardio_Video, Strength_Video, Power_Video, Flex_Video
# Register your models here.
class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(models.Post)
admin.site.register(models.Category1)
admin.site.register(models.Category2)
admin.site.register(models.Comment)
admin.site.register(Cardio_Video)
admin.site.register(Strength_Video)
admin.site.register(Power_Video)
admin.site.register(Flex_Video)