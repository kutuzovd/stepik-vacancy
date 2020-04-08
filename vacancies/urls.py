"""vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin

from junvac.views import MainView, VacancyListView, CategoryListView,  OneVacancyView, OneCompanyView # ResumeSenderView, CompanyListView


urlpatterns = [
    path('admin/', admin.site.urls),
    #Пока статические маршруты, затем - откорректировать
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('jobs/cat/<str:spec_id>/', CategoryListView.as_view(), name='category'),
    path('companies/<int:comp_id>/', OneCompanyView.as_view(), name='company'),
    path('jobs/<int:vac_id>/', OneVacancyView.as_view(), name='onevacancy'),

#    path('jobs/22/send/', ResumeSenderView.as_view(), name='send'),
#    path('companies/', CompanyListView.as_view(), name='comp_list'),

]
