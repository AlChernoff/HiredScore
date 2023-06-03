import json
import re

from hired_score import logger
from hired_score.models.candidates_profile import CandidatesProfile
from hired_score.utils.contact_info_utils import prepare_contact_info
from hired_score.utils.experience_utils import prepare_candidate_experience


def prepare_linkedin_info(candidate_contact_info, linkedin_info):
    if candidate_contact_info.phone:
        candidates_contact_details = re.sub(r'\W', '', candidate_contact_info.phone)
        search_field = "Phone Number"
    elif candidate_contact_info.email:
        candidates_contact_details = candidate_contact_info.email
        search_field = "Email"
    else:
        logger.debug(f"No contact data was found for candidate! Can't enrich profile with LinkedIn")
        return
    for row in linkedin_info:
        if row.get(search_field) == candidates_contact_details:
            return row["Linkedin"]


def prepare_final_output(candidates_profile, return_json=False):
    if return_json:
        return json.dumps(candidates_profile.to_dict())
    else:
        first_name = candidates_profile.formatted_candidate_name.get("FirstName")
        last_name = candidates_profile.formatted_candidate_name.get("LastName")
        candidates_work_experience = ''
        candidates_details = f"Hello {first_name + ' ' + last_name}\n" \
                             f"Linkedin: {candidates_profile.formatted_linkedin_info}\n"
        for experience in candidates_profile.enriched_experience_summary:
            gap = f"\nGap in CV for {experience.get('Gap')}" if experience.get("Gap") else ""
            candidates_work_experience = '\n'.join(['Worked as: {}, From {} To {} in {} {}'.format(
                experience.get('Role'), experience.get('StartDate'), experience.get('EndDate'),
                experience.get("Location"), gap), candidates_work_experience])
        return "".join([candidates_details, candidates_work_experience])


def prepare_candidates_info(candidates_info, linkedin_info):
    candidates = []
    formatted_linkedin_info = None

    for candidate_row in candidates_info:
        candidate_contact_info, formatted_candidate_name = prepare_contact_info(candidate_row)

        if linkedin_info:
            formatted_linkedin_info = prepare_linkedin_info(candidate_contact_info, linkedin_info)

        enriched_experience_summary = prepare_candidate_experience(candidate_row)
        candidates_profile = CandidatesProfile(formatted_candidate_name, formatted_linkedin_info,
                                               enriched_experience_summary)
        candidates.append(prepare_final_output(candidates_profile))

    return candidates
