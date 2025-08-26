document.addEventListener('DOMContentLoaded', function() {
    const followButtons = document.querySelectorAll('.follow-btn');

    followButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const username = this.dataset.username;
            const btn = this;

            fetch(`/user/${username}/follow/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (data.is_following) {
                        btn.textContent = 'Unfollow';
                        btn.className = 'btn btn-sm btn-outline-danger follow-btn';
                        btn.dataset.following = 'true';
                    } else {
                        btn.textContent = 'Follow';
                        btn.className = 'btn btn-sm btn-primary follow-btn';
                        btn.dataset.following = 'false';
                    }
                } else {
                    console.error('Error:', data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});