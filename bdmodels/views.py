from django.shortcuts import render, redirect
from .models import *
from .form import *
# Create your views here.
def index(req):
    forma = Personforma()
    bd = Person.objects.all()
    print(bd)
    print(Person.objects.get(id=3).name, Person.objects.get(id=3).age)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    for p in Person.objects.all():
        print(p.name, p.age, p.id)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    igors = Person.objects.filter(name='рекс')
    print(igors.values())
    print(igors.values_list())
    print(igors.in_bulk())
    print(Person.objects.filter(name='Igor',age='22'))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    qqq = Person.objects.exclude(name='Igor').exclude(age=22)
    print(qqq.values_list())
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    qqq = Person.objects.filter(name='Vlad')
    print(qqq.values_list())
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    k1 = Product.objects.create(title='confeta', price=50.00, company_id=2)
    k2 = Product.objects.create(title='confetaBIG', price=15.00, company_id=2)
    print(k2.company.name)
    shokoladki = Product.objects.filter(company__name='Mars')
    print(shokoladki.values_list())
    data = {'forma': forma, 'database': bd}
    return render(req, 'index.html', context=data)

def add1(req):
    man = Person()                                        #1вариант создания
    man.name = 'Igor'
    man.age = 22
    man.save()
    man2 = Person.objects.create(name='Vlad', age=13)      #2вариант создания
    return redirect('home')


def create(req):
    if req.POST:
        man = Person()
        man.name = req.POST.get('name1')
        man.age = req.POST.get('age1')
        man.save()
        return redirect('home')

def delete(req,ids):
    man = Person.objects.get(id=ids)
    man.delete()
    return redirect('home')

def edit(req,ids):
    man = Person.objects.get(id=ids)
    anketa = Personforma()
    data = {'forma': anketa}
    if req.POST:
        man.name = req.POST['name1']
        man.age = req.POST['age1']
        man.save()
        return redirect('home')
    else:
        return render(req, 'edit.html', context=data)
