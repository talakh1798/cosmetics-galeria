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
