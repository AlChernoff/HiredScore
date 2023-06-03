class Name:
    def __init__(self, name):
        self.formatted_name = name.get('formatted_name')
        self.family_name = name.get('family_name')
        self.middle_name = name.get('middle_name')
        self.given_name = name.get('given_name')

    def to_dict(self):
        return {"FirstName": self.given_name,
                "LastName": self.family_name
                }
