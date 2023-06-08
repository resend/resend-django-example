import resend
from django.http import JsonResponse

def index(request):

    params = {
        "from": "onboarding@resend.dev",
        "to": "delivered@resend.dev",
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }

    r = resend.Emails.send(params)

    return JsonResponse(r)