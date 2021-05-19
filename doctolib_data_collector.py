import time
from  selenium import webdriver
import json


PATH = "/usr/local/bin/chromedriver"

DOCTOLIB = "https://www.doctolib.fr/vaccination-covid-19/paris?ref_visit_motive_ids[]=6970&ref_visit_motive_ids[]=7005&force_max_limit=2"
TIME_OUT = 10  # seconds


class DoctolibDataCollector:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.centers_dict = dict()

    @staticmethod
    def available_center(calendar_text):
        """
        Check if the center proposes vaccines. Based on the text present on the calendar.
        """
        BANNED_SENTENCES = ["Aucun rendez-vous de vaccination n'est disponible dans ce lieu d'ici demain soir",
                            "Aucune disponibilité en ligne."]
        for banned_sentence in BANNED_SENTENCES:
            if banned_sentence in calendar_text:
                return False
        return True

    def format_date(self, calendar):
        """
        Can do more elegant by splitting on weekday for example and then finding information!!
        """
        week_days = {"lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"}
        timetable = dict()
        if not self.available_center(calendar):
            return None
        calendar_info = calendar.split("\n")
        for index, info in enumerate(calendar_info):
            if info in week_days:
                date = calendar_info[index] + " " +  calendar_info[index + 1]
                current_index = index + 2
                hours = []
                hour = [0, 0]
                while current_index < len(calendar_info) and len(hour) == 2:
                    hour = calendar_info[current_index].split(":")
                    if calendar_info[current_index] not in week_days:
                        hours.append(":".join(hour))
                    current_index += 1
                if hours:
                    timetable[date] = hours
        return timetable

    @staticmethod
    def format_informations(informations):
        """
        Extract address informations from center informations.
        """
        info = informations.split("\n")
        if len(info) < 3:
            return None
        vaccination_rooms = int(info[0].split(" ")[0])
        address = info[1]
        zip_code = int(info[2].split(" ")[0])
        city = " ".join(info[2].split(" ")[1:])
        location = {
            "address": address,
            "zip_code": zip_code,
            "city": city,
        }
        return location, vaccination_rooms

    @staticmethod
    def format_title(title):
        """
        Extract name and type
        """
        name = title.split("\n")[0]
        type_ = title.split("\n")[1]
        return name, type_
    
    def get_centers_information(self):
        """
        Extract information from all centers proposed in the 4 first pages of Doctolib.
        """
        self.driver.get(DOCTOLIB)
        disagree_button = self.driver.find_element_by_id("didomi-notice-disagree-button")
        disagree_button.click()
        time.sleep(0.5)

        for page_index in range(4):
            page_buttons = self.driver.find_elements_by_css_selector("a.seo-magical-link")
            page_button = page_buttons[page_index]
            page_button.click()
            centers = self.driver.find_elements_by_css_selector("div.dl-search-result")
            for center in centers:
                center_title = center.find_element_by_css_selector("div.dl-search-result-title")
                center_calendar = center.find_element_by_css_selector("div.dl-search-result-calendar")
                center_informations = center.find_element_by_css_selector("div.dl-search-result-content")
                center_url = center.find_element_by_css_selector("a.dl-button-primary.dl-button.js-search-result-path").get_attribute("href")
                t_calendar = time.time() + TIME_OUT
                while not center_calendar.text:
                    center_calendar = center.find_element_by_css_selector("div.dl-search-result-calendar")
                    center_calendar.location_once_scrolled_into_view # returns dict of X, Y coordinates
                    if time.time() > t_calendar:
                        break
                while not center_informations.text:
                    center_informations = center.find_element_by_css_selector("div.dl-search-result-specialities")
                    center.informations.location_once_scrolle_into_view
                
                center_name, center_type = self.format_title(center_title.text)
                calendar = self.format_date(center_calendar.text)
                location, vaccination_rooms = self.format_informations(center_informations.text)
                
                self.centers_dict[center_name] = {
                    "type": center_type,
                    "vaccination rooms": vaccination_rooms,
                    "calendar": calendar,
                    "location": location,
                    "url": center_url,
                }
            
        self.driver.quit()
    
    def save_centers_info_as_json(self, file_path="vaccination_centers.json"):
        """
        Save all centers informations in a json file.
        """
        with open(file_path, 'w+') as f:
            centers_json = json.dumps(self.centers_dict, ensure_ascii=False, indent=4)
            f.write(centers_json)
        print("Data collected!")


if __name__ == "__main__":
    ddc = DoctolibDataCollector()
    ddc.get_centers_information()
    ddc.save_centers_info_as_json()