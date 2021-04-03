function openNamayande() {
    closePezeshkan();
    closeMarakez();
  document.getElementById("Namayande").style.marginTop = "-1vw";
  document.getElementById("Namayande").style.height = "6.64vw";
  document.getElementById("Namayande").style.transition = "all 0.5s";
  document.getElementById("namayande").style.display = "block";
  document.getElementById("Namayande").style.background = "#bdd62e";
  document.getElementById("Namayande").style.color = "black";
  }
  function closeNamayande(){
  document.getElementById("Namayande").style.marginTop = "0";
  document.getElementById("Namayande").style.height = "5.66vw";
  document.getElementById("namayande").style.display = "none";
  document.getElementById("Namayande").style.background = "#e6e6e6";
  document.getElementById("Namayande").style.color = "black";
  }
  function openMarakez() {
  closePezeshkan();
  closeNamayande();
  document.getElementById("Marakez").style.marginTop = "-1vw";
  document.getElementById("Marakez").style.height = "6.64vw";
  document.getElementById("Marakez").style.transition = "all 0.5s";
  document.getElementById("marakez").style.display = "block";
  document.getElementById("Marakez").style.background = "#FFB129";
  document.getElementById("Marakez").style.color = "#black";
  }
  function closeMarakez() {
  document.getElementById("Marakez").style.marginTop = "0";
  document.getElementById("Marakez").style.height = "5.66vw";
  document.getElementById("marakez").style.display = "none";
  document.getElementById("Marakez").style.background = "#cccccc";
  document.getElementById("Marakez").style.color = "black";
  }
  function openPezeshkan() {
    closeNamayande();
    closeMarakez();
  document.getElementById("Pezeshkan").style.marginTop = "-1vw";
  document.getElementById("Pezeshkan").style.height = "6.64vw";
  document.getElementById("Pezeshkan").style.transition = "all 0.5s";
  document.getElementById("pezeshkan").style.display = "block";
  document.getElementById("Pezeshkan").style.background = "#6666ff";
  document.getElementById("Pezeshkan").style.color = "white";
  }
  function closePezeshkan() {
  document.getElementById("Pezeshkan").style.marginTop = "0";
  document.getElementById("Pezeshkan").style.height = "5.66vw";
  document.getElementById("pezeshkan").style.display = "none";
  document.getElementById("Pezeshkan").style.background = "#e6e6e6";
  document.getElementById("Pezeshkan").style.color = "black";
  }