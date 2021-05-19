import time
import json
from doctolib_data_collector import DoctolibDataCollector
from doctolib_data_filter import DoctolibDataFilter
from email_sender import DoctolibMessageFormatter, EmailSender


TIME_OUT = 2 * 60  # s
FILE_PATH = "vaccination_centers.json"
FILTERS = {
            "calendar": True,
            "zip_code": None,
            "city": ["Paris"],
        }
# RECEIVER_ADDRESS = "jeanmichel.vaccin@gmail.fr"
RECEIVER_ADDRESS = "gas20trinier@hotmail.fr"


def main():
    ddc = DoctolibDataCollector()
    ddc.get_centers_information()
    ddc.save_centers_info_as_json()

    ddf = DoctolibDataFilter(FILE_PATH, FILTERS)
    ddf.save_centers_info_as_json()

    with open("filtered_vaccination_centers.json", "r") as f:
        centers_information = json.load(f)
    
    if centers_information:

        dmf = DoctolibMessageFormatter()
        message = dmf.create_email_message()

        es = EmailSender(receiver_address=RECEIVER_ADDRESS)
        es.send_message(message)
    print("Waiting...")
    time.sleep(TIME_OUT)

if __name__ == "__main__":
    while True:
        main()
        