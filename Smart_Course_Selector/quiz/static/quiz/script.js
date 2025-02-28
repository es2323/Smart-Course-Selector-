
 // Smooth scrolling for anchor links
 document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault(); // Prevent default jump behavior
      const targetId = this.getAttribute('href').substring(1); // Get the target section ID
      const targetSection = document.getElementById(targetId); // Find the target section
      if (targetSection) {
        targetSection.scrollIntoView({
          behavior: 'smooth', // Enable smooth scrolling
          block: 'start' // Align to the top of the section
        });
      }
    });
  });

  //Feedback rating
  function handleRatingClick(radio) {
    // Remove the selected class from all rating numbers
    document.querySelectorAll('.rating-number').forEach(function(span) {
        span.classList.remove('bg-[#3F4F44]', 'text-white');
        span.classList.add('bg-gray-200', 'hover:bg-gray-300');
    });

    // Add the selected class to the clicked rating number
    radio.nextElementSibling.classList.remove('bg-gray-200', 'hover:bg-gray-300');
    radio.nextElementSibling.classList.add('bg-[#3F4F44]', 'text-white');
}

//Scroll to Top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

document.getElementById('mobileMenuButton').addEventListener('click', function() {
    const mobileMenu = document.getElementById('mobileMenu');
    mobileMenu.classList.toggle('max-h-0'); // Collapse
    mobileMenu.classList.toggle('max-h-96'); // Expand (adjust height as needed)
});
