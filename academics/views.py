from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Academics</h1>
        <p>Welcome to the academics page.</p>
        <a href="/">Back to Home</a>
    """)
