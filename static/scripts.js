document.addEventListener('DOMContentLoaded', function() {
    console.log('Laxnode Solutions website loaded');

    const links = document.querySelectorAll('nav ul li a');
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
            fetchSection(sectionId);
        });
    });

    function fetchSection(sectionId) {
        fetch(`/${sectionId}`)
            .then(response => response.text())
            .then(html => {
                document.querySelector('main').innerHTML = html;
            })
            .catch(error => console.error('Error loading section:', error));
    }
});
