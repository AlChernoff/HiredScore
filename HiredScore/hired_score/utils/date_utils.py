from datetime import datetime

from hired_score import logger


def calculate_gap_between_jobs(previous_job_end_date, next_job_start_date, date_format='%b/%d/%Y'):
    if not previous_job_end_date or not next_job_start_date:
        logger.warning("Date is missing - can't calculate gap")
        return
    previous_job_end_date = datetime.strptime(previous_job_end_date, date_format)
    next_job_start_date = datetime.strptime(next_job_start_date, date_format)
    gap = next_job_start_date - previous_job_end_date
    return gap.days
