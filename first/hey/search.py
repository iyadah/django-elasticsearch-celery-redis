from elasticsearch_dsl import Document, connections
from .models import Student

class StudentDocument(Document):
    class Index:
        name = 'student_index'
        fields = ['id','sname']

    class Django:
        model = Student 


##connections.create_connection(hosts=['localhost'])

#StudentDocument.init()


