# Project: Design a QR Code Generator
Assume that you're working for a popular restaurant. During evening shift, there is a lot of crowd at the restaurant and it's hard to get extra waiters for few hours to serve the customers.

The restaurant owner has asked for help to see if something can be done to handle this rush of evening customers. 

You come up with a technology solution.
<strong>QR Code Generator for ordering food by customers.</strong>

The idea is simple: Customers come and sit on available tables. Instead of a waiter going and attending to them, a QR Code will be placed on the table.
Customers will scan the QR Code with their mobile and it will take them to a website which will have the menu.

Now customers can browse all the menu from there, see the prices and order online.
Waiters would only be needed to bring food to the customers.  
After finishing their meal, the customers will be able to scan the same QR Code and pay the bill online.

This will save about 50% of waiters effort, thus reducing workforce requirement for the restaurant owner

With this goal in mind,  
let's start working on our Python QR Code Generator

You can view all the code directly from Github: [QRCODE_GENERATOR](https://github.com/suka1557/qrcode_generator/)

# Step 1: Create Virutal Environment
To create a virtual environment using the built-in <strong>venv</strong> module, which is available in Python 3.3 and later versions

Navigate to your project directory
```bash
cd path/to/your/project
```
Run the following command to create a virtual environment with the name <strong><i>qrcode_env</i></strong>
```bash
python -m venv qrcode_env
```

After this command run, you should see a new folder created inside your project root with the name <strong><i>qrcode_env</i></strong>
Your environment is created now. You need to activate it to use the packages available inside the environment.

To activate the environment
use the following command on Linux/Mac
```bash
source qrcode_env/bin/activate
```
and if you're using a Windows system, use the following command
```bash
qrcode_env\Scripts\activate
```
Once the environment has been activated, you can use <strong>pip list</strong> to see
list of packages that are installed in your python environment.
For this project, we'll be needing to install a few packages, which are listed in
<i>requirements.txt</i> file. Download this file and place it inside your project root folder.

To install all the packages in your environment directly,
Run the following command on terminal or command prompt.
```bash
pip install -r requirements.txt
```

Once this is done, you've all the packages installed that you need to work on this project.
Let's move to 2nd step now.

# Step 2: Create Project Structure
For any production grade project, our code should be modular and placed into different folders which allows any person to see the project structure and understand where they can find a particular piece of code.

For this project, we'll not make it too complicated and create 4 folders:
* <i>src</i>
* <i>configs</i>
* <i>api</i>
* <i>utils</i>

Let's understand usage of each of these folders.

&nbsp;&nbsp;&nbsp;&nbsp; <strong>src/</strong> 

Purpose: This folder usually contains the main source code of your project.

Content:

    Python modules and packages that form the core functionality of your application.
    Organize your code into modules related to specific features or components.
    The entry point of your application may reside in this directory.

&nbsp;&nbsp;&nbsp;&nbsp; <strong>configs/</strong> 

Purpose: Store configuration files and settings for your project.

Content:

    Configuration files for different environments (development, production, testing).
    Constants and settings that need to be centralized.
    Database connection settings, API keys, etc.

&nbsp;&nbsp;&nbsp;&nbsp; <strong>api/</strong> 

Purpose: If your project involves building a web API, this folder can house the code related to API endpoints and their logic.

Content:

    API routes and controllers.
    Serialization and validation logic for incoming and outgoing data.
    Middleware or other components related to API handling.

&nbsp;&nbsp;&nbsp;&nbsp; <strong>utils/</strong> 

Purpose: House utility functions and helper modules that can be used across different parts of your project.
Content:

    Reusable functions, classes, or modules that don't fit neatly into specific components.
    Helper functions for common tasks, logging, error handling, etc.

To create these folders in one single command, use the below:
```bash
mkdir src api configs utils
```

Now the project structure is ready. Now we can start getting our hands dirty with real python code.

# Step 3: __init__.py 
In the root directory of your project, create a file named: <strong><i>__init__.py</i></strong>

and put the following lines of code inside this file.
```bash
import sys
sys.path.append("./")
```

This will serve 2 purpose:
* The presence of an __init__.py file in a directory signals to Python that the directory should be treated as a package or module.
* <strong>sys.path</strong> is a list that contains directories where Python looks for modules to import. <strong>sys.path.append("./")</strong> adds the current directory (./) to the sys.path list. This modification allows the Python interpreter to search for modules in the current directory when attempting to import them. So now you'll be able to mport modules from the current directory or its subdirectories , without running into <strong>Module Not Found Error</strong>

# Step 4: QR Code Generator function
Let's create a function which will require some arguments and using those arguments, it will generate a QR Code.

Create a file named <strong>qr_code_generator.py</strong> inside the <strong>src/</strong> folder.

Import the qrcode package first. Add the below line
```bash
import qrcode
```
Next create a blank function template.
```bash
def generate_qr_code_with_data(data_to_be_encoded: dict):
    """
    function that takes in dictinary of data to be encoded into QR Code 
    and generates a QR Code image file
    
    """

    qr_code = ''
    return qr_code
```

It is always a good idea to include information about the function in the <strong>docstring</strong> - <i>triple quoted string inside the function</i>

Currently this function return an empty text. We'll fill the details further.

Let's understand the argument of the function:
* <strong>data_to_be_encoded: dict</strong>  

Why have we chosen a dict to get the parameters ? 
* The ultimate goal of the project is to create a REST API endpoint which anybody can call to get the QR Code. In API Requests, data is generally sent over network in JSON format which corresponds to dictionary in Python. So it makes sense to have the function expect a dict
* Dictionary is a flexible data structure - we can add or reduce keys in the dictionary without needeing to change the function arguments

Great!
So let's now think what information we need to encode in the QR Code.
* Table No: which table this order is for
* URL/Website: Base URL or website where restaurant Menu is visible
* Customer Id: An Id for the customer who has ordered

These 3 parameters should be there in the <strong>data_to_be_encoded</strong> dictionary. So let's unpack these arguments inside the function.

```bash
def generate_qr_code_with_data(data_to_be_encoded: dict):
    """
    function that takes in dictinary of data to be encoded into QR Code 
    and generates a QR Code image file
    
    """

    customer_id = str(data_to_be_encoded["customer_id"])
    base_url = str(data_to_be_encoded["url"])
    table_no = str(data_to_be_encoded["table_no"])

    custom_url = base_url + "?customer_id=" + customer_id + "?table_no=" + table_no

    qr_code = ''
    return qr_code
```

So we have combined table no, customer id and base url into a custom url, which will take each customer to menu ordering website and the backend will know from the url , the customer id and table no. 
To illustrate, suppose our base_url = 'https://awesome.restaurant.com'

* Table : 2, Customer: 56 --> custom_url = 'https://awesome.restaurant.com?customer_id=56?table_no=2'
* Table : 11, Customer: 143 --> custom_url = 'https://awesome.restaurant.com?customer_id=143?table_no=11'

The type of custom_url is <strong>string</strong> type because the qrcode package all information to be encoded to be given as a string.

Now we have the information that we want to encode in QR Code. Let's now actually encode that information using qrcode package.

Add the following lines to the function:
```python
def generate_qr_code_with_data(data_to_be_encoded: dict):
    """
    function that takes in dictinary of data to be encoded into QR Code 
    and generates a QR Code image file
    
    """

    customer_id = str(data_to_be_encoded["customer_id"])
    base_url = str(data_to_be_encoded["url"])
    table_no = str(data_to_be_encoded["table_no"])

    custom_url = base_url + "?customer_id=" + customer_id + "?table_no=" + table_no
    try:
        qr = qrcode.QRCode(
                version=1,  
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

        qr.add_data(custom_url)
        qr.make(fit=True)

        qrcode_img = qr.make_image(fill_color="black", back_color="white")
        qrcode_img.save("qrcode.png")

        return {"Status":"QR Code Generated Successfully"}
    except Exception as e:
        return {"Status": f"Error in QR generation process - {e}"}
```

Let's break down each piece of code to understand what's happening:
1. Import the qrcode module:

```python
import qrcode
```
This line imports the qrcode module, which provides functionality to create QR codes.

2. Create a QRCode object with specified parameters:

```python

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
```
    - version: Specifies the size of the QR code. In this case, it's set to 1.  
    
    - error_correction: Sets the error correction level. Here, it's set to low (ERROR_CORRECT_L).
    
    - box_size: Defines the size of each box (pixel) in the QR code.
    
    - border: Specifies the number of boxes to use for the border around the QR code.

3. Add data to the QR code:

```python
qr.add_data(custom_url)
```
This line adds the data (in this case, a custom URL) to the QR code.

4. Make the QR code:

```python
qr.make(fit=True)
```
This line generates the QR code. The fit=True parameter is used to automatically adjust the size of the QR code to fit the data.

5. Create an image of the QR code:

```python
qrcode_img = qr.make_image(fill_color="black", back_color="white")
```
This line generates an image of the QR code with specified fill color (black) and background color (white).

6. Save the QR code image to a file:

```python
qrcode_img.save("qrcode.png")
```
Finally, this line saves the generated QR code image to a file named "qrcode.png" in the current working directory.

After saving the file, we are returning a Status Message which will be sent as JSON Response to a client calling the API.  
Now we have the function ready. You can test this function manually by calling it with different parameters stored in a dict. In future projects, we'll go more in depth of <strong> - How to do testing of production grade projects in Python?</strong>

# Step 5: Create REST API Endpoint
Now we have the function ready. We will now be creating a REST API endpoint using FastAPI framework. This endpoint, we can deploy on any server we want (on Cloud or On Premises)

Create a new file named <strong>qr_endpoint.py</strong> inside <strong>api/</strong> folder

Add the following import statements at the top
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
```

We'll be using <b>BaseModel</b> from <b>pydantic</b> to define a class of the type of data that our endpoint will expect in JSON payload. Using pydantic has the benefit that it takes care of <strong>data validation</strong> on its own.

We have also imported <b>Optional</b> from typing to define Optional parameters in the class. It'll become clear in a moment.

Let's define the class now. Add the below lines of code in <b>qr_endpoint.py</b>
```python
#Define a Pydantic basemodel for kind of data expected in request body
class QRData(BaseModel):
    customer_id: str
    table_no: int
    url: Optional[str]
```

Let's understand what's happening inside this class. The class <b>QRData</b> inherits from <b>BaseModel</b> class. We know that we need 3 parameters to define a custom url:  

    - table_no: required parameter, type: string
    - customer_id: required parameter, type: string
    - url: Optional parameter, type: string

Let's re-look at our business scenario. We are developing this endpoint for a restaurant. The homepage address of the restaurant where the <i>food menu</i> will be stored is not going to change with each request.  

So it's better as an Optional parameter. In addition, we should also define the default value of the homepage url of the restaurant, so that if a request doesn't contain the url parameter, it will automatically have the default value.

This is a good usecase of <b>configs/</b> directory. It should contain things that are needed across the project and that are not going to change frequently.

In the <b>configs/</b> folder, create a file named <b>config.py</b> and add the following line inside that file:
```python
BASE_URL = 'https://hotelawesome.newly.com'
```

Now let's import this into our <strong>qr_endpoint.py</strong> file and add it as default value for Optional parameter.
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from configs.config import BASE_URL
from src.qr_code_generator import generate_qr_code_with_data

#Define a Pydantic basemodel for kind of data expected in request body
class QRData(BaseModel):
    customer_id: str
    table_no: int
    url: Optional[str] = BASE_URL
```

We've also imported the function to generate QRCode from the <b>src/</b> folder.

Let's now define the endpoint. Since this endpoint will expect some data to be sent, we'll create an endpoint that accepts <b>POST</b> requests.

Add the below lines of code in <strong>qr_endpoint.py</strong> file:
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from configs.config import BASE_URL
from src.qr_code_generator import generate_qr_code_with_data

qr_api = FastAPI()

#Define a Pydantic basemodel for kind of data expected in request body
class QRData(BaseModel):
    customer_id: str
    table_no: int
    url: Optional[str] = BASE_URL

@qr_api.post('/generate_qr_code')
def generate_qr(qr_data: QRData):
    return generate_qr_code_with_data(data_to_be_encoded=qr_data)

```

So we first instantiate the FastAPI object from fastapi. Then define an endpoint with the name - <b>/generate_qr_code</b> that accepts <b>POST</b> request. 

In the JSON body of the request, the endpoint would expect to get data of type <b>QRData</b>, which we have defined above using <b>BaseModel</b> class from <b>pydantic</b>

To run this api locally, you need to install an ASGI server: uvicorn. Run the following command on terminal/command prompt
```bash
pip install uvicorn
```

Now to start the webserver locally to run this endpoint, run the following command
```bash
uvicorn api.qr_endpoint:qr_api --reload
```
Before running this command make sure that you are in the root directory of this project. After running this command, it will start running the endpoint on local host.  
You can use a tool like <b>Postman</b> to send <b>POST</b> requests at the address: https://localhost:8000/generate_qr_code and see the results. The Port No - <b>8000</b> may change on your system. The exact port number, you'll be able to see as the output after running the command to start the api

### With this we have completed our QR Code generator project and deployed it locally using REST API. 

#### Happy Pythoning !!!