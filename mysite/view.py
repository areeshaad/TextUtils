# I have created this file - areesha
from django.http import HttpResponse
from django.shortcuts import render

# -----------------Home page----------------------- #
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home</h1>")

# -----------Project starts from here-------------- #
def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    lower = request.POST.get('lower', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

# -------------------Remove Puntuations--------------------- #
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

# -------------------Uppercase--------------------- #
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Converted to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

# -------------------Lowercase--------------------- #
    if (lower == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Converted to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

# -------------------New line remover--------------------- #
    if (removenewline == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

# -------------------Remove extra spaces------------------- #
    if (removeextraspace == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

# -------------------Character counter------------------ #
    if (charcount == "on"):
        analyzed = ""
        char = str(len(djtext))
        analyzed = analyzed + char + " characters in your text"
        params = {'purpose': 'Character count', 'analyzed_text': analyzed}
        djtext = analyzed
    return render(request, 'analyze.html', params)

    if(charcount != "on" and removeextraspace != "on" and removenewline != "on" and lower != "on" and fullcaps != "on" and removepunc != "on"):
        return HttpResponse("ERR")
