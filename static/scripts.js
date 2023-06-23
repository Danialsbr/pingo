// Add your JavaScript code here

// Example code: show an alert when the page is loaded
document.addEventListener('DOMContentLoaded', function() {
    alert('Page loaded!');
});

// Example code: handle form submission using AJAX
document.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the form data
    const form = event.target;
    const formData = new FormData(form);

    // Perform an AJAX request
    fetch(form.action, {
        method: form.method,
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data
        console.log(data);
    })
    .catch(error => {
        // Handle any errors
        console.error(error);
    });
});
