from django import forms
from .models import CashFlowRecord, Status, TransactionType, Category, Subcategory

class CashFlowRecordForm(forms.ModelForm):
    class Meta:
        model = CashFlowRecord
        fields = ['status', 'transaction_type', 'category', 'subcategory', 'amount', 'comment']  # Убрали 'created_date'
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтрация категорий по типу
        if 'transaction_type' in self.data:
            try:
                transaction_type_id = int(self.data.get('transaction_type'))
                self.fields['category'].queryset = Category.objects.filter(transaction_type_id=transaction_type_id)
            except (ValueError, TypeError):
                self.fields['category'].queryset = Category.objects.none()
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.transaction_type.categories.all()

        # Фильтрация подкатегорий по категории
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                self.fields['subcategory'].queryset = Subcategory.objects.none()
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()