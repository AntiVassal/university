from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Users</h1>
        <p>Welcome to the users page.</p>
        <a href="/">Back to Home</a>
    """)
