from django.contrib import admin

# Register your models here.
from .models import User, Membership, Exchange, UserExchange

admin.site.register(User)
admin.site.register(Membership)
admin.site.register(Exchange)
admin.site.register(UserExchange)
