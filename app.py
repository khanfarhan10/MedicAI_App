"""
MedicAI is an initiative by Team MLXTREME for the Hackathon.
Medical Artificial Intelligence.
Assistive Technology for better Electronic Healthcare Facilities for a brighter tomorrow.

To get a demo, Run app.py and visit the link which comes up.

Regards,
Team MLXTREME

Instructions For Running :

MedicAIEnv\Scripts\activate
To deactivate base - conda.bat deactivate
cd WebsiteFiles/FlaskApp
python app.py


TODO :
Favicon
"""

# import Flask Library

from flask import Flask, render_template, request, url_for, send_from_directory, jsonify
import os

# using datetime module
import datetime
# define constants that don't change throughout the program and are required in general
LOGIN_HEADER = "User Logged In : "
REGISTER_HEADER = "User Registered : "
GITHUB_VIEW_HEADER = "User Visited GitHub : "

app = Flask(__name__, static_folder="assets")

"""
# CODE FOR IP ADDRESS
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    IP_ADDRESS = jsonify({'ip': request.remote_addr}), 200
    print(request.remote_addr)
    return IP_ADDRESS
"""


@app.route('/')
def home1():
    return render_template('homepage.html')


@app.route('/index.html')
def home2():
    return render_template('homepage.html')


@app.route('/index')
def home3():
    return render_template('homepage.html')


@app.route('/home')
def home4():
    return render_template('homepage.html')


@app.route('/home.html')
def home():
    return render_template('homepage.html')


@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')


@app.route('/homepage.html')
def homepage1():
    return render_template('homepage.html')


@app.route('/homepage.html')
def homepage2():
    return render_template('homepage.html')


@app.route('/logs')
def logs():
    with open(os.path.join(os.getcwd(), "Logs", "log1.txt"), "r") as f:
        content = f.readlines()

    # using list comprehension
    listToStr = '<br>'.join([str(elem) for elem in content])
    # print(listToStr)
    return listToStr


def write_line(LineText, Filename):
    with open(Filename, "a+") as f:
        f.write(LineText+str("\n"))
    return LineText


def write_log(Text, Header=None, TxtFileName=os.path.join(os.getcwd(), "Logs", "log1.txt"), TimeNow=str(datetime.datetime.now())):
    # Try to write Logs for each timing
    # write a timing, header line and a dictionary separated by spaces
    """
    TIMESTAMP:
    HEADER_LINE :

    Data1:Value1
    Data2:Value2
    """
    write_line(TimeNow, TxtFileName)

    if Header is not None:
        # single line Header
        write_line(Header+str(request.remote_addr), TxtFileName)

    # handle single and iterable text separately
    if type(Text) is tuple:
        for eachText in Text:
            write_line(eachText, TxtFileName)
    elif type(Text) is dict:
        for eachPair in zip(Text.keys(), Text.values()):
            write_line(eachPair[0]+" : "+eachPair[1], TxtFileName)
    else:
        # single line given
        write_line(Text, TxtFileName)
    # for cleanliness add a blank line to log
    write_line('\n', TxtFileName)
    return 1


@app.route('/login', methods=['POST'])
def loginsuccess():
    LoginUserEmail = request.form['LoginUserEmail']
    LoginUserPassword = request.form['LoginUserPassword']
    try:
        LoginUserRememberMe = request.form['LoginUserRememberMe']
    except:
        LoginUserRememberMe = "off"

    # Creating Login Dictionaries
    LoginDict = {'LoginUserEmail': LoginUserEmail,
                 'LoginUserPassword': LoginUserPassword,
                 'LoginUserRememberMe': LoginUserRememberMe}
    write_log(Text=LoginDict, Header=LOGIN_HEADER)
    # print(LoginUserEmail, LoginUserPassword, LoginUserRememberMe)
    # Return whether login was successfull or not & redirect succesfully to dashboard in 3 secs.
    # Loading Circle ++
    return 'Hi You are now Logged in!!'
    # return render_template('success.html')


@app.route('/register', methods=['POST'])
def registersuccess():
    RegisterUserName = request.form['RegisterUserName']
    RegisterUserEmail = request.form['RegisterUserEmail']
    RegisterUserPassword = request.form['RegisterUserPassword']

    try:
        RegisterPolicy = request.form['RegisterPolicy']
    except:
        RegisterPolicy = "off"

    # Creating Login Dictionaries
    RegisterDict = {'RegisterUserName': RegisterUserName,
                    'RegisterUserEmail': RegisterUserEmail,
                    'RegisterUserPassword': RegisterUserPassword,
                    'RegisterPolicy': RegisterPolicy}
    write_log(Text=RegisterDict, Header=REGISTER_HEADER)
    # Return whether login was successfull or not & redirect succesfully to dashboard in 3 secs.
    # Loading Circle ++ TODO
    return 'Hi You are now Registered!!'
    # return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
