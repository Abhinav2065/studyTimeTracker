from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Subject, Chapter
from .forms import SubjectForm, ChapterForm
from django.utils import timezone
from django.http import JsonResponse
import json

# Create your views here.


def home(request):
    return render(request, 'studyapp/home.html', {})


class CustomLoginView(LoginView):
    template_name = 'studyapp/custom_login.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the new user
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    
    return render(request, 'studyapp/register.html', {'form': form})


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Protect the page

    # Get all subjects that belong to the logged-in user
    user_subjects = Subject.objects.filter(user=request.user)

    context = {
        'subjects': user_subjects,
    }
    return render(request, 'studyapp/dashboard.html', context)

def addSubject(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Protect the page
    
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            # Don't save yet - add the user first
            subject = form.save(commit=False)
            subject.user = request.user  # Assign the subject to the current user
            subject.save()
            return redirect('dashboard')  # Redirect back to dashboard

    else:
        form = SubjectForm()


    return render(request, 'studyapp/add_subject.html', {'form': form})


def addChapter(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ChapterForm(request.user, request.POST)  # Pass user to form
        if form.is_valid():
            chapter = form.save()
            return redirect('dashboard')
    else:
        form = ChapterForm(request.user)  # Pass user to form

    return render(request, 'studyapp/add_chapter.html', {'form': form})


def study_session(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user_subjects = Subject.objects.filter(user=request.user)
    return render(request, 'studyapp/study_session.html', {'subjects': user_subjects})



def start_study_session(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        chapter_id = request.POST.get('chapter_id')
        # Here you would start tracking time (could use JavaScript + database)
        return JsonResponse({'status': 'started'})
    
    return JsonResponse({'status': 'error'})



def get_chapters(request):
    subject_id = request.GET.get('subject_id')
    chapters = Chapter.objects.filter(subject_id=subject_id).values('id', 'name')
    return JsonResponse({'chapters': list(chapters)})

def get_notes(request):
    chapter_id = request.GET.get('chapter_id')
    chapter = Chapter.objects.get(id=chapter_id)
    return JsonResponse({'notes': chapter.notes})



def save_notes(request):
    if request.method == 'POST':
        chapter_id = request.POST.get('chapter_id')
        notes = request.POST.get('notes')
        chapter = Chapter.objects.get(id=chapter_id)
        chapter.notes = notes
        chapter.save()
        return JsonResponse({'status': 'success'})



def save_study_time(request):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            chapter_id = data.get('chapter_id')
            time_studied = data.get('time_studied')
            
            chapter = Chapter.objects.get(id=chapter_id)
            # Add the new study time to existing time
            chapter.time_studied += time_studied
            chapter.save()
            
            # Also update the subject's total time
            subject = chapter.subject
            subject.total_time += time_studied
            subject.save()
            
            return JsonResponse({'status': 'success'})

            
        except (Chapter.DoesNotExist, ValueError):
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('dashboard')


