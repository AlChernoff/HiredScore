from hired_score.models.location import Location


class Job:
    def __init__(self, experience, location):
        self.company_name: str = experience.get('company_name')
        self.current_job: bool = experience.get('current_job')
        self.job_title: str = experience.get('title')
        self.start_date: str = experience.get('start_date')
        self.end_date: str = experience.get('end_date')
        self.location = Location(location)

    def to_dict(self):
        return {"Role": self.job_title, "StartDate": self.start_date,
                "EndDate": self.end_date, "Location": self.location.short_display_address}
