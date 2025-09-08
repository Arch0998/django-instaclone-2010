async function toggleLike(postId) {
    const btn = document.getElementById('like-btn');
    const icon = btn.querySelector('i');
    const likesCount = document.getElementById('likes-count');
    const countBadge = btn.querySelector('.count-badge');

    try {
        const response = await fetch(`/posts/${postId}/like/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
        });

        const data = await response.json();

        if (data.success) {
            if (data.is_liked) {
                btn.classList.add('liked');
                icon.className = 'fas fa-heart';
            } else {
                btn.classList.remove('liked');
                icon.className = 'far fa-heart';
            }

            if (data.likes_count > 0) {
                likesCount.innerHTML = `<i class="fas fa-heart likes-icon"></i> <span>${data.likes_count}</span> like${data.likes_count !== 1 ? 's' : ''}`;

                if (countBadge) {
                    countBadge.textContent = data.likes_count;
                } else {
                    const newCountBadge = document.createElement('span');
                    newCountBadge.className = 'count-badge';
                    newCountBadge.textContent = data.likes_count;
                    btn.appendChild(newCountBadge);
                }
            } else {
                likesCount.innerHTML = '<span class="likes-empty">Be the first to like this post</span>';
                if (countBadge) {
                    countBadge.remove();
                }
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function deleteComment(commentId) {
    if (!confirm('Are you sure you want to delete this comment?')) {
        return;
    }

    try {
        const response = await fetch(`/posts/comment/${commentId}/delete/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
        });

        const data = await response.json();

        if (data.success) {
            const commentElement = document.getElementById(`comment-${commentId}`);
            commentElement.remove();

            const commentsCount = document.getElementById('comments-count');
            const currentCount = parseInt(commentsCount.textContent.match(/\d+/)[0]);
            const newCount = currentCount - 1;
            commentsCount.textContent = `(${newCount})`;

            if (newCount === 0) {
                const commentsList = document.getElementById('comments-list');
                commentsList.innerHTML = `
                <div id="no-comments" class="no-comments">
                    <div class="no-comments-icon">
                        <i class="far fa-comment"></i>
                    </div>
                    <p class="no-comments-text">
                        No comments yet. Be the first to comment!
                    </p>
                </div>
            `;
            }
        } else {
            alert('Error deleting comment: ' + (data.error || 'Unknown error'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error deleting comment');
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const commentForm = document.getElementById('comment-form');
    if (commentForm) {
        commentForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const formData = new FormData(this);
            const textarea = this.querySelector('textarea');

            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    textarea.value = '';
                    location.reload();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    const captionElement = document.getElementById('post-caption');
    if (captionElement) {
        const captionText = captionElement.innerHTML;
        const processedText = captionText.replace(/(#\w+)/g, '<a href="/posts/hashtag/$1" style="text-decoration: none; color: var(--ig-link);">$1</a>');
        captionElement.innerHTML = processedText;
    }
});
