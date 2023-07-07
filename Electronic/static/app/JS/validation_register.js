// Perform form validation on submit
document.querySelector('form').addEventListener('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Perform additional validations
    const first_name = document.getElementById('id_FirstName').value;
    const last_name = document.getElementById('id_FastName').value;
    const email = document.getElementById('id_email').value;
    const username = document.getElementById('id_username').value;
    const password = document.getElementById('id_password').value;

    if (first_name.trim() === '') {
      alert('Please enter your first name');
      return;
    }

    if (last_name.trim() === '') {
      alert('Please enter your last name');
      return;
    }

    if (email.trim() === '') {
      alert('Please enter your email');
      return;
    }
    // Email format validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Please enter a valid email address');
      return;
    }

    if (username.trim() === '') {
      alert('Please enter a username');
      return;
    }

    if (password.trim() === '') {
      alert('Please enter a password');
      return;
    }

    // If all validations pass, submit the form programmatically
    this.submit();
  });