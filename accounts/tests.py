from django.test import TestCase
from accounts.models import User
from accounts.serializers import ProfileSerializer


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(email='mz00@gmail.com', password='12345678M', nationality='002301', first_name='مرضیه',
                            last_name='معصوم زاده', phone_number='0937797', company_name='saran', validation='')

    def test_serializer_not_send_password(self):
        user = User.objects.get(pk=1)
        data = ProfileSerializer(user)
        field_label = ''
        if 'password' in data.data:
            field_label = data.data['password']
        self.assertEquals(field_label, '')

    def test_for_sending_a_random_validation_code(self):
        j_son = {
            "email": "farhad@gmil.com",
            "password": "1234567F",
            "nationality": "0037765786",
            "first_name": "Farhad",
            "last_name": "Zand",
            "phone_number": "09379870098",
            "company_name": "Asiya",
            "validation": "asikks"
        }
        code = j_son.get('validation')
        data = ProfileSerializer(data=j_son)
        field_label = ''
        if data.is_valid():
            if 'validation' in data.data:
                field_label = data.data['validation']

        self.assertNotEqual(field_label, code)

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_object_name_is_last_name_comma_first_name(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.first_name} {user.last_name}'
        self.assertEquals(expected_object_name, str(user))
