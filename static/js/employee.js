var employeeAgeList
var employeeNoList


function employeeCalc(){
    roboCalc()
}

function roboCalc(){
    employeeNoList = []
    employeeAgeList = []
    var totalNoEmp = 0
    var table = document.getElementById("employeeTable");
    for (var i = 1, row; row = table.rows[i]; i++) {
        var tempStr = "no" + String(i)
        var elements = document.getElementById(tempStr)

        var tempStr2 = "age" + String(i)
        var elements2 = document.getElementById(tempStr2)

        if(elements == null)
            continue
        else
            var no = elements.value

        if(elements2 == null)
            continue
        else
            var age = elements2.value

        let isnum = /^\d+$/.test(no);
        let isnumage = /^\d+$/.test(age);

        if(isnum && isnumage){
            totalNoEmp += parseInt(no)
            employeeNoList[i-1] = parseInt(elements.value)
            employeeAgeList[i-1] = parseInt(elements2.value)
        }
        else{
            totalNoEmp = "Not Number"
        }
    }

    totalSumAssured = totalNoEmp * document.getElementById("employeeCoverage").value

    if (typeof totalNoEmp === 'number' && !Number.isNaN(totalNoEmp) && totalNoEmp != null) {
        document.getElementById("employeeTotalNo").value = totalNoEmp
        document.getElementById("employeeTotalSumAssured").value = totalSumAssured.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    }
    else{
        document.getElementById("employeeTotalNo").value = "Invalid. Please recheck your input."
        document.getElementById("employeeTotalSumAssured").value = "Invalid. Please recheck your input."
    }

}
document.getElementById('quote').addEventListener('click', ()=>{
    
    roboCalc()
    var empCoverage = document.getElementById("employeeCoverage").value

    if (document.getElementById("employeeTotalNo").value != "Invalid. Please recheck your input."){
        // if (totalEmp <5)
        //     alert("Minimum number of employees allowed is (5)")
        // else if(totalEmp >150)
        //     alert("Maximum number of employees allowed is (150)")
        // else
            window.location.href = "/quote?empAge=" + employeeAgeList + "&empNo=" + employeeNoList + "&empCoverage=" + empCoverage
    }
    else
        alert("Invalid. Please recheck your input before submit.")
});

$(document).ready(function () {
  
    // Denotes total number of rows
    var rowIdx = 1;

    // jQuery button click event to add a row
    $('.add-row').on('click', function () {    
      // Adding a row inside the tbody.
      $('tbody').append(`<tr id="R${++rowIdx}">
           <td><input type='text' class='form-control text-center' id='age${rowIdx}' value='0' pattern='[0-9]+'' onchange='employeeCalc()' required></td>
           <td><input type='text' class='form-control text-center' id='no${rowIdx}' value='0' pattern='[0-9]+' onchange='employeeCalc()' required></td>
           <td><a class='remove'><i class='mdi mdi-minus-circle-outline align-middle minus-icon'></i></a></td>
           </tr>`);

           roboCalc()
    });

    // jQuery button click event to remove a row.
    $('tbody').on('click', '.remove', function () {

      // Getting all the rows next to the row
      // containing the clicked button
      var child = $(this).closest('tr').nextAll();

      // Iterating across all the rows 
      // obtained to change the index
      child.each(function () {

        // Getting <tr> id.
        var id = $(this).attr('id');

        // Getting the <p> inside the .row-index class.
        var idx = $(this).children('.row-index').children('p');

        // Gets the row number from <tr> id.
        var dig = parseInt(id.substring(1));

        // Modifying row index.
        idx.html(`Row ${dig - 1}`);

        // Modifying row id.
        $(this).attr('id', `R${dig - 1}`);
      });

      // Removing the current row.
      $(this).closest('tr').remove();

      // Decreasing total number of rows by 1.
      rowIdx--;

      roboCalc()
    });
  });