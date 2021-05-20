# Doctolib vaccine appointment searcher

> Find vaccination appointments near Paris, France. Sends email when an appointment is found.
---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)

---

## Description

Using Selinium to scrap Doctolib and get information about vaccination centers near Paris. Using smtplib to send an email when an appointment is found

[Back To The Top](#read-me-template)

---

## How To Use

### Installation
Install requirements
```bash
pip3 install -r requirements.txt
```
Download chrome driver for Selenium
https://chromedriver.chromium.org/downloads

### Parameters to change
In doctolib_data_collector, change <b>PATH</b> to the path to your webdriver.

Add a credentials.json file to your folder. It will contain your <b>gmail</b> account credentials.
```json
{
    "EMAIL_ADDRESS": "name.lastname@gmail.com",
    "EMAIL_PASSWORD": "password"
}
```

Add a <b>search_informations.json</b> to your folder.
```json
{
    "location": "Paris", // your location
    "vaccines": [  // Keep only the ones that you want
        "pfizer",
        "moderna",
        "astrazeneca",
        "jansen"
    ],
    "waiting_days": 3 // You want an appointment between 1 and 3 days
}
```


### How to use

Run the main.py file
```bash
python3 main.py
```
Change EMAIL_RECEIVER address <br>
Change filters:
- <b>calendar</b>: if True, only keep centers that propose appointments else None
- <b>zip_code</b>: if list, only keep centers that are located in these zipcode else None
- <b>city</b>: if list, only keep centers that are located in these city

[Back To The Top](#read-me-template)

---
