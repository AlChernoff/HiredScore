from hired_score.models.contact_info import ContactInfo


def prepare_contact_info(candidate_row):
    contact_info = candidate_row.get('contact_info')
    candidate_contact_info = ContactInfo(contact_info)
    formatted_candidate_name = candidate_contact_info.format_candidate_name()
    return candidate_contact_info, formatted_candidate_name
