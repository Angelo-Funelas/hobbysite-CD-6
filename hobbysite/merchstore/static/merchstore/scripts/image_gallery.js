const imageGalleryImages = document.querySelectorAll('.product-gallery > div:nth-child(2) > div > img');
const imageGalleryMain = document.querySelector('.product-gallery > div:first-child');
imageGalleryImages.forEach((item, key) => {
    if (key == 0) item.parentElement.style.border = '3px solid var(--theme)';
    item.addEventListener('click', (e) => {
        imageGalleryImages.forEach((el) => {
            el.parentElement.style.border = 'none';
        })
        imageGalleryMain.querySelectorAll('img').forEach((image) => {
            image.src = e.target.src;
        })
        item.parentElement.style.border = '3px solid var(--theme)';
    })
});