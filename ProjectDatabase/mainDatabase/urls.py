from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Syllabus", api.SyllabusViewSet)
router.register("Question", api.QuestionViewSet)
router.register("User", api.UserViewSet)
router.register("Course", api.CourseViewSet)
router.register("Department", api.DepartmentViewSet)
router.register("Faculties", api.FacultiesViewSet)
router.register("Subject", api.SubjectViewSet)
router.register("Group", api.GroupViewSet)
router.register("markRange", api.markRangeViewSet)
router.register("Permission", api.PermissionViewSet)
router.register("contentType", api.contentTypeViewSet)
router.register("logentry", api.logentryViewSet)
router.register("AbstractUser", api.AbstractUserViewSet)
router.register("prevYearsQp", api.prevYearsQpViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("mainDatabase/Syllabus/", views.SyllabusListView.as_view(), name="mainDatabase_Syllabus_list"),
    path("mainDatabase/Syllabus/create/", views.SyllabusCreateView.as_view(), name="mainDatabase_Syllabus_create"),
    path("mainDatabase/Syllabus/detail/<int:id>/", views.SyllabusDetailView.as_view(), name="mainDatabase_Syllabus_detail"),
    path("mainDatabase/Syllabus/update/<int:id>/", views.SyllabusUpdateView.as_view(), name="mainDatabase_Syllabus_update"),
    path("mainDatabase/Syllabus/delete/<int:id>/", views.SyllabusDeleteView.as_view(), name="mainDatabase_Syllabus_delete"),
    path("mainDatabase/Question/", views.QuestionListView.as_view(), name="mainDatabase_Question_list"),
    path("mainDatabase/Question/create/", views.QuestionCreateView.as_view(), name="mainDatabase_Question_create"),
    path("mainDatabase/Question/detail/<slug:slug>/", views.QuestionDetailView.as_view(), name="mainDatabase_Question_detail"),
    path("mainDatabase/Question/update/<slug:slug>/", views.QuestionUpdateView.as_view(), name="mainDatabase_Question_update"),
    path("mainDatabase/Question/delete/<slug:slug>/", views.QuestionDeleteView.as_view(), name="mainDatabase_Question_delete"),
    path("mainDatabase/User/", views.UserListView.as_view(), name="mainDatabase_User_list"),
    path("mainDatabase/User/create/", views.UserCreateView.as_view(), name="mainDatabase_User_create"),
    path("mainDatabase/User/detail/<int:id>/", views.UserDetailView.as_view(), name="mainDatabase_User_detail"),
    path("mainDatabase/User/update/<int:id>/", views.UserUpdateView.as_view(), name="mainDatabase_User_update"),
    path("mainDatabase/User/delete/<int:id>/", views.UserDeleteView.as_view(), name="mainDatabase_User_delete"),
    path("mainDatabase/Course/", views.CourseListView.as_view(), name="mainDatabase_Course_list"),
    path("mainDatabase/Course/create/", views.CourseCreateView.as_view(), name="mainDatabase_Course_create"),
    path("mainDatabase/Course/detail/<int:id>/", views.CourseDetailView.as_view(), name="mainDatabase_Course_detail"),
    path("mainDatabase/Course/update/<int:id>/", views.CourseUpdateView.as_view(), name="mainDatabase_Course_update"),
    path("mainDatabase/Course/delete/<int:id>/", views.CourseDeleteView.as_view(), name="mainDatabase_Course_delete"),
    path("mainDatabase/Department/", views.DepartmentListView.as_view(), name="mainDatabase_Department_list"),
    path("mainDatabase/Department/create/", views.DepartmentCreateView.as_view(), name="mainDatabase_Department_create"),
    path("mainDatabase/Department/detail/<int:id>/", views.DepartmentDetailView.as_view(), name="mainDatabase_Department_detail"),
    path("mainDatabase/Department/update/<int:id>/", views.DepartmentUpdateView.as_view(), name="mainDatabase_Department_update"),
    path("mainDatabase/Department/delete/<int:id>/", views.DepartmentDeleteView.as_view(), name="mainDatabase_Department_delete"),
    path("mainDatabase/Faculties/", views.FacultiesListView.as_view(), name="mainDatabase_Faculties_list"),
    path("mainDatabase/Faculties/create/", views.FacultiesCreateView.as_view(), name="mainDatabase_Faculties_create"),
    path("mainDatabase/Faculties/detail/<int:id>/", views.FacultiesDetailView.as_view(), name="mainDatabase_Faculties_detail"),
    path("mainDatabase/Faculties/update/<int:id>/", views.FacultiesUpdateView.as_view(), name="mainDatabase_Faculties_update"),
    path("mainDatabase/Faculties/delete/<int:id>/", views.FacultiesDeleteView.as_view(), name="mainDatabase_Faculties_delete"),
    path("mainDatabase/Subject/", views.SubjectListView.as_view(), name="mainDatabase_Subject_list"),
    path("mainDatabase/Subject/create/", views.SubjectCreateView.as_view(), name="mainDatabase_Subject_create"),
    path("mainDatabase/Subject/detail/<int:pk>/", views.SubjectDetailView.as_view(), name="mainDatabase_Subject_detail"),
    path("mainDatabase/Subject/update/<int:pk>/", views.SubjectUpdateView.as_view(), name="mainDatabase_Subject_update"),
    path("mainDatabase/Subject/delete/<int:pk>/", views.SubjectDeleteView.as_view(), name="mainDatabase_Subject_delete"),
    path("mainDatabase/Group/", views.GroupListView.as_view(), name="mainDatabase_Group_list"),
    path("mainDatabase/Group/create/", views.GroupCreateView.as_view(), name="mainDatabase_Group_create"),
    path("mainDatabase/Group/detail/<int:id>/", views.GroupDetailView.as_view(), name="mainDatabase_Group_detail"),
    path("mainDatabase/Group/update/<int:id>/", views.GroupUpdateView.as_view(), name="mainDatabase_Group_update"),
    path("mainDatabase/Group/delete/<int:id>/", views.GroupDeleteView.as_view(), name="mainDatabase_Group_delete"),
    path("mainDatabase/markRange/", views.markRangeListView.as_view(), name="mainDatabase_markRange_list"),
    path("mainDatabase/markRange/create/", views.markRangeCreateView.as_view(), name="mainDatabase_markRange_create"),
    path("mainDatabase/markRange/detail/<int:id>/", views.markRangeDetailView.as_view(), name="mainDatabase_markRange_detail"),
    path("mainDatabase/markRange/update/<int:id>/", views.markRangeUpdateView.as_view(), name="mainDatabase_markRange_update"),
    path("mainDatabase/markRange/delete/<int:id>/", views.markRangeDeleteView.as_view(), name="mainDatabase_markRange_delete"),
    path("mainDatabase/Permission/", views.PermissionListView.as_view(), name="mainDatabase_Permission_list"),
    path("mainDatabase/Permission/create/", views.PermissionCreateView.as_view(), name="mainDatabase_Permission_create"),
    path("mainDatabase/Permission/detail/<int:pk>/", views.PermissionDetailView.as_view(), name="mainDatabase_Permission_detail"),
    path("mainDatabase/Permission/update/<int:pk>/", views.PermissionUpdateView.as_view(), name="mainDatabase_Permission_update"),
    path("mainDatabase/Permission/delete/<int:pk>/", views.PermissionDeleteView.as_view(), name="mainDatabase_Permission_delete"),
    path("mainDatabase/contentType/", views.contentTypeListView.as_view(), name="mainDatabase_contentType_list"),
    path("mainDatabase/contentType/create/", views.contentTypeCreateView.as_view(), name="mainDatabase_contentType_create"),
    path("mainDatabase/contentType/detail/<int:id>/", views.contentTypeDetailView.as_view(), name="mainDatabase_contentType_detail"),
    path("mainDatabase/contentType/update/<int:id>/", views.contentTypeUpdateView.as_view(), name="mainDatabase_contentType_update"),
    path("mainDatabase/contentType/delete/<int:id>/", views.contentTypeDeleteView.as_view(), name="mainDatabase_contentType_delete"),
    path("mainDatabase/logentry/", views.logentryListView.as_view(), name="mainDatabase_logentry_list"),
    path("mainDatabase/logentry/create/", views.logentryCreateView.as_view(), name="mainDatabase_logentry_create"),
    path("mainDatabase/logentry/detail/<int:id>/", views.logentryDetailView.as_view(), name="mainDatabase_logentry_detail"),
    path("mainDatabase/logentry/update/<int:id>/", views.logentryUpdateView.as_view(), name="mainDatabase_logentry_update"),
    path("mainDatabase/logentry/delete/<int:id>/", views.logentryDeleteView.as_view(), name="mainDatabase_logentry_delete"),
    path("mainDatabase/AbstractUser/", views.AbstractUserListView.as_view(), name="mainDatabase_AbstractUser_list"),
    path("mainDatabase/AbstractUser/create/", views.AbstractUserCreateView.as_view(), name="mainDatabase_AbstractUser_create"),
    path("mainDatabase/AbstractUser/detail/<int:pk>/", views.AbstractUserDetailView.as_view(), name="mainDatabase_AbstractUser_detail"),
    path("mainDatabase/AbstractUser/update/<int:pk>/", views.AbstractUserUpdateView.as_view(), name="mainDatabase_AbstractUser_update"),
    path("mainDatabase/AbstractUser/delete/<int:pk>/", views.AbstractUserDeleteView.as_view(), name="mainDatabase_AbstractUser_delete"),
    path("mainDatabase/prevYearsQp/", views.prevYearsQpListView.as_view(), name="mainDatabase_prevYearsQp_list"),
    path("mainDatabase/prevYearsQp/create/", views.prevYearsQpCreateView.as_view(), name="mainDatabase_prevYearsQp_create"),
    path("mainDatabase/prevYearsQp/detail/<int:pk>/", views.prevYearsQpDetailView.as_view(), name="mainDatabase_prevYearsQp_detail"),
    path("mainDatabase/prevYearsQp/update/<int:pk>/", views.prevYearsQpUpdateView.as_view(), name="mainDatabase_prevYearsQp_update"),
    path("mainDatabase/prevYearsQp/delete/<int:pk>/", views.prevYearsQpDeleteView.as_view(), name="mainDatabase_prevYearsQp_delete"),
)
