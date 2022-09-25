from rest_framework import serializers

from . import models


class SyllabusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Syllabus
        fields = [
            "last_updated",
            "id",
            "course",
            "created",
            "subject",
        ]

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = [
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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "date_joined",
            "last_updated",
            "email",
            "name",
            "created",
            "id",
            "password",
            "username",
        ]

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = [
            "course",
            "active",
            "created",
            "semester",
            "department",
            "regulation",
            "last_updated",
            "id",
        ]

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = [
            "branch_code",
            "created",
            "degree",
            "last_updated",
            "id",
            "branch",
        ]

class FacultiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Faculties
        fields = [
            "id",
            "course",
            "last_updated",
            "subject",
            "created",
        ]

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = [
            "last_updated",
            "subjectName",
            "created",
            "co",
            "code",
        ]

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = [
            "name",
            "created",
            "id",
            "last_updated",
        ]

class markRangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.markRange
        fields = [
            "last_updated",
            "endField",
            "startRange",
            "id",
            "created",
        ]

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Permission
        fields = [
            "created",
            "name",
            "contentType",
            "codename",
            "last_updated",
        ]

class contentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.contentType
        fields = [
            "id",
            "model",
            "app_label",
            "created",
            "last_updated",
        ]

class logentrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.logentry
        fields = [
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

class AbstractUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AbstractUser
        fields = [
            "created",
            "email",
            "username",
            "last_updated",
            "password",
        ]

class prevYearsQpSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.prevYearsQp
        fields = [
            "year",
            "last_updated",
            "month",
            "created",
        ]
