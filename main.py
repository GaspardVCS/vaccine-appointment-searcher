import time
import json
from doctolib_data_collector import DoctolibDataCollector
from doctolib_data_filter import DoctolibDataFilter
from email_sender import DoctolibMessageFormatter, EmailSender


TIME_OUT = 2 * 60  # s
RECEIVER_ADDRESS = "jeanmichel.vaccin@gmail.com"
FILTERS = {
            "calendar": True,
            "zip_code": None,
            "city": None,
        }


def main():
    ddc = DoctolibDataCollector()
    ddc.get_centers_information()
    ddc.save_centers_info_as_json()

    ddf = DoctolibDataFilter(FILTERS)
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