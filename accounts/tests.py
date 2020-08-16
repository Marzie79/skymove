from django.test import TestCase
from accounts.serializers import *
from accounts.models import User


class AuthorModelTest(TestCase):

    # def setUp(self):
    #     # Set up non-modified objects used by all test methods
    #     self.j_son = {
    #         "email": "farhad@gmil.com",
    #         "password": "1234567F",
    #         "nationality": "0037765786",
    #         "first_name": "Farhad",
    #         "last_name": "Zand",
    #         "phone_number": "09379870098",
    #         "company_name": "Asiya",
    #         "validation": "asikks"
    #     }
    #     self.user = User.objects.create(**self.j_son)
    #     self.serializer = User.objects.create(**self.j_son)
    @classmethod
    def setUp(self):
        self.j_son = {
            "email": "marzie.7900@gmail.com",
            "password": "1234567F",
            "nationality": "IR",
            "first_name": "Farhad",
            "last_name": "Zand",
            "phone_number": "09379870098",
            "company_name": "Asiya"
        }

        self.user = User.objects.create(email='mz00@gmail.com', password='12345678M', nationality='002301',
                                        first_name='مرضیه',
                                        last_name='معصوم زاده', phone_number='0937797', company_name='saran')

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
        response = self.client.post(path='/accounts/signup/', data=self.j_son)
        self.assertEquals(response.status_code, 201)

    def test_not_unique_email(self):
        repeat = {
            "email": "mz00@gmail.com",
            "password": "1234567M",
            "nationality": "IR",
            "first_name": "Farhad",
            "last_name": "Zand",
            "phone_number": "09379870098",
            "company_name": "Asiya"
        }
        response = self.client.post(path='/accounts/signup/', data=repeat)
        self.assertEquals(response.status_code, 400)


