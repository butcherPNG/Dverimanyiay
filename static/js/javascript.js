
document.addEventListener("scroll", function () {
    let header = document.querySelector("#nav");
    nav.style.backgroundColor = window.scrollY > 0 ? "green" : "";
  });



  const button = document.querySelector('#ccc');
  const navigation = document.querySelector('#nav');
  
  button.addEventListener('click', function() {
    navigation.classList.toggle('active');
    navigation.classList.toggle('colored');
  });


