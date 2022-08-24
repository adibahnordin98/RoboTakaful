
var totalNoEmp
var empNo

function employeeCalc(){

    calclEmployeeNo()

    if (typeof totalNoEmp === 'number' && !Number.isNaN(totalNoEmp)) {
        document.getElementById("employeeTotalNo").value = totalNoEmp
        calcTotalSumAssured()
    }
    else{
        document.getElementById("employeeTotalNo").value = "Invalid. Please recheck your input."
    }

    return empNo
}

function employeeCoverage(){
    calclEmployeeNo()
    calcTotalSumAssured()
}

function calclEmployeeNo(){
    empNo = []
    totalNoEmp = 0
    
    for(let i=0; i<11; i++){
        let tempCount = i+1
        let tempStr = "no"+tempCount
        empNo[i] = parseInt(document.getElementById(tempStr).value)
        totalNoEmp += empNo[i]
    }
}

function calcTotalSumAssured(){
    totalSumAssured = totalNoEmp * document.getElementById("employeeCoverage").value
    document.getElementById("employeeTotalSumAssured").value = totalSumAssured.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

document.getElementById('quote').addEventListener('click', ()=>{
    
    var empNo = employeeCalc()
    var empCoverage = document.getElementById("employeeCoverage").value
    var totalEmp = document.getElementById("employeeTotalNo").value

    if (document.getElementById("employeeTotalNo").value != "Invalid. Please recheck your input entered."){
        if (totalEmp <5)
            alert("Minimum number of employees allowed is (5)")
        else if(totalEmp >150)
            alert("Maximum number of employees allowed is (150)")
        else
            window.location.href = "/quote?empNo=" + empNo + "&empCoverage=" + empCoverage
    }
    else
        alert("Invalid. Please recheck your input before submit.")
});