import json
import smtplib
import os
from email.message import EmailMessage

with open("credentials.json", "r") as f:
    cred = json.load(f)

os.environ["EMAIL_ADDRESS"] = cred["EMAIL_ADDRESS"]
os.environ["EMAIL_PASSWORD"] = cred["EMAIL_PASSWORD"]

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class DoctolibMessageFormatter:
    def __init__(self, file_path="filtered_vaccination_centers.json"):
        with open(file_path, "r") as f:
            self.centers = json.load(f)


    def format_center_information(self, center_name):
        center = self.centers[center_name]
        center_address = center["location"]["address"] + " " \
                        + str(center["location"]["zip_code"]) + " " \
                        + center["location"]["city"]
        appointements = ""
        if center["calendar"] is None:
            pass
        else:
            for day, hours in center["calendar"].items():
                planning = day + " " + " ".join(hours)
                appointements += planning + "<br>"
        center_message = f"""
            <b>{center_name}</b><br>
            {center_address}<br>
            {appointements}
            You can acces their webpage here:<br>
            {center["url"]}<br><br>
        """
        return center_message
    
    def create_email_message(self):
        message = "<p>"
        for center_name in self.centers.keys():
            message += self.format_center_information(center_name)
        message += "</p>"
        html_test = f"""\
            <html>
                <body>
                    <h2 style="color:SlateGray;">Available centers</h2>
                    {message}
                </body>
            </html>
            """
        return html_test
        


class EmailSender:
    def __init__(self, receiver_address):
        self.receiver_address = receiver_address
        self.sender_address = EMAIL_ADDRESS
        self.sender_password = EMAIL_PASSWORD
    
    def send_message(self, message):

        msg = EmailMessage()
        msg['Subject'] = "Vaccines available"
        msg['From'] = self.sender_address
        msg['To'] = self.receiver_address
        msg.add_alternative(str(message), subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        
        print("Message send!")


if __name__ == "__main__":
    dmf = DoctolibMessageFormatter()
    MESSAGE = dmf.create_email_message()
    
    es = EmailSender(receiver_address=EMAIL_ADDRESS)
    es.send_message(MESSAGE)