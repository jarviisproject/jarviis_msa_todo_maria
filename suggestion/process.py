from django.shortcuts import render


class Suggestion:
    def index(request):
        print(request.session.session_key)
        request.session['test'] = "hahaha"
        return render(request, 'sessiontest/index.html')