"""


ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_SIGNUP_FIELDS = [
    "email*", "password1*", "password2*"
]

HEADLESS_ONLY = True
HEADLESS_FRONTEND_URLS = {
    "account_confirm_email":"/account/verify-email/{key}",
    "account_reset_password": "/account/password/reset",
    "account_reset_password_from_key": "/account/password/reset/key/{key}",
    "account_signup":"/account/signup",
    "socialaccount_login_error": "/account/provider/callback",
}

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:8000",]

CSRF_TRUSTED_ORIGINS = [
 "http://localhost:3000",
]


HEADLESS_SERVE_SPECIFICATION = True
MFA_SUPPORTED_TYPES = ["totp", "recovery_codes", "webauthn"]
MFA_PASSKEY_LOGIN_ENABLED = True

if not DEBUG:
    MFA_PASSKEY_SIGNUP_ENABLED = True
    ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True

if DEBUG:
   SESSION_COOKIE_SECURE = False
   CSRF_COOKIE_SECURE = False
   SESSION_COOKIE_SAMESITE = "Lax"
   CSRF_COOKIE_SAMESITE = "Lax"

ACCOUNT_LOGIN_BY_CODE_ENABLED = True

CSRF_COOKIE_SAMESITE = 'lax'

CRSF_COOKIE_SECURE = False

ACCOUNT_EMAIL_VERIFICATION = 'none'

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
      "rest_framework.authentication.SessionAuthentication",
      "rest_framework.authentication.TokenAuthentication", 
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_HEADERS = [
      'accept',
      'accept-encoding',
      'authorization',
      'content-type',
      'dnt',
      'origin',
      'user-agent',
      'x-csrftoken',
      'x-requested-with',
]

CORS_EXPOSE_HEADERS = ["Set-Cookie", "Authorization"]


CORS_ALLOW_METHODS = [
   'DELETE',
   'GET',
   'OPTIONS',
   'PATCH',
   'POST',
   'PUT',
]

ROOT_URLCONF = "backend.urls"

'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.dummy',
    'allauth.mfa',
    'allauth.headless',
    'allauth.usersessions',

"""