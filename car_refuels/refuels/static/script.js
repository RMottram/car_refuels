$(document).ready(function() {
    $('.delete-refuel').click(function() {
        var refuelId = $(this).data('refuel-id');
        var csrfToken = $(this).data('csrf-token');
        if (confirm('Are you sure you want to delete this refuel session?')) {
            $.ajax({
                url: window.location.pathname + refuelId + '/',  // Include refuel ID in URL
                type: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                success: function(result) {
                    window.location.reload();
                }
            });
        }
    });
});