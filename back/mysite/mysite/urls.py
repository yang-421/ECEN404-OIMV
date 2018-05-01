from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Super Exam System'
admin.site.index_title = 'Super Exam System'
admin.site.site_title = 'Super Exam System'

urlpatterns = [
    path('exams/', include('exams.urls')),
    path('admin/', admin.site.urls),
]