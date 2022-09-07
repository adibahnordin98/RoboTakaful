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

@app.route("/gtt")
def employee_info():
    return render_template("gtt.html", title='RoboTakaful | GTT',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)

@app.route("/ghs")
def employee_info_ghs():
    return render_template("ghs.html", title='RoboTakaful | GHS',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/quote-gtt")
def quote_gtt():
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

        # Etiqa Takaful
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
        

    return render_template("quote-gtt.html", title='RoboTakaful | Quotation',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK,
                           greatEasternDict = greatEasternDict,
                           etiqaDict = etiqaDict,
                           totalSumAssured=totalSumAssured,
                           totalNoEmp=totalNoEmp,
                           empCoverage="{:,}".format(int(empCoverage)))

@app.route("/quote-ghs")
def quote_ghs():
    employeeAgeList = request.args.get('empAge')
    employeeNoList = request.args.get('empNo')
    ghsTypeList = request.args.get('ghsType')
    roomBoard = request.args.get('roomBoard')
    totalContGreatEastern = 0
    totalContEtiqa = 0
    empAge = []
    empNo = []
    ghsType = []
    totalNoEmp = 0
    tpaFee = 0

    for item in employeeNoList.split(','):
        if(item.isnumeric()):
            empNo.append(int(item))

    for item in employeeAgeList.split(','):
        if(item.isnumeric()):
            empAge.append(int(item))

    for item in ghsTypeList.split(','):
        ghsType.append(item)
            
    for idx, empAge in enumerate(empAge):

        totalNoEmp += int(empNo[idx])

        # Great Eastern Takaful
        if int(roomBoard) == 100:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 502.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 1255.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 2008.00 * empNo[idx]
            print(totalContGreatEastern)

        elif int(roomBoard) == 150:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 605.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 1512.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 2420.00 * empNo[idx]

        elif int(roomBoard) == 200:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 910.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 2275.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 3640.00 * empNo[idx]

        elif int(roomBoard) == 250:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 1247.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 3117.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 4988.00 * empNo[idx]

        elif int(roomBoard) == 300:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 1908.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 4770.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 7632.00 * empNo[idx]

        elif int(roomBoard) == 400:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 2748.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 6870.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 10922.00 * empNo[idx]

        elif int(roomBoard) == 500:
            if ghsType[idx] == "EO":
                totalContGreatEastern = totalContGreatEastern + 3516.00 * empNo[idx]
            elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                totalContGreatEastern = totalContGreatEastern + 8790.00 * empNo[idx]
            elif ghsType[idx] == "EF":
                totalContGreatEastern = totalContGreatEastern + 14064.00 * empNo[idx]

        # Etiqa Takaful
        if int(roomBoard) == 150:
            if int(empAge >= 16) and int(empAge <= 64):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 606.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 1515.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 2424.00 * empNo[idx]
            elif int(empAge >= 65) and int(empAge <= 75):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 1692.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 4230.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 6768.00 * empNo[idx]

        elif int(roomBoard) == 200:
            if int(empAge >= 16) and int(empAge <= 64):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 685.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 1713.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 2740.00 * empNo[idx]
            elif int(empAge >= 65) and int(empAge <= 75):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 2033.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 5083.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 8132.00 * empNo[idx]

        elif int(roomBoard) == 250:
            if int(empAge >= 16) and int(empAge <= 64):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 883.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 2208.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 3532.00 * empNo[idx]
            elif int(empAge >= 65) and int(empAge <= 75):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 2452.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 6130.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 9808.00 * empNo[idx]

        elif int(roomBoard) == 350:
            if int(empAge >= 16) and int(empAge <= 64):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 1083.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 2708.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 4332.00 * empNo[idx]
            elif int(empAge >= 65) and int(empAge <= 75):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 3011.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 7528.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 12044.00 * empNo[idx]

        elif int(roomBoard) == 500:
            if int(empAge >= 16) and int(empAge <= 64):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 1283.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 3208.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 5132.00 * empNo[idx]
            elif int(empAge >= 65) and int(empAge <= 75):
                if ghsType[idx] == "EO":
                    totalContEtiqa = totalContEtiqa + 3564.00 * empNo[idx]
                elif ghsType[idx] == "ES" or ghsType[idx] == "EC":
                    totalContEtiqa = totalContEtiqa + 8910.00 * empNo[idx]
                elif ghsType[idx] == "EF":
                    totalContEtiqa = totalContEtiqa + 14256.00 * empNo[idx]
        
    tpaFee = 17 * totalNoEmp
    serviceTax, stampDuty, grandTotalCont = ghsCalculate(totalContGreatEastern,tpaFee)

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

    serviceTax, stampDuty, grandTotalCont = ghsCalculate(totalContEtiqa,tpaFee)

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

    tpaFee = '{:.2f}'.format(round(tpaFee, 2))

    return render_template("quote-ghs.html", title='RoboTakaful | Quotation',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK,
                           greatEasternDict = greatEasternDict,
                           etiqaDict = etiqaDict,
                           totalNoEmp=totalNoEmp,
                           tpaFee=tpaFee,
                           roomBoard=roomBoard
                           )

############################################################### FUNCTIONS ############################################################### 

def roboCalculate(totalCont):
    serviceTax = 0.06 * totalCont
    stampDuty = 10.00
    grandTotalCont = totalCont + serviceTax + stampDuty

    return serviceTax, stampDuty, grandTotalCont

def ghsCalculate(totalCont,tpaFee):
    serviceTax = 0.06 * (totalCont + tpaFee)
    stampDuty = 10.00
    grandTotalCont = totalCont + tpaFee + serviceTax + stampDuty

    return serviceTax, stampDuty, grandTotalCont

if __name__ == '__main__':
    # HOST = "0.0.0.0"
    # PORT = 5000

    # httpserver.serve(app, host=HOST, port=PORT)
    app.run(port=5000, debug=True)
