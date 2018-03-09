from django.contrib import admin


from pizza_app.models import Address, PizzaIngredient, \
    PizzaMenuItem, PizzaSize, PizzaOrder

# Register your models here.

# PizzaIngredient
# PizzaMenuItem
# PizzaSize
# PizzaOrder

# list_display
# search
#


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full', )

admin.site.register(Address, AddressAdmin)


class PizzaIngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(PizzaIngredient, PizzaIngredientAdmin)

class PizzaMenuItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(PizzaMenuItem, PizzaMenuItemAdmin)

class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

admin.site.register(PizzaSize, PizzaSizeAdmin)

class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'kind',
                    'size', 'delivery', 'comment',
                    'delivered')
    list_editable = (
        'comment',
        'delivered',
    )
    list_filter = (
        'delivered',
    )

admin.site.register(PizzaOrder, PizzaOrderAdmin)


