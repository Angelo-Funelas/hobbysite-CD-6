const imageInput = document.querySelector('input[type=file]');
const imgDisplayContainer = document.querySelector('.profile-container > div > div');
imgDisplayContainer.addEventListener('click', () => {
    imageInput.click();
})
imageInput.addEventListener('change', (e) => {
    var files = e.target.files;
    var done = function (url) {
        imgDisplayContainer.querySelector('img:first-child').src = url;
    }
    if (files && files.length > 0) {
        file = files[0];
    }
    if (URL) {
        done(URL.createObjectURL(file));
    } else if (FileReader) {
        reader = new FileReader();
        reader.onload = function (e) {
            done(reader.result);
        };
        reader.readAsDataURL(file);
    }
})