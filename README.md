# Doctolib vaccine appointment searcher

> Find vaccination appointments near Paris, France. Sends email when an appointment is find.
---

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

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
    "EMAIL_ADDRESS": "name.lastname@gmail.com"
    "EMAIL_PASSWORD": "password"
}
```


### How to use

Run the main.py file
```bash
pytho3 main.py
```

[Back To The Top](#read-me-template)

---

## References
[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Twitter - [@jamesqquick](https://twitter.com/jamesqquick)
- Website - [James Q Quick](https://jamesqquick.com)

[Back To The Top](#read-me-template)

