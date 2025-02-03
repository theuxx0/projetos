const toggleMenu = () => {
    const nav = document.querySelector('nav ul');
    nav.classList.toggle('active');
  };
  
  document.querySelector('nav').addEventListener('click', toggleMenu);