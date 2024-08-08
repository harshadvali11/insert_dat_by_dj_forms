from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topicname']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is Created')
    return render(request,'insert_topic.html',d)

def insert_topic_by_MF(request):
    ETFMO=TopicModelForm()
    d={'ETFMO':ETFMO}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Data is Inserted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_topic_by_MF.html',d)



def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']

            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
            WO.save()
            return HttpResponse('Webpage is Created')

    return render(request,'insert_webpage.html',d)

def insert_web_by_MF(request):
    d={'EWMFO':WebpageModelForm()}

    if request.method=='POST':
        WMFDO=WebpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('Webapge is created')
    return render(request,'insert_web_by_MF.html',d)
















