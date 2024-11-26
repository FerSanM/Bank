from django.contrib import admin

from .models import BankAccountType, User, UserAddress, UserBankAccount, Banks


admin.site.register(BankAccountType)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(Banks)
#admin.site.register(UserBankAccount)