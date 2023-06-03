import unittest

from hired_score.models.contact_info import ContactInfo
from hired_score.utils.contact_info_utils import prepare_contact_info
from tests.fixtures import contact_info


class TestContactInfo(unittest.TestCase):
    def test_format_candidate_name(self):
        candidate_contact_info = ContactInfo(contact_info)
        formatted_candidate_name = candidate_contact_info.format_candidate_name()
        self.assertEqual(formatted_candidate_name, {'FirstName': 'Clark', 'LastName': 'Kent'})

    def test_format_candidate_name_name_is_missing(self):
        contact_info = {'location': {'latitude': 99.0124, 'longitude': -100.1471}, 'email': 'captainamerica@yahoo.com',
                        'phone': '123-456-7890',
                        'postal_address': {'address_line': '3', 'country_code': 'US', 'postal_code': '98765',
                                           'region': 'GM', 'municipality': 'Agrabah',
                                           'short_display_address': 'Agrabah, GM, US'},
                        'image_url': 'https://www.syfy.com/sites/syfy/files/styles/1200x680/public/2019/06/spider-man-original.jpg',
                        'name': None}
        candidate_contact_info = ContactInfo(contact_info)
        formatted_candidate_name = candidate_contact_info.format_candidate_name()
        self.assertEqual(formatted_candidate_name, None)

    def test_prepare_contact_info(self):
        contact_row = {
            'contact_info': {'location': {'latitude': 99.0124, 'longitude': -100.1471},
                             'email': 'captainamerica@yahoo.com',
                             'phone': '123-456-7890',
                             'postal_address': {'address_line': '3', 'country_code': 'US', 'postal_code': '98765',
                                                'region': 'GM', 'municipality': 'Agrabah',
                                                'short_display_address': 'Agrabah, GM, US'},
                             'image_url': 'https://www.syfy.com/sites/syfy/files/styles/1200x680/'
                                          'public/2019/06/spider-man-original.jpg',
                             'name': {'formatted_name': 'Clark L Kent', 'family_name': 'Kent', 'middle_name': 'L',
                                      'given_name': 'Clark'}}}
        candidate_contact_info, formatted_candidate_name = prepare_contact_info(contact_row)
        self.assertEqual(formatted_candidate_name, {'FirstName': 'Clark', 'LastName': 'Kent'})
