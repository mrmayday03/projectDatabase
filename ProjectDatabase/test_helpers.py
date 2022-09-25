import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from mainDatabase import models as mainDatabase_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_mainDatabase_Syllabus(**kwargs):
    defaults = {}
    if "syllabus" not in kwargs:
        defaults["syllabus"] = create_mainDatabase_Course()
    defaults.update(**kwargs)
    return mainDatabase_models.Syllabus.objects.create(**defaults)
def create_mainDatabase_Question(**kwargs):
    defaults = {}
    defaults["difficulty"] = ""
    defaults["title"] = ""
    defaults["difficulty"] = ""
    defaults["question"] = ""
    defaults["question"] = ""
    defaults["slug"] = ""
    defaults["answer"] = ""
    defaults.update(**kwargs)
    return mainDatabase_models.Question.objects.create(**defaults)
def create_mainDatabase_User(**kwargs):
    defaults = {}
    defaults["date_joined"] = datetime.now()
    defaults["email"] = ""
    defaults["name"] = ""
    defaults["password"] = ""
    defaults["username"] = ""
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    if "users" not in kwargs:
        defaults["users"] = create_mainDatabase_logentry()
    defaults.update(**kwargs)
    return mainDatabase_models.User.objects.create(**defaults)
def create_mainDatabase_Course(**kwargs):
    defaults = {}
    defaults["course"] = ""
    defaults["active"] = ""
    defaults["semester"] = ""
    defaults["regulation"] = ""
    defaults["id"] = "sometext"
    defaults["course"] = 
    defaults["last_updated"] = datetime.now()
    defaults["subject"] = 
    defaults["created"] = datetime.now()
    defaults.update(**kwargs)
    return mainDatabase_models.Course.objects.create(**defaults)
def create_mainDatabase_Department(**kwargs):
    defaults = {}
    defaults["branch_code"] = ""
    defaults["degree"] = ""
    defaults["branch"] = ""
    defaults["course"] = "text"
    defaults["active"] = true
    defaults["created"] = datetime.now()
    defaults["semester"] = 1
    defaults["department"] = 
    defaults["regulation"] = "text"
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "auto"
    if "dept" not in kwargs:
        defaults["dept"] = create_mainDatabase_Course()
    defaults.update(**kwargs)
    return mainDatabase_models.Department.objects.create(**defaults)
def create_mainDatabase_Faculties(**kwargs):
    defaults = {}
    defaults["date_joined"] = datetime.now()
    defaults["last_updated"] = datetime.now()
    defaults["email"] = "user@tempurl.com"
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults["id"] = "sometext"
    defaults["password"] = "text"
    defaults["username"] = "text"
    if "faculties" not in kwargs:
        defaults["faculties"] = create_User()
    defaults.update(**kwargs)
    return mainDatabase_models.Faculties.objects.create(**defaults)
def create_mainDatabase_Subject(**kwargs):
    defaults = {}
    defaults["subjectName"] = ""
    defaults["co"] = ""
    defaults["code"] = ""
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "sometext"
    defaults["course"] = 
    defaults["created"] = datetime.now()
    defaults["subject"] = 
    if "questions" not in kwargs:
        defaults["questions"] = create_mainDatabase_Question()
    if "subjects" not in kwargs:
        defaults["subjects"] = create_mainDatabase_Syllabus()
    defaults.update(**kwargs)
    return mainDatabase_models.Subject.objects.create(**defaults)
def create_mainDatabase_Group(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["date_joined"] = datetime.now()
    defaults["last_updated"] = datetime.now()
    defaults["email"] = "user@tempurl.com"
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults["id"] = "sometext"
    defaults["password"] = "text"
    defaults["username"] = "text"
    if "groups" not in kwargs:
        defaults["groups"] = create_User()
    defaults.update(**kwargs)
    return mainDatabase_models.Group.objects.create(**defaults)
def create_mainDatabase_markRange(**kwargs):
    defaults = {}
    defaults["endField"] = ""
    defaults["startRange"] = ""
    defaults["mark"] = 
    defaults["difficulty"] = "text"
    defaults["title"] = "text"
    defaults["difficulty"] = "text"
    defaults["id"] = "sometext"
    defaults["question"] = "text"
    defaults["subject"] = 
    defaults["question"] = "text"
    defaults["created"] = datetime.now()
    defaults["slug"] = "slug"
    defaults["answer"] = "text"
    defaults["last_updated"] = datetime.now()
    defaults.update(**kwargs)
    return mainDatabase_models.markRange.objects.create(**defaults)
def create_mainDatabase_Permission(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["codename"] = ""
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults["id"] = "auto"
    defaults["last_updated"] = datetime.now()
    if "permissions(group)" not in kwargs:
        defaults["permissions(group)"] = create_Group()
    defaults.update(**kwargs)
    return mainDatabase_models.Permission.objects.create(**defaults)
def create_mainDatabase_contentType(**kwargs):
    defaults = {}
    defaults["model"] = ""
    defaults["app_label"] = ""
    defaults["created"] = datetime.now()
    defaults["name"] = "text"
    defaults["contentType"] = 
    defaults["codename"] = "text"
    defaults["last_updated"] = datetime.now()
    if "contentType" not in kwargs:
        defaults["contentType"] = create_mainDatabase_Permission()
    defaults.update(**kwargs)
    return mainDatabase_models.contentType.objects.create(**defaults)
def create_mainDatabase_logentry(**kwargs):
    defaults = {}
    defaults["objectId"] = ""
    defaults["objectRepr"] = ""
    defaults["change_message"] = ""
    defaults["actionFlag"] = ""
    defaults["actionTime"] = datetime.now()
    defaults["objectId"] = "text"
    defaults["objectRepr"] = "text"
    defaults["change_message"] = "text"
    defaults["actionFlag"] = 1
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "auto"
    defaults["actionTime"] = datetime.now()
    defaults["user"] = 
    defaults["contentType"] = 
    defaults["created"] = datetime.now()
    defaults.update(**kwargs)
    return mainDatabase_models.logentry.objects.create(**defaults)
def create_mainDatabase_prevYearsQp(**kwargs):
    defaults = {}
    defaults["year"] = ""
    defaults["month"] = ""
    defaults["mark"] = 
    defaults["difficulty"] = "text"
    defaults["title"] = "text"
    defaults["difficulty"] = "text"
    defaults["id"] = "sometext"
    defaults["question"] = "text"
    defaults["subject"] = 
    defaults["question"] = "text"
    defaults["created"] = datetime.now()
    defaults["slug"] = "slug"
    defaults["answer"] = "text"
    defaults["last_updated"] = datetime.now()
    if "prevYrQp" not in kwargs:
        defaults["prevYrQp"] = create_mainDatabase_Question()
    defaults.update(**kwargs)
    return mainDatabase_models.prevYearsQp.objects.create(**defaults)
