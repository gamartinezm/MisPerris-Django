// Cuando se termine de cargar la página web se cargarán todas las
// sentencias y funciones que se encuentran en el siguiente bloque
$(document).ready(function() {
	// Variables que verifican a cada campo si están validados o no
	var username_ok;
	var password_ok;

	$(".error").hide(); // Oculta los mensajes de error de cada campo

	/* * * * Comienza la sección de los eventos * * * */
	// Evento cuando el campo NOMBRE DE USUARIO pierde el enfoque y procede a ser evaluado
	$("#username").focusout(function() {
		username_ok = chkIngresado("#username", "Nombre de usuario", "#error_username");
	});

	// Evento cuando el campo CONTRASEÑA pierde el enfoque y procede a ser evaluado
	$("#password").focusout(function() {
		password_ok = chkIngresado("#password", "Contraseña", "#error_password");
	});

	// Evento para autenticar el usuario ingresado
	$("#login").submit(function() {
		// Se llama a cada función para validar campos y se guarda el veredicto en cada
		// variable que representa a todos los campos que existen en el formulario
		username_ok = chkIngresado("#username", "Nombre de usuario", "#error_username");
		password_ok = chkIngresado("#password", "Contraseña", "#error_password");

		// Retorna verdadero si todos los campos están validados, de lo contrario no se procede el inicio de sesión
		return username_ok && password_ok;
	});
	/* * * * Fin de la sección de los eventos * * * */
});
