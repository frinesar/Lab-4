from cmath import e
from django.http import HttpResponse
from .models import Record


def index(request):
    Record.objects.create()    
    result = ''
    if len(Record.objects.all()) < 15:
        for record in Record.objects.order_by('-time_stamp'):
            result += str(record.time_stamp.strftime('%m/%d/%Y --- %H:%M:%S') + '\n')
    else:
        for record in Record.objects.order_by('-time_stamp')[:15:]:
            result += str(record.time_stamp.strftime('%m/%d/%Y --- %H:%M:%S') + '\n')
    return HttpResponse(str(result), content_type='text/plain; charset=utf-8')


    


