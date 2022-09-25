from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SyllabusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Syllabus class"""

    queryset = models.Syllabus.objects.all()
    serializer_class = serializers.SyllabusSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Question class"""

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the User class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Course class"""

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Department class"""

    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class FacultiesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Faculties class"""

    queryset = models.Faculties.objects.all()
    serializer_class = serializers.FacultiesSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the Group class"""

    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class markRangeViewSet(viewsets.ModelViewSet):
    """ViewSet for the markRange class"""

    queryset = models.markRange.objects.all()
    serializer_class = serializers.markRangeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Permission class"""

    queryset = models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]


class contentTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the contentType class"""

    queryset = models.contentType.objects.all()
    serializer_class = serializers.contentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class logentryViewSet(viewsets.ModelViewSet):
    """ViewSet for the logentry class"""

    queryset = models.logentry.objects.all()
    serializer_class = serializers.logentrySerializer
    permission_classes = [permissions.IsAuthenticated]


class AbstractUserViewSet(viewsets.ModelViewSet):
    """ViewSet for the AbstractUser class"""

    queryset = models.AbstractUser.objects.all()
    serializer_class = serializers.AbstractUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class prevYearsQpViewSet(viewsets.ModelViewSet):
    """ViewSet for the prevYearsQp class"""

    queryset = models.prevYearsQp.objects.all()
    serializer_class = serializers.prevYearsQpSerializer
    permission_classes = [permissions.IsAuthenticated]
