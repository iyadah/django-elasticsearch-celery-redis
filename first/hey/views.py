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
        
    return render(request, 'hello.html') 

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