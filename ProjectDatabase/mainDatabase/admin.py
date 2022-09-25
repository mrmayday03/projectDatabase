from django.contrib import admin
from django import forms

from . import models


class SyllabusAdminForm(forms.ModelForm):

    class Meta:
        model = models.Syllabus
        fields = "__all__"


class SyllabusAdmin(admin.ModelAdmin):
    form = SyllabusAdminForm
    list_display = [
        "last_updated",
        "id",
        "course",
        "created",
        "subject",
    ]
    readonly_fields = [
        "last_updated",
        "id",
        "course",
        "created",
        "subject",
    ]


class QuestionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = [
        "mark",
        "difficulty",
        "title",
        "difficulty",
        "id",
        "question",
        "subject",
        "question",
        "created",
        "slug",
        "answer",
        "last_updated",
    ]
    readonly_fields = [
        "mark",
        "difficulty",
        "title",
        "difficulty",
        "id",
        "question",
        "subject",
        "question",
        "created",
        "slug",
        "answer",
        "last_updated",
    ]


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = "__all__"


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = [
        "date_joined",
        "last_updated",
        "email",
        "name",
        "created",
        "id",
        "password",
        "username",
    ]
    readonly_fields = [
        "date_joined",
        "last_updated",
        "email",
        "name",
        "created",
        "id",
        "password",
        "username",
    ]


class CourseAdminForm(forms.ModelForm):

    class Meta:
        model = models.Course
        fields = "__all__"


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = [
        "course",
        "active",
        "created",
        "semester",
        "department",
        "regulation",
        "last_updated",
        "id",
    ]
    readonly_fields = [
        "course",
        "active",
        "created",
        "semester",
        "department",
        "regulation",
        "last_updated",
        "id",
    ]


class DepartmentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Department
        fields = "__all__"


class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm
    list_display = [
        "branch_code",
        "created",
        "degree",
        "last_updated",
        "id",
        "branch",
    ]
    readonly_fields = [
        "branch_code",
        "created",
        "degree",
        "last_updated",
        "id",
        "branch",
    ]


class FacultiesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Faculties
        fields = "__all__"


class FacultiesAdmin(admin.ModelAdmin):
    form = FacultiesAdminForm
    list_display = [
        "id",
        "course",
        "last_updated",
        "subject",
        "created",
    ]
    readonly_fields = [
        "id",
        "course",
        "last_updated",
        "subject",
        "created",
    ]


class SubjectAdminForm(forms.ModelForm):

    class Meta:
        model = models.Subject
        fields = "__all__"


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = [
        "last_updated",
        "subjectName",
        "created",
        "co",
        "code",
    ]
    readonly_fields = [
        "last_updated",
        "subjectName",
        "created",
        "co",
        "code",
    ]


class GroupAdminForm(forms.ModelForm):

    class Meta:
        model = models.Group
        fields = "__all__"


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = [
        "name",
        "created",
        "id",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "created",
        "id",
        "last_updated",
    ]


class markRangeAdminForm(forms.ModelForm):

    class Meta:
        model = models.markRange
        fields = "__all__"


class markRangeAdmin(admin.ModelAdmin):
    form = markRangeAdminForm
    list_display = [
        "last_updated",
        "endField",
        "startRange",
        "id",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "endField",
        "startRange",
        "id",
        "created",
    ]


class PermissionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Permission
        fields = "__all__"


class PermissionAdmin(admin.ModelAdmin):
    form = PermissionAdminForm
    list_display = [
        "created",
        "name",
        "contentType",
        "codename",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "name",
        "contentType",
        "codename",
        "last_updated",
    ]


class contentTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.contentType
        fields = "__all__"


class contentTypeAdmin(admin.ModelAdmin):
    form = contentTypeAdminForm
    list_display = [
        "id",
        "model",
        "app_label",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "id",
        "model",
        "app_label",
        "created",
        "last_updated",
    ]


class logentryAdminForm(forms.ModelForm):

    class Meta:
        model = models.logentry
        fields = "__all__"


class logentryAdmin(admin.ModelAdmin):
    form = logentryAdminForm
    list_display = [
        "objectId",
        "objectRepr",
        "change_message",
        "actionFlag",
        "last_updated",
        "id",
        "actionTime",
        "user",
        "contentType",
        "created",
    ]
    readonly_fields = [
        "objectId",
        "objectRepr",
        "change_message",
        "actionFlag",
        "last_updated",
        "id",
        "actionTime",
        "user",
        "contentType",
        "created",
    ]


class AbstractUserAdminForm(forms.ModelForm):

    class Meta:
        model = models.AbstractUser
        fields = "__all__"


class AbstractUserAdmin(admin.ModelAdmin):
    form = AbstractUserAdminForm
    list_display = [
        "created",
        "email",
        "username",
        "last_updated",
        "password",
    ]
    readonly_fields = [
        "created",
        "email",
        "username",
        "last_updated",
        "password",
    ]


class prevYearsQpAdminForm(forms.ModelForm):

    class Meta:
        model = models.prevYearsQp
        fields = "__all__"


class prevYearsQpAdmin(admin.ModelAdmin):
    form = prevYearsQpAdminForm
    list_display = [
        "year",
        "last_updated",
        "month",
        "created",
    ]
    readonly_fields = [
        "year",
        "last_updated",
        "month",
        "created",
    ]


admin.site.register(models.Syllabus, SyllabusAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Faculties, FacultiesAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.markRange, markRangeAdmin)
admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.contentType, contentTypeAdmin)
admin.site.register(models.logentry, logentryAdmin)
admin.site.register(models.AbstractUser, AbstractUserAdmin)
admin.site.register(models.prevYearsQp, prevYearsQpAdmin)
