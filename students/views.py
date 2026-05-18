from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Students</h1>
        <p>Welcome to the students page.</p>
        <a href="/">Back to Home</a>
    """)
