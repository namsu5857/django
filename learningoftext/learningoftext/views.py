#This is file is created by M Usman S
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse(" <h1>Asslam-0-Alaikum!Congratulation you have successfull in your work</h1> <a href='https://www.facebook.com/'>facebook</a> <a href='https://www.youtube.com/'>Youtube</a> <a href='https://www.google.com/'>Google</a>")
    return render(request,'index.html')

# def countcharcter(request):
#     return HttpResponse(" <h1>Asslam-0-Alaikum!Congratulation you have successfull to count charcters</h1>")


# def capitalizedchar(request):
#     return HttpResponse(" <h1>Asslam-0-Alaikum!Congratulation you have successfull to capitalized charcters</h1>")

# def removespace(request):
#     return HttpResponse(" <h1>Asslam-0-Alaikum!Congratulation you have successfull to remove spaces</h1> ")

# def addspace(request):
#     return HttpResponse(" <h1>Asslam-0-Alaikum!Congratulation you have successfull to add spaces</h1>")

# def lowerchar(request):
#     return HttpResponse(" <h1>Asslam-0-Alaikum!Congratulation you have successfull to add lowercase charcters")


# def tempimpot(request):
#     return render(request,'index.html')
    
def removepunc(request):
    djtext = request.GET.get('text', 'default')
    removedpunct = request.GET.get('removedpunct', 'off')
    
    if removedpunct == "on":
        analyzed = ''
        punctlist = '''!()-[]{};:'",<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctlist:
                analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
            return render(request, 'analyzed.html', params)
    else:
        return HttpResponse('Error')