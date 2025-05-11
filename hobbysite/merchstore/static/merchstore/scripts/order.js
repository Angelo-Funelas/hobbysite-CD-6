const orderForm = document.querySelector('form');
const orderButtons = document.querySelectorAll('.purchase-buttons > button')
orderButtons.forEach((item) => {
    item.addEventListener('click', () => {
        orderForm.querySelector('#order-status').value = item.dataset.status;
        orderForm.submit();
    })
})