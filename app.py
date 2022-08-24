from flask import Flask, render_template, request


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'any secret key'

# Meta
META_IMAGE_LINK = ""
META_DESCRIPTION = ""


@app.route("/")
def index():
    return render_template("home.html", title='RoboTakaful',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/login")
def login():
    return render_template("login.html", title='RoboTakaful | Login',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/signup")
def signup():
    return render_template("signup.html", title='RoboTakaful | SignUp',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/company-info")
def compony_info():
    return render_template("company-info.html", title='RoboTakaful | Company Info',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)

@app.route("/employee-info")
def employee_info():
    return render_template("employee-info.html", title='RoboTakaful | Employee Info',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/quote")
def quote():
    empNo = request.args.get('empNo')
    empCoverage = request.args.get('empCoverage')
    empList =[]
    totalNoEmp = 0

    for item in empNo:
        if(item.isnumeric()):
            empList.append(int(item))

    print(len(empList))

    if int(empCoverage) == 10000:
        totalCont = (empList[0] * 17.70 + empList[1] * 17.70 + empList[2] * 17.70 + empList[3] * 17.70 
        + empList[4] * 19.90 + empList[5] * 31.90 + empList[6] * 55.40 + empList[7] * 91.70
        + empList[8] * 151.80 + empList[9] * 262.30 + empList[10] * 435.90)

    elif int(empCoverage) == 30000:
        totalCont = (empList[0] * 36.30 + empList[1] * 36.30 + empList[2] * 36.30 + empList[3] * 36.30
        + empList[4] * 40.90 + empList[5] * 65.50 + empList[6] * 113.80 + empList[7] * 188.50
        + empList[8] * 312.00 + empList[9] * 538.70 + empList[10] * 895.70)

    elif int(empCoverage) == 50000:
        totalCont = (empList[0] * 54.90 + empList[1] * 54.90 + empList[2] * 54.90 + empList[3] * 54.90
        + empList[4] * 61.90 + empList[5] * 99.10 + empList[6] * 172.20 + empList[7] * 285.30
        + empList[8] * 472.20 + empList[9] * 815.10 + empList[10] * 1355.50)

    elif int(empCoverage) == 100000:
        totalCont = (empList[0] * 101.40 + empList[1] * 101.40 + empList[2] * 101.40 + empList[3] * 101.40
        + empList[4] * 114.40 + empList[5] * 183.10 + empList[6] * 318.20 + empList[7] * 527.30
        + empList[8] * 872.70 + empList[9] * 1506.10 + empList[10] * 2505.00)

    elif int(empCoverage) == 200000:
        totalCont = (empList[0] * 192.40 + empList[1] * 192.40 + empList[2] * 192.40 + empList[3] * 192.40
        + empList[4] * 217.40 + empList[5] * 348.10 + empList[6] * 606.20 + empList[7] * 1003.30
        + empList[8] * 1661.70 + empList[9] * 2869.10 + empList[10] * 4772.00)

    elif int(empCoverage) == 300000:
        totalCont = (empList[0] * 283.40 + empList[1] * 283.40 + empList[2] * 283.40 + empList[3] * 283.40
        + empList[4] * 320.40 + empList[5] * 513.10 + empList[6] * 849.20 + empList[7] * 1479.30
        + empList[8] * 2450.70 + empList[9] * 4232.10 + empList[10] * 7039.00)

    elif int(empCoverage) == 400000:
        totalCont = (empList[0] * 374.40 + empList[1] * 374.40 + empList[2] * 374.40 + empList[3] * 374.40
        + empList[4] * 423.40 + empList[5] * 678.10 + empList[6] * 1182.20 + empList[7] * 1955.30
        + empList[8] * 3239.70 + empList[9] * 5595.10 + empList[10] * 9306.00)
            
    elif int(empCoverage) == 500000:
        totalCont = (empList[0] * 465.40 + empList[1] * 465.40 + empList[2] * 465.40 + empList[3] * 465.40
        + empList[4] * 526.40 + empList[5] * 843.10 + empList[6] * 1470.20 + empList[7] * 2431.30
        + empList[8] * 4028.70 + empList[9] * 6958.10 + empList[10] * 11573.00)

    serviceTax = 0.06 * totalCont
    stampDuty = 10.00
    grandTotalCont = totalCont + serviceTax + stampDuty

    for item in empList:
        totalNoEmp += item

    totalSumAssured = "{:,}".format(totalNoEmp * int(empCoverage))

    return render_template("quote.html", title='RoboTakaful | Quotation',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK,
                           totalCont='{:.2f}'.format(round(totalCont, 2)),
                           serviceTax='{:.2f}'.format(round(serviceTax, 2)),
                           stampDuty='{:.2f}'.format(round(stampDuty, 2)),
                           grandTotalCont='{:.2f}'.format(round(grandTotalCont, 2)),
                           totalSumAssured=totalSumAssured,
                           totalNoEmp=totalNoEmp)
if __name__ == '__main__':
    # HOST = "0.0.0.0"
    # PORT = 5000

    # httpserver.serve(app, host=HOST, port=PORT)
    app.run(port=5000, debug=True)
