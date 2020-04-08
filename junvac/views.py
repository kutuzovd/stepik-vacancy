from django.shortcuts import render
from django.views import View
from django.db.models import Count
from junvac.models import Vacancy, Company, Speciality
# Create your views here.

#Обработчик главной страницы
class MainView(View):
    def get(self, request):
        #Аннотирование специализаций по числу вакансий
        spec_count = Speciality.objects.annotate(countvac=Count('speciality'))
        #Аннотирование компаний по числу вакансий
        comp_count=Company.objects.annotate(countcomp=Count('company'))
        return render(request, 'index.html', context={'comp_count': comp_count,
                                                      'spec_count' : spec_count})


#Обработчик показа листа всех вакансий
class VacancyListView(View):
    def get(self, request):
        #Получение всех вакансий
        all_vacancies = Vacancy.objects.all()
        #Подчет числа вакансий в базе
        vac_count = Vacancy.objects.all().count()
        #Просто название страницы
        title_page = 'Все вакансии'
        return render(request, 'list.html', context={'all_vacancies' : all_vacancies,
                                                     'title_page' : title_page,
                                                     'vac_count' : vac_count})


#Обработчик показа листа вакансий по категориям
class CategoryListView(View):
    def get(self, request, spec_id):
        vacancies_on_spec = Speciality.objects.filter(code=spec_id).first()
        all_vacancies=vacancies_on_spec.speciality.all()
        vac_count = vacancies_on_spec.speciality.all().count()
        title_page = Speciality.objects.filter(code=spec_id).first().title
        return render(request, 'list.html', context={'all_vacancies' : all_vacancies,
                                                     'title_page' : title_page,
                                                     'vac_count' : vac_count})


# class CompanyListView(View):
#     def get(self, request):
#         return render(request, 'list.html', context={})


#Обработчик показа одной вакансии
class OneVacancyView(View):
    def get(self, request, vac_id):
        vacancy_full = Vacancy.objects.get(id=vac_id)
        speciality_title = Vacancy.objects.get(id=vac_id).speciality.title
        company_data = Vacancy.objects.get(id=vac_id).company
        return render(request, 'vacancy.html', context={'vacancy_full' : vacancy_full,
                                                        'speciality_title' : speciality_title,
                                                        'company_data' : company_data})


#Обработчик показа одной компании
class OneCompanyView(View):
    def get(self, request, comp_id):
        get_company = Company.objects.get(id=comp_id)
        vacancies_for_comp = get_company.company.all()
        vac_count = get_company.company.all().count()
        return render(request, 'company.html', context={'vacancies_for_comp' : vacancies_for_comp,
                                                        'get_company' : get_company,
                                                        'vac_count' : vac_count})


#Обработчик отправки вакансии
# class ResumeSenderView(View):
#     def get(self, request):
#         return render(request, 'sent.html', context={})


