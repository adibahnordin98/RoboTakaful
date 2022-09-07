var employeeAgeList
var employeeNoList
var ghsTypeList
var minmaxAge
var totalNoEmp

function employeeCalc(){
    roboCalc()
}

function roboCalc(){
    employeeNoList = []
    employeeAgeList = []
    ghsTypeList = []
    totalNoEmp = 0
    var table = document.getElementById("employeeTable");
    for (var i = 1, row; row = table.rows[i]; i++) {
        var tempStr = "no" + String(i)
        var elements = document.getElementById(tempStr)

        var tempStr2 = "age" + String(i)
        var elements2 = document.getElementById(tempStr2)

        var tempStr3 = "ghsType" + String(i)
        var elements3 = document.getElementById(tempStr3)

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
            ghsTypeList[i-1] = elements3.value

            if(minmaxAge != true){
                if(employeeAgeList[i-1] <16 || employeeAgeList[i-1] > 70){
                    minmaxAge = true
                }
            }
        }
        else{
            totalNoEmp = "Not Number"
        }
    }

    if (typeof totalNoEmp === 'number' && !Number.isNaN(totalNoEmp) && totalNoEmp != null) {
        document.getElementById("employeeTotalNo").value = totalNoEmp
    }
    else{
        document.getElementById("employeeTotalNo").value = "Invalid. Please recheck your input."
    }

}
document.getElementById('quote').addEventListener('click', ()=>{
    
    minmaxAge = false
    roboCalc()
    var roomBoard = document.getElementById("roomBoard").value

    if (document.getElementById("employeeTotalNo").value != "Invalid. Please recheck your input."){
        if (minmaxAge){
            alert("The age entered must be between 16 - 70 only")
        }
        else if (totalNoEmp < 5){
            alert("The minimum number of employees must be 5")
        }
        else{
            window.location.href = "/quote-ghs?empAge=" + employeeAgeList + "&empNo=" + employeeNoList + "&ghsType=" + ghsTypeList + "&roomBoard=" + roomBoard
        }
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
           <td class='align-middle'><input type='text' class='form-control text-center' id='age${rowIdx}' value='0' pattern='[0-9]+'' onchange='employeeCalc()' required></td>
           <td class='align-middle'><input type='text' class='form-control text-center' id='no${rowIdx}' value='0' pattern='[0-9]+' onchange='employeeCalc()' required></td>
           <td class='align-middle'><select id='ghsType${rowIdx}' class='form-select rb text-center'>
                <option value="EO" selected>Employee Only</option>
                <option value="ES">Employee & Spouse</option>
                <option value="EC">Employee & Children</option>
                <option value="EF">Employee & Family</option>
            </select></td>
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