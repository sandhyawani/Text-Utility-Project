#created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount','off')
    firstcap=request.POST.get('firstcap','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
       
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
             analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
     
    if(extraspaceremover=="on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
              analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext=analyzed
   
    if charcount == 'on':
        analyzed=('No. of characters given in the text are : '+ str(len(djtext.replace(' ',''))))
        params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
        djtext=analyzed

    if firstcap=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.lower()
        params={'purpose':' Your Text has been converted in lowercase','analyzed_text':analyzed}    

    if(removepunc !="on" and fullcaps!="on" and extraspaceremover!="on"  and  newlineremover != "on" and charcount != 'on' and firstcap!="on"): 
        return HttpResponse("UnboundLocalError at /analyze please select valid option to analyze your text ")  
       
    return render (request, 'analyze.html', params)
