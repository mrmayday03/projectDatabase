from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class SyllabusListView(generic.ListView):
    model = models.Syllabus
    form_class = forms.SyllabusForm


class SyllabusCreateView(generic.CreateView):
    model = models.Syllabus
    form_class = forms.SyllabusForm


class SyllabusDetailView(generic.DetailView):
    model = models.Syllabus
    form_class = forms.SyllabusForm
    pk_url_kwarg = "id"


class SyllabusUpdateView(generic.UpdateView):
    model = models.Syllabus
    form_class = forms.SyllabusForm
    pk_url_kwarg = "id"


class SyllabusDeleteView(generic.DeleteView):
    model = models.Syllabus
    success_url = reverse_lazy("mainDatabase_Syllabus_list")


class QuestionListView(generic.ListView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionCreateView(generic.CreateView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionDetailView(generic.DetailView):
    model = models.Question
    form_class = forms.QuestionForm
    slug_url_kwarg = "slug"


class QuestionUpdateView(generic.UpdateView):
    model = models.Question
    form_class = forms.QuestionForm
    slug_url_kwarg = "slug"


class QuestionDeleteView(generic.DeleteView):
    model = models.Question
    success_url = reverse_lazy("mainDatabase_Question_list")


class UserListView(generic.ListView):
    model = models.User
    form_class = forms.UserForm


class UserCreateView(generic.CreateView):
    model = models.User
    form_class = forms.UserForm


class UserDetailView(generic.DetailView):
    model = models.User
    form_class = forms.UserForm
    pk_url_kwarg = "id"


class UserUpdateView(generic.UpdateView):
    model = models.User
    form_class = forms.UserForm
    pk_url_kwarg = "id"


class UserDeleteView(generic.DeleteView):
    model = models.User
    success_url = reverse_lazy("mainDatabase_User_list")


class CourseListView(generic.ListView):
    model = models.Course
    form_class = forms.CourseForm


class CourseCreateView(generic.CreateView):
    model = models.Course
    form_class = forms.CourseForm


class CourseDetailView(generic.DetailView):
    model = models.Course
    form_class = forms.CourseForm
    pk_url_kwarg = "id"


class CourseUpdateView(generic.UpdateView):
    model = models.Course
    form_class = forms.CourseForm
    pk_url_kwarg = "id"


class CourseDeleteView(generic.DeleteView):
    model = models.Course
    success_url = reverse_lazy("mainDatabase_Course_list")


class DepartmentListView(generic.ListView):
    model = models.Department
    form_class = forms.DepartmentForm


class DepartmentCreateView(generic.CreateView):
    model = models.Department
    form_class = forms.DepartmentForm


class DepartmentDetailView(generic.DetailView):
    model = models.Department
    form_class = forms.DepartmentForm
    pk_url_kwarg = "id"


class DepartmentUpdateView(generic.UpdateView):
    model = models.Department
    form_class = forms.DepartmentForm
    pk_url_kwarg = "id"


class DepartmentDeleteView(generic.DeleteView):
    model = models.Department
    success_url = reverse_lazy("mainDatabase_Department_list")


class FacultiesListView(generic.ListView):
    model = models.Faculties
    form_class = forms.FacultiesForm


class FacultiesCreateView(generic.CreateView):
    model = models.Faculties
    form_class = forms.FacultiesForm


class FacultiesDetailView(generic.DetailView):
    model = models.Faculties
    form_class = forms.FacultiesForm
    pk_url_kwarg = "id"


class FacultiesUpdateView(generic.UpdateView):
    model = models.Faculties
    form_class = forms.FacultiesForm
    pk_url_kwarg = "id"


class FacultiesDeleteView(generic.DeleteView):
    model = models.Faculties
    success_url = reverse_lazy("mainDatabase_Faculties_list")


class SubjectListView(generic.ListView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectCreateView(generic.CreateView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectDetailView(generic.DetailView):
    model = models.Subject
    form_class = forms.SubjectForm


class SubjectUpdateView(generic.UpdateView):
    model = models.Subject
    form_class = forms.SubjectForm
    pk_url_kwarg = "pk"


class SubjectDeleteView(generic.DeleteView):
    model = models.Subject
    success_url = reverse_lazy("mainDatabase_Subject_list")


class GroupListView(generic.ListView):
    model = models.Group
    form_class = forms.GroupForm


class GroupCreateView(generic.CreateView):
    model = models.Group
    form_class = forms.GroupForm


class GroupDetailView(generic.DetailView):
    model = models.Group
    form_class = forms.GroupForm
    pk_url_kwarg = "id"


class GroupUpdateView(generic.UpdateView):
    model = models.Group
    form_class = forms.GroupForm
    pk_url_kwarg = "id"


class GroupDeleteView(generic.DeleteView):
    model = models.Group
    success_url = reverse_lazy("mainDatabase_Group_list")


class markRangeListView(generic.ListView):
    model = models.markRange
    form_class = forms.markRangeForm


class markRangeCreateView(generic.CreateView):
    model = models.markRange
    form_class = forms.markRangeForm


class markRangeDetailView(generic.DetailView):
    model = models.markRange
    form_class = forms.markRangeForm
    pk_url_kwarg = "id"


class markRangeUpdateView(generic.UpdateView):
    model = models.markRange
    form_class = forms.markRangeForm
    pk_url_kwarg = "id"


class markRangeDeleteView(generic.DeleteView):
    model = models.markRange
    success_url = reverse_lazy("mainDatabase_markRange_list")


class PermissionListView(generic.ListView):
    model = models.Permission
    form_class = forms.PermissionForm


class PermissionCreateView(generic.CreateView):
    model = models.Permission
    form_class = forms.PermissionForm


class PermissionDetailView(generic.DetailView):
    model = models.Permission
    form_class = forms.PermissionForm


class PermissionUpdateView(generic.UpdateView):
    model = models.Permission
    form_class = forms.PermissionForm
    pk_url_kwarg = "pk"


class PermissionDeleteView(generic.DeleteView):
    model = models.Permission
    success_url = reverse_lazy("mainDatabase_Permission_list")


class contentTypeListView(generic.ListView):
    model = models.contentType
    form_class = forms.contentTypeForm


class contentTypeCreateView(generic.CreateView):
    model = models.contentType
    form_class = forms.contentTypeForm


class contentTypeDetailView(generic.DetailView):
    model = models.contentType
    form_class = forms.contentTypeForm
    pk_url_kwarg = "id"


class contentTypeUpdateView(generic.UpdateView):
    model = models.contentType
    form_class = forms.contentTypeForm
    pk_url_kwarg = "id"


class contentTypeDeleteView(generic.DeleteView):
    model = models.contentType
    success_url = reverse_lazy("mainDatabase_contentType_list")


class logentryListView(generic.ListView):
    model = models.logentry
    form_class = forms.logentryForm


class logentryCreateView(generic.CreateView):
    model = models.logentry
    form_class = forms.logentryForm


class logentryDetailView(generic.DetailView):
    model = models.logentry
    form_class = forms.logentryForm
    pk_url_kwarg = "id"


class logentryUpdateView(generic.UpdateView):
    model = models.logentry
    form_class = forms.logentryForm
    pk_url_kwarg = "id"


class logentryDeleteView(generic.DeleteView):
    model = models.logentry
    success_url = reverse_lazy("mainDatabase_logentry_list")


class prevYearsQpListView(generic.ListView):
    model = models.prevYearsQp
    form_class = forms.prevYearsQpForm


class prevYearsQpCreateView(generic.CreateView):
    model = models.prevYearsQp
    form_class = forms.prevYearsQpForm


class prevYearsQpDetailView(generic.DetailView):
    model = models.prevYearsQp
    form_class = forms.prevYearsQpForm


class prevYearsQpUpdateView(generic.UpdateView):
    model = models.prevYearsQp
    form_class = forms.prevYearsQpForm
    pk_url_kwarg = "pk"


class prevYearsQpDeleteView(generic.DeleteView):
    model = models.prevYearsQp
    success_url = reverse_lazy("mainDatabase_prevYearsQp_list")
