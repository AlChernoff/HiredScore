class Location:
    def __init__(self, location_info):
        self.region:str = location_info.get("region")
        self.country_code:str = location_info.get("country_code")
        self.municipality:str = location_info.get("municipality")
        self.short_display_address:str = location_info.get("short_display_address")