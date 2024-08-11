
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

    // Add event listeners to open lightbox on image click
    const images = document.querySelectorAll('.image');
    images.forEach(image => {
        image.addEventListener('click', () => {
            const imageName = image.getAttribute('data-image-name');
            const imageUrl = image.getAttribute('data-image-url');

            // Make an AJAX request to retrieve image data
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/get_image_data/${imageName}`, true);
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const imageData = JSON.parse(xhr.responseText);
                    openLightbox(imageUrl, imageData.name);
                }
            };
            xhr.send();
        });
    });

    // Add event listener to close lightbox
    document.getElementById('lightbox-close').addEventListener('click', closeLightbox);
});

function openLightbox(image, name) {
    document.getElementById('lightbox-img').src = `{% static 'img/' %}` + image;
    document.getElementById('lightbox-name').textContent = name;
    document.getElementById('lightbox').style.display = 'block';
}

function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
}
