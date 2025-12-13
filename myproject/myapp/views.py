from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from urllib.parse import urlencode
from django.http import JsonResponse,HttpResponse
# Create your views here.

def home(req):
    return HttpResponse("hello this is my home page")
def about(req):
    return HttpResponse("hello my na,e is ritu bisen this my about page ")
def my_render(req):
    return render(req,'landing.html')
    # data={'name':'ritu','age':20}
  
def my_redirect2(req):
    # return redirect("my_redirect3")
      x=reverse('my_redirect3')
      data=urlencode({'name':'ritu','age':20})
      return redirect(f'{x}?{data}')
def my_redirect3(req):
      n=req.GET.get('name')
      a=req.GET.get('age')
      print(n,a)
      return render(req,'redirectdata.html',{'x':n,'y':a})
    # return HttpResponse("helooo my page .....................")


    # json response

# def my_jsonresponse(req):
#      data=10
#     #  data={'x':True,"y":False,'''z''':None,'name':"ritu"}
#      return JsonResponse(data)



def my_jsonresponse(req):
    #  data=10
    # data=10.5+5j complex data ko json ke sath nhi bhej skte hai 
     data='string is serialazable'
     data=['list is serialazable'] # list
     data=('tuple is serialazable') # tuple
    # data={'set and frozenset is not  serialazable'}
   
     return JsonResponse(data,safe=False)