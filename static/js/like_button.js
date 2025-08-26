document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            const icon = this.querySelector('i');
            const countBadge = this.querySelector('.count-badge');

            fetch(`/posts/${postId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (data.is_liked) {
                        icon.className = 'fas fa-heart';
                        this.classList.add('liked');
                    } else {
                        icon.className = 'far fa-heart';
                        this.classList.remove('liked');
                    }

                    if (countBadge && data.likes_count !== undefined) {
                        if (data.likes_count > 0) {
                            countBadge.textContent = data.likes_count;
                            countBadge.style.display = 'inline-block';
                        } else {
                            countBadge.style.display = 'none';
                        }
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
