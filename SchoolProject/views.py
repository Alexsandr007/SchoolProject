from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        print(form_id)
        if form_id == 'test':
            form = TestForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('create_test')  # Перенаправляем на эту же страницу после регистрации
        elif form_id == 'question':
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('create_test')  # Перенаправляем на эту же страницу после регистрации
    else:
        test_form = TestForm()
        question_form = QuestionForm()
        return render(request, 'create_test.html', {'testForm': test_form, 'questionForm': question_form})


def get_tests(request):
    data = Test.objects.all().values()
    return JsonResponse(list(data), safe=False)


def get_questions(request, test_id):
    your_model_instance = Test.objects.get(id=test_id)
    related_model_instance = your_model_instance.question_set.filter(test_id=test_id).values()
    print(related_model_instance)
    return JsonResponse(list(related_model_instance), safe=False)
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
