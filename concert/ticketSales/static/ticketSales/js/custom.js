function addProductToOrder(concertId) {
    $.get('/order_module/add_to_order?concert_id=' + concertId +'&seat='+ 1 ) .then(res=>{
      
        Swal.fire({
            title: "Notification",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: res.confirm_button_text,
          }).then(confirm => {
            if(res.status==='not_auth'){
                window.location.href ='/accounts/login/';
            }
          
          });
    })
}

document.getElementById('contact-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  const form = this;
  const formData = new FormData(form);

  fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: {
          'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
      },
  })
  .then(response => response.json())
  .then(res => {
      Swal.fire({
          title: "Notification",
          text: res.text,
          icon: res.icon,
          confirmButtonColor: "#3085d6",
          confirmButtonText: res.confirm_button_text,
      });
      if (res.status === 'success') {
          form.reset(); // Reset form fields
      }
  })
  .catch(error => {
      Swal.fire({
          title: "Error",
          text: "Something went wrong. Please try again later.",
          icon: "error",
      });
  });
});

