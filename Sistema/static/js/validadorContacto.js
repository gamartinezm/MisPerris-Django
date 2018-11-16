// Cuando se termine de cargar la página web se cargarán todas las
// sentencias y funciones que se encuentran en el siguiente bloque
$(document).ready(function() {
	// Variables que verifican a cada campo si están validados o no
	var nombre_ok;
	var correo_ok;
	var mensaje_ok;

	$(".error").hide(); // Oculta los mensajes de error de cada campo

	/* * * * Comienza la sección de los eventos * * * */
	// Evento cuando el campo NOMBRE pierde el enfoque y procede a ser evaluado
	$("#nombre").focusout(function() {
		nombre_ok = chkIngresado("#nombre", "Nombre", "#error_nombre");
	});

	// Evento cuando el campo CORREO ELECTRÓNICO pierde el enfoque y procede a ser evaluado
	$("#correo").focusout(function() {
		correo_ok = chkCorreo();
	});

	// Evento cuando el campo MENSAJE pierde el enfoque y procede a ser evaluado
	$("#mensaje").focusout(function() {
		mensaje_ok = chkIngresado("#mensaje", "Mensaje", "#error_mensaje");
	});

	// Evento para enviar el mensaje de contacto
	$("#contacto").submit(function() {
		// Se llama a cada función para validar campos y se guarda el veredicto en cada
		// variable que representa a todos los campos que existen en el formulario
		nombre_ok = chkIngresado("#nombre", "Nombre", "#error_nombre");
		correo_ok = chkCorreo();
		mensaje_ok = chkIngresado("#mensaje", "Mensaje", "#error_mensaje");

		// Retorna verdadero si todos los campos están validados, de lo contrario no se procede el envío del mensaje de contacto
		return nombre_ok && correo_ok && mensaje_ok;
	});
	/* * * * Fin de la sección de los eventos * * * */
});
