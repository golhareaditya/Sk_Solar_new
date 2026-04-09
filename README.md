# sk_solar

Render deployment ke liye admin login enable karne ke liye ye environment variables set karein:

- `DJANGO_SUPERUSER_USERNAME`
- `DJANGO_SUPERUSER_EMAIL`
- `DJANGO_SUPERUSER_PASSWORD`

Deploy ke time `python manage.py ensure_admin_user` automatically admin account create ya update karega.
