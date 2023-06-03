from hired_score import logger
from hired_score.consts import CANDIDATES_URL, LINKEDIN_DATA_URL
from hired_score.utils.api_utils import get_candidates_info, get_csv_data
from hired_score.utils.candidate_info_utils import prepare_candidates_info

logger.debug("Starting process")
candidates_info = get_candidates_info(CANDIDATES_URL)
linkedin_info = get_csv_data(LINKEDIN_DATA_URL)

if candidates_info:
    candidates = prepare_candidates_info(candidates_info, linkedin_info)

    for candidate in candidates:
        logger.info(candidate)

else:
    logger.warning("No data was received from candidates API")
