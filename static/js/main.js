// main.js — students will add JavaScript here as features are built

// Video Modal Functionality
(function() {
    const modal = document.getElementById('video-modal');
    const openBtn = document.getElementById('how-it-works-btn');
    const closeBtn = document.getElementById('modal-close');
    const iframe = document.getElementById('youtube-frame');

    if (!modal || !openBtn) return;

    const videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ';

    openBtn.addEventListener('click', function() {
        iframe.src = videoUrl + '?autoplay=1';
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    });

    function closeModal() {
        modal.classList.remove('active');
        iframe.src = '';
        document.body.style.overflow = '';
    }

    closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModal();
        }
    });

    modal.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeModal();
        }
    });
})();
