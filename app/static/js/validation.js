document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('user-form');
    const confirmationMessage = document.getElementById('confirmation-message');
    const errorMessageElement = document.getElementById('error-message');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const ageInput = document.getElementById('age');

        const name = nameInput.value.trim();
        const email = emailInput.value.trim();
        const age = ageInput.value;

        let errors = [];

        // Clear previous errors
        if (errorMessageElement) {
            errorMessageElement.innerHTML = '';
            errorMessageElement.style.display = 'none';
        }
        if (confirmationMessage) {
            confirmationMessage.style.display = 'none';
        }

        // Name validation
        if (name === '') {
            errors.push('Name cannot be empty.');
        }

        // Email validation
        const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}/;
        if (!emailRegex.test(email)) {
            errors.push('Please enter a valid email address.');
        }

        // Age validation
        const ageInt = parseInt(age);
        if (isNaN(ageInt) || ageInt <= 0) {
            errors.push('Age must be a positive number.');
        }

        if (errors.length > 0) {
            if (errorMessageElement) {
                errorMessageElement.innerHTML = errors.join('<br>');
                errorMessageElement.style.display = 'block';
            }
        } else {
            // If validation passes, simulate form submission (e.g., via AJAX or just show confirmation)
            // In a real app, you'd send this data to the server here.
            console.log('Form submitted successfully:', { name, email, age });

            // Display confirmation message
            if (confirmationMessage) {
                confirmationMessage.style.display = 'block';
            }

            // Optionally clear the form after successful submission
            form.reset();
        }
    });
});
