from django.contrib import admin

from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    # list_display = ('first_name', 'last_name','student_id','quiz_type','quiz_name','correct_number','total_number','get_socre',
    # 'total_socre','mouse_move','mouse_click')
    list_display = [field.name for field in Question._meta.get_fields()]
    list_per_page = 25
  
admin.site.register(Question,QuestionAdmin)