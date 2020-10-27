from django.contrib import admin
from main.models import *

admin.site.register(user_info)
admin.site.register(exam_info)
admin.site.register(user_answer)
admin.site.register(Questions)
admin.site.register(img)

admin.site.register(submitted_user)

class UserScoreAdmin(admin.ModelAdmin):
    search_fields = ['FullName']

admin.site.register(user_score, UserScoreAdmin)