document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.toggle-status').forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.dataset.taskId;
            const isDone = this.classList.contains('btn-danger');

            fetch(`/tasks/${taskId}/update-status/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ is_done: !isDone })
            })
            .then(response => {
                if (response.ok) {
                    window.location.reload();
                } else {
                    console.error('Error updating task status');
                }
            })
            .catch(error => {
                console.error('Error updating task status:', error);
            });
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
