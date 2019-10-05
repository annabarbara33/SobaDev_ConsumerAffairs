var array = [];

function myFunction1() {
  // Get the checkbox
  var checkBox = document.getElementById("customCheck1");
  // Get the output text
  var text = document.getElementById("text1");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
  //  text.style.display = "block";
    array.push("Home");
  } else {
 //   text.style.display = "none";
    array.pop();
  }
}

function myFunction2() {
  // Get the checkbox
  var checkBox = document.getElementById("customCheck2");
  // Get the output text
  var text = document.getElementById("text2");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
   // text.style.display = "block";
    array.push("Car");
  } else {
 //   text.style.display = "none";
    array.pop();
  }
}

function myFunction3() {
  // Get the checkbox
  var checkBox = document.getElementById("customCheck3");
  // Get the output text
  var text = document.getElementById("text3");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
   // text.style.display = "block";
    array.push("Loan");
  } else {
    //text.style.display = "none";
    array.pop();
  }
}

function myFunction4() {
  // Get the checkbox
  var checkBox = document.getElementById("customCheck4");
  // Get the output text
  var text = document.getElementById("text4");

  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
   // text.style.display = "block";
    array.push("Other");
  } else {
   // text.style.display = "none";
    array.pop();
  }
}
function myFunction5() {
  // Get the checkbox
  mySelect = document.getElementsByName('credit_score')[0];
  var text = mySelect.options[mySelect.selectedIndex].text;
  array.push(text);
  //alert(array.toString());
  //   alert(text);

}
function myFunction6() {
  // Get the checkbox
  mySelect = document.getElementsByName('report_items')[0];
  var text = mySelect.options[mySelect.selectedIndex].text;
  array.push(text);
  //alert(array.toString());
  //   alert(text);

}
function myFunction7() {
    var first = document.getElementById("zipcodebox").value;
    array.push(first);
    // alert(first);
}
function myFunction8() {
    //
    // alert("hhhhhhh");
    // array.push("123");
    //  array.push("456");

    document.getElementById("p3").innerHTML = array;
}

