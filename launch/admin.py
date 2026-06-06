# landing/admin.py

from django.contrib import admin
from .models import Feedback, Waitlist

admin.site.register(Feedback)
admin.site.register(Waitlist)