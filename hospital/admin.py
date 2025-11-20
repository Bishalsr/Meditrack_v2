from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalRecord
# Register your models here.
from .models import Feedback

admin.site.site_header = "MediTrack Admin"
admin.site.site_title = "MediTrack Admin Portal"
admin.site.index_title = "Welcome to MediTrack Admin"

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('submitted_at',)
    list_per_page = 10