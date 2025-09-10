from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(CreateBlog)
admin.site.register(Wishlist)
admin.site.register(Likeuser)
admin.site.register(DisLikeuser)