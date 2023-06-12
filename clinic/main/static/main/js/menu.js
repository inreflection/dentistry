function toggleMenu() {
    var navbar = document.querySelector('.navbar-collapse');
    navbar.classList.toggle('show');
  }

  var navbarToggler = document.querySelector('.navbar-toggler');
  navbarToggler.addEventListener('click', toggleMenu);
