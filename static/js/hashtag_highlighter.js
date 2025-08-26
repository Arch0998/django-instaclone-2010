function highlightHashtags(textarea) {
    const text = textarea.value;
    const hashtags = text.match(/#\w+/g) || [];
    const hashtagPreview = document.getElementById('hashtag-preview');
    const hashtagsContainer = document.getElementById('hashtags-container');

    if (hashtags.length > 0) {
        hashtagPreview.style.display = 'block';
        hashtagsContainer.innerHTML = '';

        const uniqueHashtags = [...new Set(hashtags)];

        uniqueHashtags.forEach(hashtag => {
            const tag = document.createElement('span');
            tag.textContent = hashtag;
            tag.className = 'hashtag-tag';
            hashtagsContainer.appendChild(tag);
        });
    } else {
        hashtagPreview.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('textarea');
    if (textarea && textarea.value) {
        highlightHashtags(textarea);
    }
});
