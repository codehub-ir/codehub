from django.contrib import messages 

def MarkApproved(modeladmin, request, queryset):
    queryset.update(is_valid = 'approved')
    messages.success(request, 'وضعیت {} تیکت به حالت "تایید شده" تغییر کرد'.format(queryset.count()))

def MarkRejected(modeladmin, request, queryset):
    queryset.update(is_valid = 'rejected')
    messages.success(request, 'وضعیت {} تیکت به حالت "رد شده" تغییر کرد'.format(queryset.count()))

def MarkPending(modeladmin, request, queryset):
    queryset.update(is_valid = 'pending')
    messages.success(request, 'وضعیت {} تیکت به حالت "در انتظار" تغییر کرد'.format(queryset.count()))
