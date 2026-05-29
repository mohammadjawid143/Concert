(function($) {
    "use strict";
    /*==================================================================
    [ Focus input ]*/
    $('.input100').each(function() {
        $(this).on('blur', function() {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    });


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function() {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function() {
        $(this).focus(function() {
            hideValidate(this);
        });
    });


    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    /*==================================================================
    [ Show pass ]*/
    var showPass = 0;
    $('.btn-show-pass').on('click', function() {
        if (showPass == 0) {
            $(this).next('input').attr('type', 'text');
            $(this).find('i').removeClass('zmdi-eye');
            $(this).find('i').addClass('zmdi-eye-off');
            showPass = 1;
        } else {
            $(this).next('input').attr('type', 'password');
            $(this).find('i').addClass('zmdi-eye');
            $(this).find('i').removeClass('zmdi-eye-off');
            showPass = 0;
        }

    });


})(jQuery);


const inputs = document.querySelectorAll('.input100');

inputs.forEach(input => {
    input.addEventListener('blur', function() {
        if (this.value.trim() !== "") {
            this.classList.add('has-val');
        } else {
            this.classList.remove('has-val');
        }
    });
});


function handle(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        document.getElementById('search').submit(); // Optionally submit the form manually
    }
};


const inputs1 = document.querySelectorAll('.wrap-register-input #id_name');
inputs.forEach(input1 => {
    input1.addEventListener('#id_name', function() {
        if (this.value.trim() !== '') {
            this.classList.add('has-val');
        } else {
            this.classList.remove('has-val');
        }
    });
});




const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');

togglePassword.addEventListener('click', () => {
    // Toggle the password visibility
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);

    // Toggle the eye icon class
    togglePassword.classList.toggle('zmdi-eye');
    togglePassword.classList.toggle('zmdi-eye-off');
});


function goToStep2() {
    document.getElementById("step1").style.display = "none";
    document.getElementById("step2").style.display = "block";
}

function skipProfile() {
    document.forms[0].submit();
}
