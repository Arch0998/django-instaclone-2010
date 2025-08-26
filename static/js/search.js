let searchTimeout;

function searchUsers(query) {
    clearTimeout(searchTimeout);
    const resultsDiv = document.getElementById('search-results');

    if (query.length < 2) {
        resultsDiv.style.display = 'none';
        return;
    }

    searchTimeout = setTimeout(async () => {
        try {
            const response = await fetch(`/posts/search-users/?q=${encodeURIComponent(query)}`);
            const data = await response.json();

            if (data.users.length > 0) {
                resultsDiv.innerHTML = data.users.map(user => `
                <div class="search-result-item" onclick="window.location.href='${user.profile_url}'">
                    ${user.avatar ?
                    `<img src="${user.avatar}" alt="${user.username}" class="search-result-avatar">` :
                    `<div class="search-result-avatar-placeholder"><i class="fas fa-user fa-sm"></i></div>`
                }
                    <div class="search-result-info">
                        <div class="search-result-username">${user.username}</div>
                        <div class="search-result-name">${user.first_name} ${user.last_name}</div>
                    </div>
                </div>
            `).join('');
                resultsDiv.style.display = 'block';
            } else {
                resultsDiv.innerHTML = `<div class="search-no-results">No users found</div>`;
                resultsDiv.style.display = 'block';
            }
        } catch (error) {
            console.error('Search error:', error);
            resultsDiv.style.display = 'none';
        }
    }, 300);
}

document.addEventListener('click', function (e) {
    const searchInput = document.getElementById('search-input');
    const resultsDiv = document.getElementById('search-results');

    if (searchInput && resultsDiv && !searchInput.contains(e.target) && !resultsDiv.contains(e.target)) {
        resultsDiv.style.display = 'none';
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('focus', function () {
            if (this.value.length >= 2) {
                const resultsDiv = document.getElementById('search-results');
                if (resultsDiv.innerHTML.trim() !== '') {
                    resultsDiv.style.display = 'block';
                }
            }
        });
    }
});
