// Cuando se termine de cargar la página web se cargarán todas las
// sentencias y funciones que se encuentran en el siguiente bloque
$(document).ready(function() {
	// Variable que verifica al campo correo si está correcto o no
	var correo_ok;

	/* * * * Comienza la sección de los eventos * * * */
	// Evento cuando el campo CORREO ELECTRÓNICO pierde el enfoque y procede a ser evaluado
	$("#correo").focusout(function() {
		correo_ok = chkCorreo();
	});

	// Evento para enviar datos del formulario
	$("recuperar-pass").submit(function() {
		correo_ok = chkCorreo();
		return correo_ok;
	});
	/* * * * Fin de la sección de los eventos * * * */
});
