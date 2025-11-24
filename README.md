# Resend with Django (using django-anymail)

This example demonstrates how to integrate Resend with Django using **django-anymail**, which provides a Django email backend for Resend. This approach uses Django's standard email API (`send_mail()`, `EmailMessage`, etc.)

## Prerequisites

To get the most out of this guide, you'll need to:

- [Create an API key](https://resend.com/api-keys)
- [Verify your domain](https://resend.com/domains)
- Install `virtualenv` by running `pip install virtualenv`

## Instructions

1. Create and activate a new virtual env:

```sh
virtualenv venv
source venv/bin/activate
```

2. Install dependencies (includes django-anymail with Resend support):

```sh
pip install -r requirements.txt
```

3. Set your RESEND_API_KEY environment variable:

```sh
export RESEND_API_KEY="re_123456789"
```

4. Navigate to the Django project directory and run the development server:

```sh
cd resend_django_example
python manage.py runserver
```

5. Test the email endpoints using curl:

   **Simple email** (default recipient):

   ```sh
   curl -X POST http://127.0.0.1:8000/send/
   ```

   **Simple email** (custom recipient):

   ```sh
   curl -X POST -d "email=your-email@example.com" http://127.0.0.1:8000/send/
   ```

   **Template-based email** (default recipient):

   ```sh
   curl -X POST http://127.0.0.1:8000/template_send/
   ```

   **Template-based email** (custom recipient):

   ```sh
   curl -X POST -d "email=your-email@example.com" http://127.0.0.1:8000/template_send/
   ```

## What's Included

This example demonstrates three patterns for sending emails in Django:

### 1. Simple Email (`/send/` route)

Uses Django's `send_mail()` function - the simplest way to send emails in Django.

### 2. Template-Based Email (`/template_send/` route)

Shows how to use Django templates for email content with:

- Django's `render_to_string()` for template rendering
- `EmailMessage` class for more control
- Resend-specific features like tags via `esp_extra`

### 3. Email Template (`templates/emails/welcome.html`)

A reusable HTML email template that demonstrates:

- Template variables (user_name, user_email, etc.)
- Professional email styling
- Django template system integration

## Configuration

The django-anymail backend is configured in `settings.py`:

```python
# Add anymail to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'anymail',
]

# Configure Anymail with Resend backend
EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"

ANYMAIL = {
    "RESEND_API_KEY": os.environ.get("RESEND_API_KEY"),
}

DEFAULT_FROM_EMAIL = "onboarding@resend.dev"
```

## Learn More

- [django-anymail Documentation](https://anymail.dev/)
- [django-anymail Resend Backend](https://anymail.dev/en/stable/esps/resend/)
- [Django Email Documentation](https://docs.djangoproject.com/en/stable/topics/email/)
- [Resend Documentation](https://resend.com/docs)

## License

MIT License
