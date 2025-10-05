document.addEventListener('DOMContentLoaded', function () {
    var addToCartButtons = document.querySelectorAll('.add-to-cart');
    var cartItems = document.getElementById('cart-items');

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var itemName = this.parentElement.querySelector('.item-name').textContent;
            var listItem = document.createElement('li');
            listItem.textContent = itemName;
            cartItems.appendChild(listItem);
        });
    });
});