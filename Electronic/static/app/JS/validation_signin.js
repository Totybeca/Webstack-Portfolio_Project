document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('exampleInputUserName').value;
    const password = document.getElementById('exampleInputPasswordName').value;

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