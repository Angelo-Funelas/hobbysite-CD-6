window.addEventListener('load', () => {
    document.getElementById('loader-container').style.display = 'none';
})
window.addEventListener('beforeunload', function () {
    document.getElementById('loader-container').style.display = '';
});
window.addEventListener('pageshow', (e) => {
    if (e.persisted) {
        const loader = document.getElementById('loader-container');
        if (loader) loader.style.display = 'none';
    }
});
const loader = document.getElementById('loader-container');
if (loader) loader.style.display = 'none';