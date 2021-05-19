import json


class DoctolibDataFilter:
    def __init__(self, file_path, filters):
        with open(file_path, "r") as f:
            self.centers_info = json.load(f)
        self.filters = filters
        self.filtered_centers = dict()
        self.filter_vaccination_center()
    
    def filter_calendar(self, calendar):
        if self.filters["calendar"] is None:
            return True
        return (calendar is not None)
    
    def filter_zip_code(self, zip_code):
        if self.filters["zip_code"] is None:
            return True
        return (zip_code in self.filters["zip_code"])

    def filter_city(self, city):
        if self.filters["city"] is None:
            return True
        return (city in self.filters["city"])
    
    def filter_center(self, center_info):
        calendar_condition = self.filter_calendar(center_info["calendar"])
        zip_code_condtion = self.filter_zip_code(center_info["location"]["zip_code"])
        city_condition = self.filter_city(center_info["location"]["city"])
        return (calendar_condition and zip_code_condtion and city_condition)
    
    def filter_vaccination_center(self):
        for center_name, center_info in self.centers_info.items():
            if self.filter_center(center_info):
                self.filtered_centers[center_name] = center_info
    
    def save_centers_info_as_json(self, file_path="filtered_vaccination_centers.json"):
        with open(file_path, 'w+') as f:
            centers_json = json.dumps(self.filtered_centers, ensure_ascii=False, indent=4)
            f.write(centers_json)
        print(f"Data filtered!")
    



if __name__ == "__main__":
    FILE_PATH = "vaccination_centers.json"
    FILTERS = {
                "calendar": True,
                "zip_code": None,
                "city": None,
              }
    ddf = DoctolibDataFilter(FILE_PATH, FILTERS)
    ddf.save_centers_info_as_json()
    