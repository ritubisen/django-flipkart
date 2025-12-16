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
    

        req.session['name']=n
        req.session['email']=e
    return render(req,'landing.html',{'msg':"data set succesfully"})
def get_data(req):
    n=req.session.get('name')
    e=req.session.get('email')
    data={'name':n,'email':e}
    return render(req,'landing.html',{'data':data,'msg1':"get data from session"})


def delete_data(req):
    if req.session.get('name') and req.session.get('email'):
        del req.session['name']
        del req.session['email']
        # req.session.flush()
        return render(req,'landing.html',{'msg2':"data deleted"})
    else:
        return render(req,'landing.html',{'msg2':"data not found"})
    