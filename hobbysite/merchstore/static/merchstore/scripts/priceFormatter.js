var prices = document.querySelectorAll('.price')
for (var price of prices) {
    price.innerText = price.innerText.replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}