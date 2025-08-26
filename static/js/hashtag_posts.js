document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.post-card').forEach(card => {
        card.addEventListener('click', function() {
            console.log('Post clicked:', this.getAttribute('onclick'));
        });
    });

    document.querySelectorAll('.pagination-link').forEach(link => {
        link.addEventListener('click', function() {
            setTimeout(() => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }, 100);
        });
    });
});
