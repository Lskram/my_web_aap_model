from django.shortcuts import render , HttpResponse

# Create your views here.

def Home (request):
    return render(request,"index.html")
def About(request):
    return HttpResponse ("นี่คือข้อมูลของฉันหากคุณกำลังตามหา...")
def Contact(request):
    return HttpResponse ("สามารถติดต่อฉันได้จากที่นี่...")
    
