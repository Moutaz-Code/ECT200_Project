document.getElementById("BookButton").addEventListener("click", function() {
  document.getElementById("BookContent").style.display = "block";
  document.getElementById("ManageContent").style.display = "none";
  document.getElementById("FlightContent").style.display = "none";
  });
  
document.getElementById("ManageButton").addEventListener("click", function() {
  document.getElementById("BookContent").style.display = "none";
  document.getElementById("ManageContent").style.display = "block";
  document.getElementById("FlightContent").style.display = "none";
  });
document.getElementById("FlightButton").addEventListener("click", function() {
  document.getElementById("BookContent").style.display = "none";
  document.getElementById("ManageContent").style.display = "none";
  document.getElementById("FlightContent").style.display = "block";
  });
  
