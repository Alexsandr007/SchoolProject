from django.shortcuts import render, redirect
from .models import Student, Question, Test
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import QuestionForm

def student_list_and_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Перенаправляем на эту же страницу после регистрации
    else:
        form = StudentForm()

    students = Student.objects.all()
    context = {'students': students, 'form': form}
    return render(request, 'list_students.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def create_test(request):
    testForm = TestForm()
    questionForm = QuestionForm()
    return render(request, 'create_test.html', {'testForm': testForm,'questionForm':questionForm})

def get_tests(request):
    data = Test.objects.all().values()
    return JsonResponse(list(data), safe=False)

def get_questions(request):
    data = Question.objects.all().values()
    return JsonResponse(list(data), safe=False)
# def get_question(request):
#     if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save()
#             return JsonResponse({'question_text': question.text})
#     else:
#         form = QuestionForm()
#         serialized_data = {
#             'text': form.cleaned_data['text'],
#             # Добавьте другие поля формы
#         }
#         return JsonResponse({'form_data': serialized_data})

def home(request):
    return render(request, 'home.html')
