from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from studyapp.views import CustomLoginView, register, dashboard, addSubject, addChapter, study_session, get_chapters, get_notes, save_notes, start_study_session, save_study_time

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('accounts/register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-subject/', addSubject, name='add_subject'),
    path('add-chapter/', addChapter, name='add_chapter'),
    path('study-session/', study_session, name='study_session'),
    path('get-chapters/', get_chapters, name='get_chapters'),
    path('get-notes/', get_notes, name='get_notes'),
    path('save-notes/', save_notes, name='save_notes'),
    path('start-study/', start_study_session, name='start_study'),
    path('save-study-time/', save_study_time, name='save_study_time'), 
    ]
