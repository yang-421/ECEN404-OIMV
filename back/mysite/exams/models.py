from django.db import models


class Question(models.Model):
    first_name = models.CharField(max_length=20,default='rob')
    last_name = models.CharField(max_length=20,default='rob')
    student_id = models.PositiveSmallIntegerField(default=0)
    quiz_type = models.CharField(max_length=10,default='rob')
    quiz_name = models.CharField(max_length=20,default='rob')
    correct_questions  = models.PositiveSmallIntegerField(default=0)
    total_questions  = models.PositiveSmallIntegerField(default=0)
    got_socre = models.PositiveSmallIntegerField(default=0)
    total_socre = models.PositiveSmallIntegerField(default=0)
    mouse_clicks  = models.PositiveSmallIntegerField(default=0)
    pub_date = models.DateTimeField('date published',auto_now_add=True)


