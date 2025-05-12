const editForm = document.querySelector('form');
const addImageButton = document.getElementById('add-image-button');
const imageGallery = document.querySelector('.product-gallery > div:nth-child(2)');
let fileInputCount = 1
addImageButton.addEventListener('click', () => {
    const imageInput = document.querySelector('.image-inputs > input[type=file]:last-child');
    imageInput.click();
    imageInput.addEventListener('change', (e) => {
        var files = e.target.files;
        var done = function (url) {
            let newImageCont = document.createElement('div');
            let deleteIcon = document.createElement('img');
            deleteIcon.src = '/static/merchstore/icons/delete.svg'
            deleteIcon.addEventListener('click', (ev) => {
                document.getElementById(ev.target.dataset.fileInputId).remove();
                ev.target.parentElement.remove();
            })
            deleteIcon.dataset.fileInputId = `image-${fileInputCount}`;
            let newImage = document.createElement('img');
            newImage.src = url;
            let newImageInput = document.createElement('input');
            newImageInput.type = 'file';
            newImageInput.accept = 'image/*';
            newImageInput.hidden = true;
            fileInputCount++;
            newImageInput.id = `image-${fileInputCount}`;
            newImageCont.append(newImage, deleteIcon);
            imageGallery.append(newImageCont);
            document.querySelector('.image-inputs').append(newImageInput)
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
    }, { once: true })
})
editForm.addEventListener('submit', (e) => {
    e.preventDefault();
    nameFileInputs();
    const formData = new FormData(editForm);
    console.log(formData)
    editForm.submit();
})
function nameFileInputs() {
    const fileInputs = document.querySelectorAll('.image-inputs > input[type=file]');
    fileInputs.forEach((item, key) => {
        if (key < fileInputs.length-1) {
            item.name = `image-${1+key}`
        } else {
            item.remove();
        };
    })
    document.getElementById('image-count').value = fileInputs.length-1;
}
function setupImageObjDelete() {
    const imageObjs = document.querySelectorAll('.product-gallery > div > div > img:nth-child(2)');
    imageObjs.forEach((item) => {
        item.addEventListener('click', (e) => {
            document.getElementById('images-to-delete').value += `${e.target.dataset.obj_id} `;
            e.target.parentElement.remove();
        })
    })
}
setupImageObjDelete();