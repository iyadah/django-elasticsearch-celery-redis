from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Student, Stage
from .serializer import StudentSerializer,StageSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        queryset = Student.objects.all()
        
        # queryset = Sutden.objects.filter...
        # return self.queryset
        #queryset.objects.values('id','sname','sage','stage')
        return queryset

    def list(self, requests, *args, **kwargs):
        #queryset.objects.values('id','sname','sage','stage')
        student_serializer = StudentSerializer(self.queryset,fields=['id','sname','sage','stage'], many=True).data

        #return super(StudentViewSet, self).get_list()
        return Response({'student_result':student_serializer})
    
    def create(self, requests):
        #requests.POST['stage']=1
        return super(StudentViewSet, self).create(requests)

    def retrieve(self, request, pk=None):
        return super(StudentViewSet, self).retrieve(request, pk)

    @action(methods=['get'], detail=True) #detail False without pk, and True: pk is a must
    def custom_function(self, requests, pk=1):
        return Response({'val1':'one', 'val2': 'two'})

    