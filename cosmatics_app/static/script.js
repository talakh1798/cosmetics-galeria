// function checkoutAlert() {
//     alert("Your order has been placed. Please pay when you receive your order.");
// }


// Using the sweetalert2 library

function checkoutAlert() {
    Swal.fire({
        title: 'Order Placed!',
        text: 'Your order has been placed. Please pay when you receive your order.',
        icon: 'success',
        confirmButtonText: 'OK'
    });
}

// Using vanilla JavaScript for about us

document.addEventListener('DOMContentLoaded', () => {
    const valuesList = document.querySelectorAll('.values li');
    const valueDetails = document.querySelectorAll('.value-detail');

    valuesList.forEach((value, index) => {
        value.addEventListener('click', () => {
            valueDetails.forEach(detail => detail.style.display = 'none');
            valueDetails[index].style.display = 'block';
        });
    });
});

function openLightbox(image, name) {
    document.getElementById('lightbox-img').src = `{% static 'img/' %}` + image;
    document.getElementById('lightbox-name').textContent = name;
    document.getElementById('lightbox').style.display = 'block';
}

function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
}
