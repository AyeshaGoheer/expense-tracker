from django.contrib import admin
from .models import Transaction, Category, Budget, Tag


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'description', 'date', 'category', 'amount')
    list_filter = ('user', 'date', 'category', 'transaction_type')
    search_fields = ('description', 'category__name', 'tags__name')
    list_per_page = 20

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        form.base_fields['user'].initial = request.user
        # form.base_fields['user'].widget.attrs['disabled'] = True
        form.base_fields['user'].widget.can_add_related = False
        form.base_fields['user'].widget.can_change_related = False
        form.base_fields['user'].widget.can_view_related = False
        return form


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(Tag)
