from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string


def index(request):
    """
    Simple example using Django's send_mail() with Anymail + Resend backend.
    This is the standard Django way to send emails.

    Query parameters:
    - email: recipient email address (defaults to delivered@resend.dev)
    """
    try:
        # Get recipient email from query parameter, default to Resend test address
        recipient_email = request.GET.get('email', 'delivered@resend.dev')

        # If empty string provided, use default
        if not recipient_email:
            recipient_email = 'delivered@resend.dev'

        # Using Django's standard send_mail function
        num_sent = send_mail(
            subject="Hello from Django + Resend",
            message="This is a plain text message.",
            from_email="onboarding@resend.dev",
            recipient_list=[recipient_email],
            html_message="<strong>it works!</strong> This email was sent using Django's standard email API with Anymail and Resend.",
        )

        return JsonResponse({
            "success": True,
            "message": f"Email sent successfully using Django's email backend",
            "emails_sent": num_sent,
            "recipient": recipient_email
        })
    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=500)


def send_advanced_email(request):
    """
    Advanced example using EmailMessage with Django templates.
    This demonstrates the standard Django pattern for sending templated emails.

    Query parameters:
    - email: recipient email address (defaults to delivered@resend.dev)
    """
    try:
        # Get recipient email from query parameter, default to Resend test address
        recipient_email = request.GET.get('email', 'delivered@resend.dev')

        # If empty string provided, use default
        if not recipient_email:
            recipient_email = 'delivered@resend.dev'

        # Render the HTML email template with context data
        html_content = render_to_string('emails/welcome.html', {
            'user_name': 'Django Developer',
            'user_email': recipient_email,
            'dashboard_url': 'https://example.com/dashboard',
        })

        # Create an EmailMessage for more advanced features
        message = EmailMessage(
            subject="Welcome to Our Service!",
            body="Welcome! Please view this email in an HTML-capable client.",
            from_email="onboarding@resend.dev",
            to=[recipient_email],
        )

        # Add the rendered HTML content
        message.content_subtype = "html"
        message.body = html_content

        # Add Resend-specific tags using Anymail's esp_extra
        message.esp_extra = {
            "tags": [
                {"name": "category", "value": "welcome"},
                {"name": "environment", "value": "development"},
            ],
        }

        # Send the email
        message.send()

        return JsonResponse({
            "success": True,
            "message": "Template-based email sent successfully using Django templates",
            "recipient": recipient_email
        })
    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=500)