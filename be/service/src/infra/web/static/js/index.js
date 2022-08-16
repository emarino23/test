$(".validate").on("click", function () {
  var { valid, message } = validate()
  if (!valid) {
    Swal.fire({
      title: 'Error!',
      text: message,
      icon: 'error',
      showCancelButton: true,
      showConfirmButton: false,
    });
    return false;
  }
  else {
    Swal.fire({
      title: 'Muy Bien!',
      text: 'Deseas enviar la nueva contraseña?',
      icon: 'success',
      confirmButtonText: 'Sí',
      showCancelButton: true,
    }).then((result) => {
      if (result.value) {
        $("#form").submit();
      }
      return false;

    });
    return false;
  }
});

function validate() {
  var message = ""
  var valid = true
  var password = $("#password").val()
  var validators = [
    [!/\W/.test(password), "la contraseña debe tener una letra especial"],
    [!/[0-9]/.test(password), "la contraseña debe tener un número"],
    [!/[A-Z]/.test(password), "la contraseña debe tener una Mayuscula"],
    [!/[a-z]/.test(password), "la contraseña debe tener una minuscula"],
    [password.length < 8, "la contraseña debe tener un mínimo de 8 dígitos"],
    [password != $("#confirm").val(), "las contraseñas no coinciden"],
    [password == "", "la contraseña está vacia"]
  ]

  validators.map((validator) => {
    if (validator[0]) {
      valid = !validator[0]
      message = validator[1]
    }

  })


  return { valid, message };

}

$('input').attr('class', 'input');
