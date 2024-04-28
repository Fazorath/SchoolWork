document.addEventListener("DOMContentLoaded", function() {
    const subscribeButton = document.getElementById("submitButton");
    const formContainer = document.getElementById("subscribeFormContainer");
  
    subscribeButton.addEventListener("click", function() {
      formContainer.innerHTML = ''; // Clear existing content
      fetch('subscribe.html') // Fetch the subscribe.html file
        .then(response => response.text())
        .then(html => {
          formContainer.style.display = "block"; // Display the form
          formContainer.innerHTML = html; // Inject the form HTML
        });
    });
  });
  