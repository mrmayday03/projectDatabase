import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Syllabus_list_view():
    instance1 = test_helpers.create_mainDatabase_Syllabus()
    instance2 = test_helpers.create_mainDatabase_Syllabus()
    client = Client()
    url = reverse("mainDatabase_Syllabus_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Syllabus_create_view():
    syllabus = test_helpers.create_mainDatabase_Course()
    client = Client()
    url = reverse("mainDatabase_Syllabus_create")
    data = {
        "syllabus": syllabus.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Syllabus_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Syllabus()
    url = reverse("mainDatabase_Syllabus_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Syllabus_update_view():
    syllabus = test_helpers.create_mainDatabase_Course()
    client = Client()
    instance = test_helpers.create_mainDatabase_Syllabus()
    url = reverse("mainDatabase_Syllabus_update", args=[instance.id, ])
    data = {
        "syllabus": syllabus.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Question_list_view():
    instance1 = test_helpers.create_mainDatabase_Question()
    instance2 = test_helpers.create_mainDatabase_Question()
    client = Client()
    url = reverse("mainDatabase_Question_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Question_create_view():
    client = Client()
    url = reverse("mainDatabase_Question_create")
    data = {
        "difficulty": "text",
        "title": "text",
        "difficulty": "text",
        "question": "text",
        "question": "text",
        "slug": "slug",
        "answer": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Question_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Question()
    url = reverse("mainDatabase_Question_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Question_update_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Question()
    url = reverse("mainDatabase_Question_update", args=[instance.slug, ])
    data = {
        "difficulty": "text",
        "title": "text",
        "difficulty": "text",
        "question": "text",
        "question": "text",
        "slug": "slug",
        "answer": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_list_view():
    instance1 = test_helpers.create_mainDatabase_User()
    instance2 = test_helpers.create_mainDatabase_User()
    client = Client()
    url = reverse("mainDatabase_User_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_User_create_view():
    users = test_helpers.create_mainDatabase_logentry()
    client = Client()
    url = reverse("mainDatabase_User_create")
    data = {
        "date_joined": datetime.now(),
        "email": "user@tempurl.com",
        "name": "text",
        "password": "text",
        "username": "text",
        "users": users.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_User()
    url = reverse("mainDatabase_User_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_User_update_view():
    users = test_helpers.create_mainDatabase_logentry()
    client = Client()
    instance = test_helpers.create_mainDatabase_User()
    url = reverse("mainDatabase_User_update", args=[instance.id, ])
    data = {
        "date_joined": datetime.now(),
        "email": "user@tempurl.com",
        "name": "text",
        "password": "text",
        "username": "text",
        "users": users.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Course_list_view():
    instance1 = test_helpers.create_mainDatabase_Course()
    instance2 = test_helpers.create_mainDatabase_Course()
    client = Client()
    url = reverse("mainDatabase_Course_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Course_create_view():
    client = Client()
    url = reverse("mainDatabase_Course_create")
    data = {
        "course": "text",
        "active": true,
        "semester": 1,
        "regulation": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Course_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Course()
    url = reverse("mainDatabase_Course_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Course_update_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Course()
    url = reverse("mainDatabase_Course_update", args=[instance.id, ])
    data = {
        "course": "text",
        "active": true,
        "semester": 1,
        "regulation": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Department_list_view():
    instance1 = test_helpers.create_mainDatabase_Department()
    instance2 = test_helpers.create_mainDatabase_Department()
    client = Client()
    url = reverse("mainDatabase_Department_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Department_create_view():
    dept = test_helpers.create_mainDatabase_Course()
    client = Client()
    url = reverse("mainDatabase_Department_create")
    data = {
        "branch_code": "text",
        "degree": "text",
        "branch": "text",
        "dept": dept.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Department_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Department()
    url = reverse("mainDatabase_Department_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Department_update_view():
    dept = test_helpers.create_mainDatabase_Course()
    client = Client()
    instance = test_helpers.create_mainDatabase_Department()
    url = reverse("mainDatabase_Department_update", args=[instance.id, ])
    data = {
        "branch_code": "text",
        "degree": "text",
        "branch": "text",
        "dept": dept.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Faculties_list_view():
    instance1 = test_helpers.create_mainDatabase_Faculties()
    instance2 = test_helpers.create_mainDatabase_Faculties()
    client = Client()
    url = reverse("mainDatabase_Faculties_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Faculties_create_view():
    faculties = test_helpers.create_User()
    client = Client()
    url = reverse("mainDatabase_Faculties_create")
    data = {
        "faculties": faculties.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Faculties_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Faculties()
    url = reverse("mainDatabase_Faculties_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Faculties_update_view():
    faculties = test_helpers.create_User()
    client = Client()
    instance = test_helpers.create_mainDatabase_Faculties()
    url = reverse("mainDatabase_Faculties_update", args=[instance.id, ])
    data = {
        "faculties": faculties.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Subject_list_view():
    instance1 = test_helpers.create_mainDatabase_Subject()
    instance2 = test_helpers.create_mainDatabase_Subject()
    client = Client()
    url = reverse("mainDatabase_Subject_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Subject_create_view():
    questions = test_helpers.create_mainDatabase_Question()
    subjects = test_helpers.create_mainDatabase_Syllabus()
    client = Client()
    url = reverse("mainDatabase_Subject_create")
    data = {
        "subjectName": "text",
        "co": "text",
        "code": "text",
        "questions": questions.pk,
        "subjects": subjects.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Subject_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Subject()
    url = reverse("mainDatabase_Subject_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Subject_update_view():
    questions = test_helpers.create_mainDatabase_Question()
    subjects = test_helpers.create_mainDatabase_Syllabus()
    client = Client()
    instance = test_helpers.create_mainDatabase_Subject()
    url = reverse("mainDatabase_Subject_update", args=[instance.pk, ])
    data = {
        "subjectName": "text",
        "co": "text",
        "code": "text",
        "questions": questions.pk,
        "subjects": subjects.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Group_list_view():
    instance1 = test_helpers.create_mainDatabase_Group()
    instance2 = test_helpers.create_mainDatabase_Group()
    client = Client()
    url = reverse("mainDatabase_Group_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Group_create_view():
    groups = test_helpers.create_User()
    client = Client()
    url = reverse("mainDatabase_Group_create")
    data = {
        "name": "text",
        "groups": groups.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Group_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Group()
    url = reverse("mainDatabase_Group_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Group_update_view():
    groups = test_helpers.create_User()
    client = Client()
    instance = test_helpers.create_mainDatabase_Group()
    url = reverse("mainDatabase_Group_update", args=[instance.id, ])
    data = {
        "name": "text",
        "groups": groups.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_markRange_list_view():
    instance1 = test_helpers.create_mainDatabase_markRange()
    instance2 = test_helpers.create_mainDatabase_markRange()
    client = Client()
    url = reverse("mainDatabase_markRange_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_markRange_create_view():
    client = Client()
    url = reverse("mainDatabase_markRange_create")
    data = {
        "endField": 1,
        "startRange": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_markRange_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_markRange()
    url = reverse("mainDatabase_markRange_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_markRange_update_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_markRange()
    url = reverse("mainDatabase_markRange_update", args=[instance.id, ])
    data = {
        "endField": 1,
        "startRange": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Permission_list_view():
    instance1 = test_helpers.create_mainDatabase_Permission()
    instance2 = test_helpers.create_mainDatabase_Permission()
    client = Client()
    url = reverse("mainDatabase_Permission_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Permission_create_view():
    permissions(group) = test_helpers.create_Group()
    client = Client()
    url = reverse("mainDatabase_Permission_create")
    data = {
        "name": "text",
        "codename": "text",
        "permissions(group)": permissions(group).pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Permission_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_Permission()
    url = reverse("mainDatabase_Permission_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Permission_update_view():
    permissions(group) = test_helpers.create_Group()
    client = Client()
    instance = test_helpers.create_mainDatabase_Permission()
    url = reverse("mainDatabase_Permission_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "codename": "text",
        "permissions(group)": permissions(group).pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_contentType_list_view():
    instance1 = test_helpers.create_mainDatabase_contentType()
    instance2 = test_helpers.create_mainDatabase_contentType()
    client = Client()
    url = reverse("mainDatabase_contentType_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_contentType_create_view():
    contentType = test_helpers.create_mainDatabase_Permission()
    client = Client()
    url = reverse("mainDatabase_contentType_create")
    data = {
        "model": "text",
        "app_label": "text",
        "contentType": contentType.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_contentType_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_contentType()
    url = reverse("mainDatabase_contentType_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_contentType_update_view():
    contentType = test_helpers.create_mainDatabase_Permission()
    client = Client()
    instance = test_helpers.create_mainDatabase_contentType()
    url = reverse("mainDatabase_contentType_update", args=[instance.id, ])
    data = {
        "model": "text",
        "app_label": "text",
        "contentType": contentType.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_logentry_list_view():
    instance1 = test_helpers.create_mainDatabase_logentry()
    instance2 = test_helpers.create_mainDatabase_logentry()
    client = Client()
    url = reverse("mainDatabase_logentry_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_logentry_create_view():
    client = Client()
    url = reverse("mainDatabase_logentry_create")
    data = {
        "objectId": "text",
        "objectRepr": "text",
        "change_message": "text",
        "actionFlag": 1,
        "actionTime": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_logentry_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_logentry()
    url = reverse("mainDatabase_logentry_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_logentry_update_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_logentry()
    url = reverse("mainDatabase_logentry_update", args=[instance.id, ])
    data = {
        "objectId": "text",
        "objectRepr": "text",
        "change_message": "text",
        "actionFlag": 1,
        "actionTime": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_prevYearsQp_list_view():
    instance1 = test_helpers.create_mainDatabase_prevYearsQp()
    instance2 = test_helpers.create_mainDatabase_prevYearsQp()
    client = Client()
    url = reverse("mainDatabase_prevYearsQp_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_prevYearsQp_create_view():
    prevYrQp = test_helpers.create_mainDatabase_Question()
    client = Client()
    url = reverse("mainDatabase_prevYearsQp_create")
    data = {
        "year": "text",
        "month": 1,
        "prevYrQp": prevYrQp.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_prevYearsQp_detail_view():
    client = Client()
    instance = test_helpers.create_mainDatabase_prevYearsQp()
    url = reverse("mainDatabase_prevYearsQp_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_prevYearsQp_update_view():
    prevYrQp = test_helpers.create_mainDatabase_Question()
    client = Client()
    instance = test_helpers.create_mainDatabase_prevYearsQp()
    url = reverse("mainDatabase_prevYearsQp_update", args=[instance.pk, ])
    data = {
        "year": "text",
        "month": 1,
        "prevYrQp": prevYrQp.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
