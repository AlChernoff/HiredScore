import unittest

from hired_score.models.contact_info import ContactInfo
from tests.fixtures import contact_info, contact_info_no_phone, contact_info_no_contact_info, linkedin_info, \
    candidates_info, expected_candidates
from hired_score.utils.candidate_info_utils import prepare_linkedin_info, prepare_candidates_info


class TestCandidateInfo(unittest.TestCase):
    def test_prepare_linkedin_info_phone(self):
        candidate_contact_info = ContactInfo(contact_info)
        candidates_linkedin = prepare_linkedin_info(candidate_contact_info, linkedin_info)
        assert candidates_linkedin == 'https://linkedin.com/in/captainamerica'

    def test_prepare_linkedin_info_email(self):
        candidate_contact_info = ContactInfo(contact_info_no_phone)
        candidates_linkedin = prepare_linkedin_info(candidate_contact_info, linkedin_info)
        self.assertEqual(candidates_linkedin, 'https://linkedin.com/in/captainamerica')

    def test_prepare_linkedin_info_no_contact_info(self):
        candidate_contact_info = ContactInfo(contact_info_no_contact_info)
        candidates_linkedin = prepare_linkedin_info(candidate_contact_info, linkedin_info)
        self.assertEqual(candidates_linkedin, None)

    def test_prepare_linkedin_info_no_linkedin_info(self):
        linkedin_info = []
        candidate_contact_info = ContactInfo(contact_info)
        candidates_linkedin = prepare_linkedin_info(candidate_contact_info, linkedin_info)
        assert candidates_linkedin is None

    def test_prepare_candidates_info(self):
        candidates = prepare_candidates_info(candidates_info, linkedin_info)
        assert candidates == expected_candidates
