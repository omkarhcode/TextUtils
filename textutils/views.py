
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

def analyze(request):
	# Get the text
	djtext = request.POST.get('text', 'default')

	# Check checkbox values
	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')
	extraspaceremover = request.POST.get('extraspaceremover', 'off')
	charcount = request.POST.get('charcount', 'off')

	# Check if checkbox is on
	if removepunc == "on" and djtext:
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = ""
		for char in djtext:
			if char not in punctuations:
				analyzed += char
		params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
		djtext = analyzed
		
	if fullcaps == "on" and djtext:
		analyzed = ""
		for char in djtext:
			analyzed += char.upper()
		params = {'purpose': 'Changes to Uppercase', 'analyzed_text': analyzed}
		djtext = analyzed

	if newlineremover == "on" and djtext:
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != "\r":
				analyzed += char.upper()
		params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
		djtext = analyzed
		
	if extraspaceremover == "on" and djtext:
		analyzed = ""
		for index, char in enumerate(djtext):
			if not (djtext[index] == " " and djtext[index+1] == " "):
				analyzed += char
		params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
		djtext = analyzed
		
	if charcount == "on" and djtext:
		analyzed = len(djtext)
		params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
		djtext = analyzed
		
	if (removepunc == "on" or fullcaps == "on" or newlineremover == "on" or extraspaceremover == "on" ) and djtext:
		return render(request, 'analyze.html', params)
	else:
		return HttpResponse('Please Select any operation and try again!')

