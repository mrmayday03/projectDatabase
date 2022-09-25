from django.db import models
from django.urls import reverse


class Syllabus(models.Model):

    # Relationships
    syllabus = models.ForeignKey("mainDatabase.Course", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.BigAutoField(primary_key=True)
    course = models.GenericForeignKey("content_type", "id")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    subject = models.GenericForeignKey("content_type", "id")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_Syllabus_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_Syllabus_update", args=(self.id,))


class Question(models.Model):

    # Fields
    mark = models.GenericForeignKey("content_type", "object_id")
    difficulty = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    difficulty = models.CharField(max_length=30)
    id = models.BigAutoField(primary_key=True)
    question = models.TextField(max_length=100)
    subject = models.GenericForeignKey("content_type", "object_id")
    question = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()
    answer = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_Question_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("mainDatabase_Question_update", args=(self.slug,))


class User(AbstractUser):

    # Relationships
    users = models.ForeignKey("mainDatabase.logentry", on_delete=models.CASCADE)

    # Fields
    date_joined = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainDatabase_User_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_User_update", args=(self.id,))


class Course(Faculties):

    # Fields
    course = models.CharField(max_length=30)
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    semester = models.IntegerField()
    department = models.GenericForeignKey("content_type", "id")
    regulation = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_Course_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_Course_update", args=(self.id,))


class Department(Course):

    # Relationships
    dept = models.ForeignKey("mainDatabase.Course", on_delete=models.CASCADE)

    # Fields
    branch_code = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    degree = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.BigAutoField(primary_key=True)
    branch = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_Department_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_Department_update", args=(self.id,))


class Faculties(User):

    # Relationships
    faculties = models.OneToOneField("auth.User")

    # Fields
    id = models.BigAutoField(primary_key=True)
    course = models.GenericForeignKey("content_type", "id")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    subject = models.GenericForeignKey("content_type", "id")
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_Faculties_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_Faculties_update", args=(self.id,))


class Subject(Syllabus):

    # Relationships
    questions = models.OneToOneField("mainDatabase.Question")
    subjects = models.OneToOneField("mainDatabase.Syllabus")

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    subjectName = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    co = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_Subject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainDatabase_Subject_update", args=(self.pk,))


class Group(User):

    # Relationships
    groups = models.OneToOneField("auth.User")

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.AutoField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainDatabase_Group_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_Group_update", args=(self.id,))


class markRange(Question):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    endField = models.IntegerField()
    startRange = models.IntegerField()
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_markRange_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_markRange_update", args=(self.id,))


class Permission(Group):

    # Relationships
    permissions(group) = models.OneToOneField("auth.Group")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    contentType = models.GenericForeignKey("content_type", "id")
    codename = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("mainDatabase_Permission_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainDatabase_Permission_update", args=(self.pk,))


class contentType(Permission):

    # Relationships
    contentType = models.OneToOneField("mainDatabase.Permission")

    # Fields
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30)
    app_label = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_contentType_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_contentType_update", args=(self.id,))


class logentry(logentry):

    # Fields
    objectId = models.TextField(max_length=100)
    objectRepr = models.CharField(max_length=30)
    change_message = models.TextField(max_length=100)
    actionFlag = models.PositiveSmallIntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.AutoField(primary_key=True)
    actionTime = models.DateTimeField()
    user = models.GenericForeignKey("content_type", "id")
    contentType = models.GenericForeignKey("content_type", "id")
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_logentry_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("mainDatabase_logentry_update", args=(self.id,))


class AbstractUser(AbstractBaseUser):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    password = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_AbstractUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainDatabase_AbstractUser_update", args=(self.pk,))


class prevYearsQp(Question):

    # Relationships
    prevYrQp = models.OneToOneField("mainDatabase.Question")

    # Fields
    year = models.CharField(max_length=10)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    month = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("mainDatabase_prevYearsQp_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("mainDatabase_prevYearsQp_update", args=(self.pk,))
