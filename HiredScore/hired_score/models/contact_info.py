from hired_score import logger
from hired_score.models.name import Name


class ContactInfo:
    def __init__(self, contact_info):
        self.email: str = contact_info.get('email')
        self.phone: str = contact_info.get('phone')
        self.name: Name = Name(contact_info.get('name', {})) if contact_info.get('name') else None

    def to_dict(self):
        return self.name.to_dict()

    def format_candidate_name(self):
        logger.debug("Starting to format candidates name")

        if not self.name:
            logger.warning(
                f"Please check data of candidate with phone: {self.phone}, his name is empty!")
            return

        return self.name.to_dict()
