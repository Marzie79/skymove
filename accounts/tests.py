from django.test import TestCase
from rest_framework.reverse import reverse
from .views import *


class UserModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.j_son = {
            "email": "marzie.7900@gmail.com",
            "password": "1234567F",
            "nationality": "IR",
            "first_name": "Farhad",
            "last_name": "Zand",
            "phone_number": "+989369447797",
            "company_name": "Asiya"
        }

        self.user = User.objects.create(email='mz00@gmail.com', password='12345678M', nationality='IR',
                                        first_name='مرضیه', last_name='معصوم زاده', phone_number='+989369447797',
                                        company_name='saran', is_validate=True, validation='abcdef')
        self.user.set_password(self.user.password)
        self.user.save()

        self.user1 = User.objects.create(email='maz00@gmail.com', password='12345678M', nationality='IR',
                                         first_name='سایه', last_name='نصیری', phone_number='+989369447797',
                                         company_name='saran', is_validate=False)
        self.user1.set_password(self.user.password)
        self.user1.save()

    def test_serializer_not_send_password(self):
        user = User.objects.get(pk=1)
        data = ProfileSerializer(user)
        field_label = ''
        if 'password' in data.data:
            field_label = data.data['password']
        self.assertEquals(field_label, '')

    # def test_for_sending_a_random_validation_code(self):
    #     j_son = {
    #         "email": "farhad@gmil.com",
    #         "password": "1234567F",
    #         "nationality": "0037765786",
    #         "first_name": "Farhad",
    #         "last_name": "Zand",
    #         "phone_number": "09379870098",
    #         "company_name": "Asiya",
    #     }
    #     code = j_son.get('validation')
    #     data = ProfileSerializer(data=j_son)
    #     field_label = ''
    #     if data.is_valid():
    #         if 'validation' in data.data:
    #             field_label = data.data['validation']
    #
    #     self.assertNotEqual(field_label, code)

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length_last_name = user._meta.get_field('last_name').max_length
        max_length_first_name = user._meta.get_field('first_name').max_length
        max_length_nationality = user._meta.get_field('nationality').max_length
        self.assertEquals(max_length_first_name, 30)
        self.assertEquals(max_length_last_name, 30)
        self.assertEquals(max_length_nationality, 2)

    def test_object_name_is_last_name_comma_first_name(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.first_name} {user.last_name}'
        self.assertEquals(expected_object_name, str(user))

    def test_object_sending_data_correct(self):
        user = User.objects.get(id=1)
        data = ProfileSerializer(user)
        email = data.data['email']
        first_name = data.data['first_name']
        last_name = data.data['last_name']
        nationality = data.data['nationality']
        phone_number = data.data['phone_number']
        self.assertEquals(email, user.email)
        self.assertEquals(first_name, user.first_name)
        self.assertEquals(last_name, user.last_name)
        self.assertEquals(nationality, user.nationality)
        self.assertEquals(phone_number, user.phone_number)

    def test_sign_up_correct_data(self):
        response = self.client.post(reverse('v1:sign_up'), data=self.j_son)
        self.assertEquals(response.status_code, 201)

    def test_not_unique_email_for_sign_up(self):
        repeat = {
            "email": "mz00@gmail.com",
            "password": "1234567M",
            "nationality": "IR",
            "first_name": "Farhad",
            "last_name": "Zand",
            "phone_number": "+9809369447797",
            "company_name": "Asiya"
        }
        response = self.client.post(reverse('v1:sign_up'), data=repeat)
        self.assertEquals(response.status_code, 400)

    def test_sign_in_correct_data(self):
        person = {
            "email": "mz00@gmail.com",
            "password": "12345678M"
        }
        response = self.client.post(reverse('v1:log_in'), data=person)
        self.assertEquals(response.status_code, 200)

    def test_sign_in_wrong_password(self):
        person = {
            "email": "mz00@gmail.com",
            "password": "12345678"
        }
        response = self.client.post(reverse('v1:log_in'), data=person)
        self.assertEquals(response.status_code, 406)

    def test_sign_in_bad_request(self):
        person = {
            "password": "12345678M"
        }
        response = self.client.post(reverse('v1:log_in'), data=person)
        self.assertEquals(response.status_code, 400)

    def test_sign_in_email_is_not_exist(self):
        person = {
            "email": "alireza7900@gmail.com",
            "password": "12345678M"
        }
        response = self.client.post(reverse('v1:log_in'), data=person)
        self.assertEquals(response.status_code, 404)

    def test_sign_in_user_is_not_validate(self):
        person = {
            "email": "maz00@gmail.com",
            "password": "12345678M"
        }
        response = self.client.post(reverse('v1:log_in'), data=person)
        self.assertEquals(response.status_code, 401)

    def test_validate_email_for_first_time(self):
        person = {
            "email": "maz00@gmail.com"
        }
        response = self.client.post(reverse('v1:validate_email'), data=person)
        self.assertEquals(response.status_code, 200)

    def test_validate_email_when_user_is_valid(self):
        person = {
            "email": "mz00@gmail.com"
        }
        response = self.client.post(reverse('v1:validate_email'), data=person)
        self.assertEquals(response.status_code, 409)

    def test_validate_email_with_none_exist_email(self):
        person = {
            "email": "m00@gmail.com"
        }
        response = self.client.post(reverse('v1:validate_email'), data=person)
        self.assertEquals(response.status_code, 404)

    def test_validate_email_when_it_is_valid(self):
        person = {
            "email": "mz00@gmail.com",
            "validation": "abcdef"
        }
        response = self.client.post(path=reverse('v1:validate_email_code'), data=person)
        self.assertEquals(response.status_code, 409)

    def test_validate_email_when_email_does_not_exist(self):
        person = {
            "email": "m00@gmail.com",
            "validation": "abcdef"
        }
        response = self.client.post(path=reverse('v1:validate_email_code'), data=person)
        self.assertEquals(response.status_code, 404)

    def test_validate_email_set_correct_validate_code(self):
        self.user1.validation = 'abcdef'
        self.user1.save()
        person = {
            "email": "maz00@gmail.com",
            "validation": self.user1.validation
        }
        response = self.client.post(path=reverse('v1:validate_email_code'), data=person)
        self.assertEquals(response.status_code, 200)

    def test_validate_email_set_wrong_validate_code(self):
        self.user1.validation = 'abcdef'
        self.user1.save()
        person = {
            "email": "maz00@gmail.com",
            "validation": "dfm.e"
        }
        response = self.client.post(path=reverse('v1:validate_email_code'), data=person)
        self.assertEquals(response.status_code, 406)

    def test_custom_validation_error_empty_field(self):
        response = CustomValidation(detail=None, field='email', status_code=status.HTTP_200_OK)
        self.assertEquals(response.status_code, 200)

    # def test_password_reset(self):
