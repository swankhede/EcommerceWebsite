 var flag = 0;
  function navbar() {
    
    if (flag==0) {
      document.getElementById("mobileNavbar").style.display = "block";
      console.log(flag);
      flag++;
    }else {
      document.getElementById("mobileNavbar").style.display = "none";
      console.log(flag);
      flag=0;
    }

  }