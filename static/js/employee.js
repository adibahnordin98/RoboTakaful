
function employeeCalc(){
    var empNo = []
    var totalNoEmp = 0
    
    for(let i=0; i<11; i++){
        let tempCount = i+1
        let tempStr = "no"+tempCount
        empNo[i] = parseInt(document.getElementById(tempStr).value)
        totalNoEmp += empNo[i]
    }

    if (typeof totalNoEmp === 'number' && !Number.isNaN(totalNoEmp)) {
        document.getElementById("employeeTotalNo").value = totalNoEmp
    }
    else{
        document.getElementById("employeeTotalNo").value = "Invalid. Please recheck no of employees entered."
    }

    return empNo
}

document.getElementById('quote').addEventListener('click', ()=>{
    
    var empNo = employeeCalc()
    var empCoverage = document.getElementById("employeeCoverage").value
    var totalEmp = document.getElementById("employeeTotalNo").value

    if (document.getElementById("employeeTotalNo").value != "Invalid. Please recheck no of employees entered."){
    if (totalEmp <5)
        alert("Minimum number of employees required is (5)")
    else if(totalEmp >150)
        alert("Maximum number of employees required is (150)")
    else
        window.location.href = "/quote?empNo=" + empNo + "&empCoverage=" + empCoverage
    }
    else
        alert("Invalid. Please recheck no of employees entered before submit.")
});