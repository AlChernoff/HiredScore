class CandidatesProfile:
    def __init__(self, formatted_candidate_name, formatted_linkedin_info, enriched_experience_summary):
        self.formatted_candidate_name = formatted_candidate_name
        self.formatted_linkedin_info= formatted_linkedin_info
        self.enriched_experience_summary = enriched_experience_summary

    def to_dict(self):
        return {"Name": self.formatted_candidate_name, "Linkedin": self.formatted_linkedin_info,
                              "JobExperience": self.enriched_experience_summary}