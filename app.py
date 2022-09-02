from flask import Flask, render_template, request, json,jsonify


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
    employeeAgeList = request.args.get('empAge')
    employeeNoList = request.args.get('empNo')
    empCoverage = request.args.get('empCoverage')
    totalContGreatEastern = 0
    totalContEtiqa = 0
    empAge = []
    empNo = []
    totalNoEmp = 0

    for item in employeeNoList.split(','):
        if(item.isnumeric()):
            empNo.append(int(item))

    for item in employeeAgeList.split(','):
        if(item.isnumeric()):
            empAge.append(int(item))
            
    for idx, empAge in enumerate(empAge):

        totalNoEmp += int(empNo[idx])

        # Great Eastern Takaful
        if int(empCoverage) == 10000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 17.70 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 19.90 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 31.90 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 55.40 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 91.70 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 151.80 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 262.30 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 435.90 * empNo[idx]

        elif int(empCoverage) == 30000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 36.30 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 40.90 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 65.50 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 113.80 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 188.50 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 312.00 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 538.70 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 895.70 * empNo[idx]

        elif int(empCoverage) == 50000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 54.90 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 61.90 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 99.10 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 172.20 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 285.30 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 472.20 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 815.10 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 11355.50 * empNo[idx]

        elif int(empCoverage) == 100000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 101.40 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 114.40 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 183.10 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 318.20 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 527.30 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 872.70 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 1506.10 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 2505.00 * empNo[idx]

        elif int(empCoverage) == 200000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 192.40 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 217.40 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 348.10 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 606.20 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 1003.30 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 1661.70 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 2869.10 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 4772.00 * empNo[idx]

        elif int(empCoverage) == 300000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 283.40 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 320.40 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 513.10 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 894.20 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 1479.30 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 2450.70 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 4232.10 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 7039.00 * empNo[idx]

        elif int(empCoverage) == 400000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 374.40 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 423.40 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 678.10 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 1182.20 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 1955.30 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 3239.70 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 5595.10 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 9306.00 * empNo[idx]

        elif int(empCoverage) == 500000:
            if int(empAge >= 17) and int(empAge <= 35):
                totalContGreatEastern = totalContGreatEastern + 465.40 * empNo[idx]
            elif int(empAge >= 36) and int(empAge <= 40):
                totalContGreatEastern = totalContGreatEastern + 526.40 * empNo[idx]
            elif int(empAge >= 41) and int(empAge <= 45):
                totalContGreatEastern = totalContGreatEastern + 843.10 * empNo[idx]
            elif int(empAge >= 46) and int(empAge <= 50):
                totalContGreatEastern = totalContGreatEastern + 14720.20 * empNo[idx]
            elif int(empAge >= 51) and int(empAge <= 55):
                totalContGreatEastern = totalContGreatEastern + 2431.30 * empNo[idx]
            elif int(empAge >= 56) and int(empAge <= 60):
                totalContGreatEastern = totalContGreatEastern + 4028.70 * empNo[idx]
            elif int(empAge >= 61) and int(empAge <= 65):
                totalContGreatEastern = totalContGreatEastern + 6958.10 * empNo[idx]
            elif int(empAge >= 66) and int(empAge <= 70):
                totalContGreatEastern = totalContGreatEastern + 11573.00 * empNo[idx]

        # Great Eastern Takaful
        if int(empCoverage) == 20000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 28.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 1845.00 * empNo[idx]

        elif int(empCoverage) == 50000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 70.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 4613.00 * empNo[idx]

        elif int(empCoverage) == 100000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 140.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 9226.00 * empNo[idx]

        elif int(empCoverage) == 150000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 210.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 13839.00 * empNo[idx]

        elif int(empCoverage) == 200000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 280.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 18452.00 * empNo[idx]

        elif int(empCoverage) == 250000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 350.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 23065.00 * empNo[idx]

        elif int(empCoverage) == 300000:
            if int(empAge >= 16) and int(empAge <= 69):
                totalContEtiqa = totalContEtiqa + 420.00 * empNo[idx]
            elif int(empAge >= 70) and int(empAge <= 75):
                totalContEtiqa = totalContEtiqa + 27678.00 * empNo[idx]
        
    totalSumAssured = "{:,}".format(totalNoEmp * int(empCoverage))

    serviceTax, stampDuty, grandTotalCont = roboCalculate(totalContGreatEastern)

    if totalContGreatEastern != 0:
        greatEasternDict = {
            "takafulName": "Great Eastern",
            "totalCont" : '{:.2f}'.format(round(totalContGreatEastern, 2)),
            "serviceTax" : '{:.2f}'.format(round(serviceTax, 2)),
            "stampDuty" : '{:.2f}'.format(round(stampDuty, 2)),
            "grandTotalCont" : '{:.2f}'.format(round(grandTotalCont, 2))
        }
    else:
        greatEasternDict = {
                "takafulName": "None",
        }

    serviceTax, stampDuty, grandTotalCont = roboCalculate(totalContEtiqa)

    if totalContEtiqa != 0:
        etiqaDict = {
            "takafulName": "Great Eastern",
            "totalCont" : '{:.2f}'.format(round(totalContEtiqa, 2)),
            "serviceTax" : '{:.2f}'.format(round(serviceTax, 2)),
            "stampDuty" : '{:.2f}'.format(round(stampDuty, 2)),
            "grandTotalCont" : '{:.2f}'.format(round(grandTotalCont, 2))
        }
    else:
        etiqaDict = {
                "takafulName": "None",
        }
        

    return render_template("quote.html", title='RoboTakaful | Quotation',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK,
                           greatEasternDict = greatEasternDict,
                           etiqaDict = etiqaDict,
                           totalSumAssured=totalSumAssured,
                           totalNoEmp=totalNoEmp,
                           empCoverage="{:,}".format(int(empCoverage)))

############################################################### FUNCTIONS ############################################################### 

def roboCalculate(totalCont):
    serviceTax = 0.06 * totalCont
    stampDuty = 10.00
    grandTotalCont = totalCont + serviceTax + stampDuty

    return serviceTax, stampDuty, grandTotalCont

if __name__ == '__main__':
    # HOST = "0.0.0.0"
    # PORT = 5000

    # httpserver.serve(app, host=HOST, port=PORT)
    app.run(port=5000, debug=True)
