async function toggleFollow(username) {
    const btn = document.getElementById('follow-btn');
    const icon = btn.querySelector('i');
    const text = btn.querySelector('span');

    try {
        const response = await fetch(`/user/${username}/follow/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
        });

        const data = await response.json();

        if (data.success) {
            if (data.is_following) {
                btn.className = 'follow-btn btn-outline-gradient';
                icon.className = 'fas fa-user-check';
                text.textContent = 'Unfollow';
            } else {
                btn.className = 'follow-btn btn-gradient';
                icon.className = 'fas fa-user-plus';
                text.textContent = 'Follow';
            }

            const followersCount = document.querySelector('.stat-item:first-child .stat-number');
            if (followersCount) {
                followersCount.textContent = data.followers_count;
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.stat-item').forEach(item => {
        item.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 15px rgba(0,0,0,0.1)';
        });

        item.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'none';
        });
    });
});
