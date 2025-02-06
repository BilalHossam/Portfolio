document.addEventListener('DOMContentLoaded', () => {
    // Example: Form submit animation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', () => {
            form.querySelector('button').disabled = true;
            form.querySelector('button').innerText = 'Submitting...';
        });
    });

    // Example: Smooth scroll to top
    const backToTopButton = document.createElement('button');
    backToTopButton.innerText = 'Back to Top';
    backToTopButton.className = 'btn';
    backToTopButton.style.position = 'fixed';
    backToTopButton.style.bottom = '1rem';
    backToTopButton.style.right = '1rem';
    backToTopButton.style.display = 'none';
    document.body.appendChild(backToTopButton);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
