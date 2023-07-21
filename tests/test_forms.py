from django.test import TestCase
from taxi.forms import DriverCreationForm


class FormsTests(TestCase):
    def test_driver_form_with_license_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "Test first",
            "last_name": "Test last",
            "license_number": "ABC12345"
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)