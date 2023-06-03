import unittest

from tests.fixtures import experience, expected_experience, experience_for_enrichment, expected_enriched_experience, \
    experience_for_enrichment_no_gap, expected_enriched_experience_no_gap, experience_for_enrichment_small_gap, \
    expected_enriched_experience_small_gap
from hired_score.utils.experience_utils import prepare_candidates_experience_info, enrich_candidate_experience_info


class TestExperienceUtils(unittest.TestCase):
    def test_prepare_candidates_experience_info(self):
        experience_info = prepare_candidates_experience_info(experience)
        self.assertEqual(experience_info, expected_experience)

    def test_prepare_candidates_experience_info_no_experience(self):
        experience = None
        experience_info = prepare_candidates_experience_info(experience)
        self.assertEqual(experience_info, [])

    def test_enrich_candidate_experience_info(self):
        enriched_experienced_info = enrich_candidate_experience_info(experience_for_enrichment)
        self.assertEqual(enriched_experienced_info, expected_enriched_experience)

    def test_enrich_candidate_experience_info_no_gap(self):
        enriched_experienced_info = enrich_candidate_experience_info(experience_for_enrichment_no_gap)
        self.assertEqual(enriched_experienced_info, expected_enriched_experience_no_gap)

    def test_enrich_candidate_experience_info_gap_less_than_grace(self):
        enriched_experienced_info = enrich_candidate_experience_info(experience_for_enrichment_small_gap, 30)
        self.assertEqual(enriched_experienced_info, expected_enriched_experience_small_gap)
