// Cuando se termine de cargar la página web se cargarán todas las
// sentencias y funciones que se encuentran en el siguiente bloque
$(document).ready(function() {
	// Variables que verifican a cada campo si están validados o no
	var nuevapass_ok;
	var confirmpass_ok;

	$(".error").hide(); // Oculta los mensajes de error de cada campo

	// Función que valida el campo CONFIRMAR CONTRASEÑA
	function chkConfirmPass() {
		var validado = false;

		// Verifica que el campo no esté vacío
		if (chkIngresado("#confirmpass", "La confirmación de contraseña", "#error_confirmpass")) {
			if ($("#nuevapass").val() != $("#confirmpass").val()) {
				// En caso de que las contraseñas no sean iguales se despliega este mensaje
				$("#error_confirmpass").html("Las contraseñas deben ser iguales.")
				$("#error_confirmpass").show();
			} else {
				$("#error_confirmpass").hide();
				validado = true;
			}
		}

		return validado;
	}

	/* * * * Comienza la sección de los eventos * * * */
	// Evento cuando el campo NUEVA CONTRASEÑA pierde el enfoque y procede a ser evaluado
	$("#nuevapass").focusout(function() {
		nuevapass_ok = chkIngresado("#nuevapass", "Nueva contraseña", "#error_nuevapass");
	});

	// Evento cuando el campo CONFIRMAR CONTRASEÑA pierde el enfoque y procede a ser evaluado
	$("#confirmpass").focusout(function() {
		confirmpass_ok = chkConfirmPass();
	});

	// Evento para enviar datos del formulario
	$("#cambio-pass").submit(function() {
		nuevapass_ok = chkIngresado("#nuevapass", "Nueva contraseña", "#error_nuevapass");
		confirmpass_ok = chkConfirmPass();
		return nuevapass_ok && confirmpass_ok;
	});
	/* * * * Fin de la sección de los eventos * * * */
});
