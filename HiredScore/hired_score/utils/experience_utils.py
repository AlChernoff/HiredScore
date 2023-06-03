from hired_score import logger
from hired_score.consts import GAP_GRACE_PERIOD
from hired_score.models.job import Job
from hired_score.utils.date_utils import calculate_gap_between_jobs


def prepare_candidate_experience(candidate_row):
    experience_summary_response = candidate_row.get('experience')
    experience_summary = prepare_candidates_experience_info(experience_summary_response)
    enriched_experience_summary = enrich_candidate_experience_info(experience_summary)
    return enriched_experience_summary


def prepare_candidates_experience_info(experience_summary_response):
    logger.debug("Starting to prepare candidates experience info")

    experience_summary = []

    for experience in experience_summary_response or []:
        location_info = experience.get("location")
        job_description = Job(experience, location_info)
        experience_summary.append(job_description.to_dict())

    logger.debug("Finished candidates experience preparation")

    return experience_summary


def enrich_candidate_experience_info(experience_summary, gap_grace_period=GAP_GRACE_PERIOD):
    logger.debug("Enriching candidates experience with gaps information")

    if not experience_summary:
        logger.debug("Candidate has no experience")
        return {}

    experience_summary.sort(key=lambda x: x['StartDate'], reverse=True)

    for index, value in reversed(list(enumerate(experience_summary))):
        if index > 0:
            last_job = experience_summary[index]
            next_job = experience_summary[index - 1]
            logger.debug(
                f"End date of last job is {last_job.get('EndDate')}, "
                f"start date of next one is: {next_job.get('StartDate')} ")
            gap = calculate_gap_between_jobs(last_job.get('EndDate'), next_job.get('StartDate'))

            if gap and gap > gap_grace_period:
                logger.debug(f"Gap that was found is: {gap}")
                experience_summary[index]["Gap"] = f"{gap} days"

    logger.debug("Enriching candidates experience with gaps information")

    return experience_summary
