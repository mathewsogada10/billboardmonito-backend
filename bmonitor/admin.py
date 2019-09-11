from django.contrib import admin

# Register your models here.
from bmonitor.models import Town, MediaAgency, Client, Brand, BillBoard, Image, Competitor, Users, BillBoardBrand, BrandAgency, BoardSupplier

admin.site.register(Town)
admin.site.register(MediaAgency)
admin.site.register(Client)
admin.site.register(Brand)
admin.site.register(BillBoard)
admin.site.register(Image)
admin.site.register(Competitor)
admin.site.register(Users)
admin.site.register(BillBoardBrand)
admin.site.register(BrandAgency)
admin.site.register(BoardSupplier)
