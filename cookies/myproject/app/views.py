from django.shortcuts import render

def landing(req):
    return render (req,'landing.html')


def set(req):
    return render(req,'set.html')

def set_data(req):
    if req.method== 'POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        print(n,e)
    

        response=render(req ,'landing.html',{'msg':"cookies set"})
        response.set_cookie('name',n)
        response.set_cookie('email',e)
        return response