from django import forms
from . import models


class SyllabusForm(forms.ModelForm):
    class Meta:
        model = models.Syllabus
        fields = [
            "syllabus",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "difficulty",
            "title",
            "difficulty",
            "question",
            "question",
            "slug",
            "answer",
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "date_joined",
            "email",
            "name",
            "password",
            "username",
            "users",
        ]


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = [
            "course",
            "active",
            "semester",
            "regulation",
        ]


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = [
            "branch_code",
            "degree",
            "branch",
            "dept",
        ]


class FacultiesForm(forms.ModelForm):
    class Meta:
        model = models.Faculties
        fields = [
            "faculties",
        ]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = [
            "subjectName",
            "co",
            "code",
            "questions",
            "subjects",
        ]


class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = [
            "name",
            "groups",
        ]


class markRangeForm(forms.ModelForm):
    class Meta:
        model = models.markRange
        fields = [
            "endField",
            "startRange",
        ]


class PermissionForm(forms.ModelForm):
    class Meta:
        model = models.Permission
        fields = [
            "name",
            "codename",
            "permissions(group)",
        ]


class contentTypeForm(forms.ModelForm):
    class Meta:
        model = models.contentType
        fields = [
            "model",
            "app_label",
            "contentType",
        ]


class logentryForm(forms.ModelForm):
    class Meta:
        model = models.logentry
        fields = [
            "objectId",
            "objectRepr",
            "change_message",
            "actionFlag",
            "actionTime",
        ]


class prevYearsQpForm(forms.ModelForm):
    class Meta:
        model = models.prevYearsQp
        fields = [
            "year",
            "month",
            "prevYrQp",
        ]
