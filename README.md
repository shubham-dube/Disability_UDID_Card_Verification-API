# Disability UDID Card Verification API

This API fetches basic details with Aadhaar Number of Unique Disability ID (UDID) Card Number.

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#EndPoints)
- [Support](#Support)
- [Contribution](#Contribution)

## Features
- It Needs only UDID Number to check their Details.
- Returns the UDID Application Details.
- Easy to integrate in any of your application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubham-dube/Disability_UDID_Card_Verification-API.git
   cd Disability_UDID_Card_Verification-API
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux use `source venv/bin/activate`
   
3. Install the dependencies:
   ```bash
   pip install flask requests

4. Run the Application:
   ```bash
   python app.py
 *The API will be available at http://127.0.0.1:5000.*
 
## Usage
- Show the UDID Number input Field to the user.
- Send the entered UDID Number to the given endpoint acc. to request body.
- You will get all the details of UDID Number in JSON Format
  
## EndPoints

### Fetching UDID Details

**Endpoint:** `/api/v1/get_UDID_details`

**Method:** `POST`

**Description:** `This Endpoint takes UDID Number as input request body and return the basic details along with aadhaar number of that UDID.`

**Request Body:**
```json
{
    "UDID_Number": "HP0410719380008988"
}
```
**Response**
```json
{
    "_active": 1,
    "_result": [
        {
            "aadhaar_no": "788959802366",
            "application_number": "02040000019010098403",
            "full_name": "Rebati",
            "hospital": {
                "hospital_name": "Regional Hospital, Kullu"
            },
            "id": 5337964,
            "mobile": "9418816810",
            "pwdapplicationstatus": {
                "status_name": "UDID Card Dispatched."
            },
            "udid_number": "HP0410719380008988"
        }
    ],
    "_resultflag": 1,
    "message": "success"
}
```
**Status Codes**
- 200 OK : `Details Recieved`

## Support
For Support Contact me at itzshubhamofficial@gmail.com
or Mobile Number : `+917687877772`

## Contribution

We welcome contributions to improve this project. Here are some ways you can contribute:

1. **Report Bugs:** If you find any bugs, please report them by opening an issue on GitHub.
2. **Feature Requests:** If you have ideas for new features, feel free to suggest them by opening an issue.
3. **Code Contributions:** 
    - Fork the repository.
    - Create a new branch (`git checkout -b feature-branch`).
    - Make your changes.
    - Commit your changes (`git commit -m 'Add some feature'`).
    - Push to the branch (`git push origin feature-branch`).
    - Open a pull request.

4. **Documentation:** Improve the documentation to help others understand and use the project.
5. **Testing:** Write tests to improve code coverage and ensure stability.

Please make sure your contributions adhere to our coding guidelines and standards.
