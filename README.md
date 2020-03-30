# Flask101

Workshop introducing how to use Flask for API development

## Installation

### 1. Workshop Repo
(Assuming that you have git installed. If not, refer to the [official tutorial](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))


1. In your terminal/command prompt, navigate to the folder you would like to install the project files to. (ex.`cd path/to/folder/`) 
2. Run the following: `git clone https://github.com/bbwong23/flask101.git`


### 2. Python & Libraries
**Install python3 to your computer if not already**

**(Mac)** open your terminal and run `brew install python3`

**(Windows)** download the windows python installer [here](https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe)

To confirm that you have successfully downloaded python, on your terminal/command prompt run the following: `python --version` or `python3 --version`
```bash
user:~$ python --version
Python 3.7.3
```

(**NOTE:** if the command works with `python3` instead of `python`, use `python3` or `pip3` instead when instructed to run commands using `python` or `pip`)

**Install the python libraries needed**
1. In your terminal/command prompt, navigate inside the project directory downloaded in step 2 under **Workshop Repo** above. 
2. Run the following: `pip install -r requirements.txt`


### 3. Postman
Download the Postman application [here](https://www.postman.com/downloads/)



## Folder Structure

- `sample/` This directory contains all the sample project files used in the workshop presentation for the live demos
- `service/` This directory contains the source code for the service used in the lab. This includes the functions to a calculator that returns the raw results. **Nothing in this folder should be modified.**
- `tests/` This directory contains the test collection that you will import to Postman to validate that you have set up your API correctly. Included in this collection are also the tests used in the live demo. 


## Lab Instructions
In this lab, you will be creating an API that exposes a calculator's functions to the consumer (can either be an individual, a script, or an application). Typically a controller is the file that handles all the routing and payload processing. So, the script that will be worked on for this lab is `calculator_controller.py`. A skeleton is provided with comments including step by step instructions on what to figure out. 

There are 5 things that need to be completed in the controller file:
1. Import the necessary libraries
2. Create the Flask application object
3. Define the routes for your API according to the path and REST call type specified in the comments
4. Parse the input request according to the type specified
5. Run the Flask app object


Feel free to use the files from the `sample` folder as reference to the topics discussed in the workshop. The comments in the controller will also include a hint specifying which sample file to reference. If you get absolutely stuck, there is a solution file you can use as reference as well `calculator_controller_solution.py`, but try your best not to be tempted to just jump straight to the solution without trying to solve this by yourself!

Good luck!

### Lab Testing/Validation

#### Start up your API server
1. In your terminal/command prompt, navigate to the directory with the Flask file (the python file where you define your Flask app)
2. Run the following: `python flaskfile.py` (replace the file name with whatever you are trying to run). If there are no errors in the your file, then you should get something that looks like this in return:
```bash
user:~$ python3 flaskfile.py
 * Serving Flask app "sample" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)

```
With this, your API server is up and running! 

#### Import the test collection into Postman:

1. Click on "Import" in the top left corner of the Postman window
2. Select the `flask101.postman_collection.json` file from the `tests/` folder to import
3. In the left menu, select the "Collections" tab
4. Navigate to the folder labeled as "flask101" and expand the folders to access the test requests
5. To run each test request, simply select the request from the folder and click the blue "Send" button on the right. Be sure to run your flask application first before running the request
6. To confirm that the request is as expected, click on the "Test Results" tab in the response section to see if all test cases passed
