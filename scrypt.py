from junvac.data import specialties, jobs, companies

from junvac.models import Speciality, Vacancy, Company


Speciality.objects.all().delete()
for speciality in specialties:
    Speciality.objects.create(code=speciality['code'],
                              title=speciality['title'],
                              picture='https://place-hold.it/100x60')
    #print(speciality, speciality_id)


Vacancy.objects.all().delete()
for job in jobs:
    Vacancy.objects.create(title=job['title'],
                           skills=job['cat'],
                           description=job['desc'],
                           salary_min=job['salary_from'],
                           salary_max=job['salary_to'],
                           published_at=job['posted'])



Company.objects.all().delete()
for company in companies:
    Company.objects.create(name=company['title'],
                           logo='https://place-hold.it/100x60')


for job in jobs:
    my_job=Vacancy.objects.filter(title=job['title']).first()
    my_comp=Company.objects.filter(name=job['company']).first()
    my_spec=Speciality.objects.filter(code=job['cat']).first()
    my_job.company=my_comp
    my_job.speciality=my_spec
    my_job.save()





print('export ok')
