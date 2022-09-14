var employeeAgeList
var employeeNoList
var ghsTypeList
var minmaxAge
var totalNoEmp
var isFirst = false
var isLast = false

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

        if (products == "GTT&GHS"){
            var tempStr3 = "ghsType" + String(i)
            var elements3 = document.getElementById(tempStr3)
        }

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
            if (products == "GTT&GHS")
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

document.getElementById('employeeTotalSumAssured').addEventListener('change', function() {
    document.getElementById("employeeTotalSumAssured").value = this.value * totalNoEmp
  });

document.getElementById('quote').addEventListener('click', ()=>{
    
    minmaxAge = false
    roboCalc()
    if (products == "GTT&GHS")
        var roomBoard = document.getElementById("roomBoard").value
    var empCoverage = document.getElementById("employeeCoverage").value

    if (document.getElementById("employeeTotalNo").value != "Invalid. Please recheck your input."){

        if (minmaxAge){
            alert("The age entered must be between 16 - 70 only")
        }
        else if (totalNoEmp < 5){
            alert("The total number of employees must be between 5 - 150 only")
        }
        else{
            if(products == "GTT")
                window.location.href = "/quote-gtt?empAge=" + employeeAgeList + "&empNo=" + employeeNoList + "&empCoverage=" + empCoverage
            else
                window.location.href = "/quote-gtt-ghs?empAge=" + employeeAgeList + "&empNo=" + employeeNoList + "&ghsType=" + ghsTypeList + "&roomBoard=" + roomBoard + "&empCoverage=" + empCoverage
        }
    }
    else
        alert("Invalid. Please recheck your input before submit.")
});

$(document).ready(function () {
  
    // Denotes total number of rows
    var rowIdx = 1;

    // jQuery button click event to add a row
    $(document).on('click', '#add-row', function(){   
      // Adding a row inside the tbody.


      if(products == "GTT"){
        $('tbody').append(`<tr id="R${++rowIdx}">
        <td class='align-middle'><input type='text' class='form-control text-center' id='age${rowIdx}' value='0' pattern='[0-9]+'' onchange='employeeCalc()' required></td>
        <td class='align-middle'><input type='text' class='form-control text-center' id='no${rowIdx}' value='0' pattern='[0-9]+' onchange='employeeCalc()' required></td>
        <td class='align-middle'><a class='remove'><i class='mdi mdi-minus-circle-outline align-middle minus-icon'></i></a></td>
        <td class='align-middle'><a id='add-row'><i class='mdi mdi-plus-circle-outline align-middle plus-icon'></i></a></td>
        </tr>`);

      }
      else if(products == "GTT&GHS"){
        $('tbody').append(`<tr id="R${++rowIdx}">
           <td class='align-middle'><input type='text' class='form-control text-center' id='age${rowIdx}' value='0' pattern='[0-9]+'' onchange='employeeCalc()' required></td>
           <td class='align-middle'><input type='text' class='form-control text-center' id='no${rowIdx}' value='0' pattern='[0-9]+' onchange='employeeCalc()' required></td>
           <td class='align-middle'><select id='ghsType${rowIdx}' class='form-select rb text-center'>
                <option value="EO" selected>Employee Only</option>
                <option value="ES">Employee & Spouse</option>
                <option value="EC">Employee & Children</option>
                <option value="EF">Employee & Family</option>
            </select></td>
            <td class='align-middle'><a class='remove'><i class='mdi mdi-minus-circle-outline align-middle minus-icon'></i></a></td>
            <td class='align-middle'><a id='add-row'><i class='mdi mdi-plus-circle-outline align-middle plus-icon'></i></a></td>
           </tr>`);
      }

      var tble = $('table > tbody  > tr')

      tble.each(function(index) { 

        if(index == 0 && isFirst == false){
            var tmp = $(this).closest('tr').children('td')
            tmp.each (function(index2) {
                if(index2 == tmp.length - 2){
                    tmp.children().slice(index2).remove();
                    tmp.eq(index2).html("<td class='align-middle'><a class='remove'><i class='mdi mdi-minus-circle-outline align-middle minus-icon'></i></a></td>");
                }
            });
            isFirst = true
        }

        else if (index != (tble.length - 1)){

            var tmp = $(this).closest('tr').children('td')
            tmp.each (function(index2) {
                if(index2 == tmp.length - 1){
                    tmp.children().slice(index2).remove();
                }
            });  
        }
     });
      
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

          // Gets the row number from <tr> id.
          var dig = parseInt(id.substring(1));
          let tempIdx = dig - 1

          // Modifying age id
          var count = 0
          $(this).find(':input').each (function() {

            if(count == 0)
                $(this).attr('id', 'age' + tempIdx);
            else if(count == 1)
                $(this).attr('id', 'no' + tempIdx);
            else if(count == 2)
                $(this).attr('id', 'ghsType' + tempIdx);

            count++
          });  

          // Modifying row id.
          $(this).attr('id', 'R' + tempIdx);
        });
  
        // Removing the current row.
        $(this).closest('tr').remove();

        var tble = $('table > tbody  > tr:last-child')
        var tmp = tble.children('td')
                tmp.each (function(index2) {
                    if(index2 == tmp.length-1){
                        tmp.eq(index2).html("<td class='align-middle'><a id='add-row'><i class='mdi mdi-plus-circle-outline align-middle plus-icon'></i></a></td>");
                    }
                }); 

        tble.each(function(index) {
            // if (tble.length == 1){
            //     var tmp = $(this).closest('tr').children('td')
            //     tmp.each (function(index2) {
            //         if(index2 == 4){
            //             tmp.children().slice(index2-1).remove();
            //             tmp.eq(index2-1).after("<td class='align-middle'><a id='add-row'><i class='mdi mdi-plus-circle-outline align-middle plus-icon'></i></a></td>");
            //         }
            //     });  
            // }
            // else if (index == (tble.length - 1)){

            //     var tmp = $(this).closest('tr').children('td')
            //     tmp.each (function(index2) {
            //         if(index2 == 4){
            //             tmp.children().slice(index2).remove();
            //             tmp.eq(index2-1).after("<td class='align-middle'><a id='add-row'><i class='mdi mdi-plus-circle-outline align-middle plus-icon'></i></a></td>");
            //         }
            //     });  
            // }
        });


        // Decreasing total number of rows by 1.
        rowIdx--;
        
        roboCalc()
        
      });
  });