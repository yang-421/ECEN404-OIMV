from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Question

# Create your views here.
def index(request):
    print('')
    return JsonResponse({   
            'status': 'ok',
            'msg':'welcome'
        })

@csrf_exempt
def addQuiz(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        print(json_data)
        question = Question()
        question.first_name = json_data.get('first_name', None)
        question.last_name = json_data.get('last_name', None)
        question.student_id = json_data.get('student_id', None)
        question.quiz_type = json_data.get('quiz_type', None)
        question.quiz_name = json_data.get('quiz_name', None)
        question.correct_questions = json_data.get('correct_questions', None)
        question.total_questions = json_data.get('total_questions', None)
        question.got_socre = json_data.get('got_socre', None)
        question.total_socre = json_data.get('total_socre', None)
        question.mouse_moves = json_data.get('mouse_moves', None)
        question.mouse_clicks = json_data.get('mouse_clicks', None)
        question.save()
        print(question.first_name)
        res_json={
            'status':'ok',
            'data':json_data
        }
        return JsonResponse(res_json)
    