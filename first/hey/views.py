from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Stage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from elasticsearch_dsl import connections
from .search import StudentDocument
from .celery import cleanMe
# Create your views here.
def hello(request):
    # Stage.objects.create(sstage='SG')
    # Student.objects.create(sname='Hoso', sage=25, stage=Stage.objects.get(pk='1'))
    FREELANCER_DISPLAY_NAME = 'Djorge'
    EMPLOYER_LINK = 'https://hello.com'
    EMPLOYER_DISPLAY_NAME = 'Iyad Ahmad'
    JOB_LINK_PAGE = 'http://www.google.com'
    JOB_NAME='Translation of page'
    link = "https://www.baristahustle.com/"
    
    #txt2 = cleanMe.delay(f.text)
    txt2 = cleanMe.apply_async(queue='q1',kwargs={'link':link},priority=1)
        
    return render(request, 'hello.html',locals()) 

def retrieve(request):
    user_id = request.GET['user_id']
    if user_id is None:
        slist = Student.objects.all()
    else:
        slist = Student.objects.filter(pk=user_id)

    return render(request, 'slist.html', {'slist':slist})

def elastic_insert(request):
    connections.create_connection(hosts=['localhost'])
    student = StudentDocument(meta={'id':3})
    student.save()
    return render(request, 'hello.html')

@api_view(['GET'])
def retrieve_api(request):
    get_id = request.query_params.get('id')
    if get_id is None:
        slist = Student.objects.all()
    else:
        slist = Student.objects.filter(pk=get_id)

    data = StudentSerializer(slist, many=True)
    # k    # for x in slist:
    #     final_list.append({'sname':x.sname,'sage':x.sage})
    
    return Response({'slist':data.data})