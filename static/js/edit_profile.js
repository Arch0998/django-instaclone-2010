function previewAvatar(input) {
    const preview = document.getElementById('avatar-preview');
    const previewImg = document.getElementById('preview-avatar');

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            previewImg.src = e.target.result;
            preview.style.display = 'block';
        }

        reader.readAsDataURL(input.files[0]);
    } else {
        preview.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const preview = document.getElementById('avatar-preview');
    if (preview) {
        preview.style.display = 'none';
    }
});
