import unittest

from hired_score.utils.date_utils import calculate_gap_between_jobs


class TestCandidateInfo(unittest.TestCase):
    def test_calculate_gap_between_jobs_default_date_format(self):
        previous_job_end_date = "Feb/23/2023"
        next_job_start_date = "Jun/23/2023"
        gap = calculate_gap_between_jobs(previous_job_end_date, next_job_start_date)
        self.assertEqual(gap, 120)

    def test_calculate_gap_between_jobs_custom_date_format(self):
        previous_job_end_date = "02/23/2023"
        next_job_start_date = "06/23/2023"
        gap = calculate_gap_between_jobs(previous_job_end_date, next_job_start_date, date_format="%m/%d/%Y")
        self.assertEqual(gap, 120)

    def test_calculate_gap_between_jobs_start_date_is_missing(self):
        previous_job_end_date = "02/23/2023"
        next_job_start_date = None
        gap = calculate_gap_between_jobs(previous_job_end_date, next_job_start_date, date_format="%m/%d/%Y")
        self.assertEqual(gap, None)

    def test_calculate_gap_between_jobs_end_date_is_missing(self):
        previous_job_end_date = None
        next_job_start_date = "06/23/2023"
        gap = calculate_gap_between_jobs(previous_job_end_date, next_job_start_date, date_format="%m/%d/%Y")
        self.assertEqual(gap, None)
