from django.shortcuts import render, redirect, get_object_or_404
from .models import CashFlowRecord, Status, TransactionType, Category, Subcategory
from .forms import CashFlowRecordForm
from django import forms

# Формы для справочников
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'transaction_type']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

# Представления для записей ДДС
def record_list(request):
    records = CashFlowRecord.objects.all()
    if request.method == 'GET' and any(k in request.GET for k in ['date_from', 'date_to', 'status', 'transaction_type', 'category', 'subcategory']):
        # Фильтрация по дате
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        if date_from:
            records = records.filter(created_date__gte=date_from)
        if date_to:
            records = records.filter(created_date__lte=date_to)
        # Фильтрация по остальным полям
        status = request.GET.get('status')
        if status:
            records = records.filter(status__id=status)
        transaction_type = request.GET.get('transaction_type')
        if transaction_type:
            records = records.filter(transaction_type__id=transaction_type)
        category = request.GET.get('category')
        if category:
            records = records.filter(category__id=category)
        subcategory = request.GET.get('subcategory')
        if subcategory:
            records = records.filter(subcategory__id=subcategory)

    statuses = Status.objects.all()
    transaction_types = TransactionType.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'core/record_list.html', {
        'records': records,
        'statuses': statuses,
        'transaction_types': transaction_types,
        'categories': categories,
        'subcategories': subcategories,
    })

def record_create(request):
    if request.method == 'POST':
        form = CashFlowRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = CashFlowRecordForm()
    return render(request, 'core/record_form.html', {'form': form, 'title': 'Создать запись'})

def record_edit(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == 'POST':
        form = CashFlowRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = CashFlowRecordForm(instance=record)
    return render(request, 'core/record_form.html', {'form': form, 'title': 'Редактировать запись'})

def record_delete(request, pk):
    record = get_object_or_404(CashFlowRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'core/record_confirm_delete.html', {'record': record})

# Представления для справочников
def reference_list(request):
    statuses = Status.objects.all()
    types = TransactionType.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'core/reference_list.html', {
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    })

def status_add(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = StatusForm()
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Добавить статус'})

def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Редактировать статус'})

def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('reference_list')
    return render(request, 'core/reference_confirm_delete.html', {'object': status, 'type': 'статус'})

def type_add(request):
    if request.method == 'POST':
        form = TransactionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = TransactionTypeForm()
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Добавить тип'})

def type_edit(request, pk):
    type = get_object_or_404(TransactionType, pk=pk)
    if request.method == 'POST':
        form = TransactionTypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = TransactionTypeForm(instance=type)
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Редактировать тип'})

def type_delete(request, pk):
    type = get_object_or_404(TransactionType, pk=pk)
    if request.method == 'POST':
        type.delete()
        return redirect('reference_list')
    return render(request, 'core/reference_confirm_delete.html', {'object': type, 'type': 'тип'})

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = CategoryForm()
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Добавить категорию'})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Редактировать категорию'})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('reference_list')
    return render(request, 'core/reference_confirm_delete.html', {'object': category, 'type': 'категорию'})

def subcategory_add(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = SubcategoryForm()
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Добавить подкатегорию'})

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'core/reference_form.html', {'form': form, 'title': 'Редактировать подкатегорию'})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('reference_list')
    return render(request, 'core/reference_confirm_delete.html', {'object': subcategory, 'type': 'подкатегорию'})