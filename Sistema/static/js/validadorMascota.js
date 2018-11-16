// Cuando se termine de cargar la página web se cargarán todas las
// sentencias y funciones que se encuentran en el siguiente bloque
$(document).ready(function() {
	// Variables que verifican a cada campo si están validados o no
	var nombre_ok;
	var raza_ok;
	var descripcion_ok;

	$(".error").hide(); // Oculta los mensajes de error de cada campo

	/* * * * Comienza la sección de los eventos * * * */
	// Evento cuando el campo NOMBRE pierde el enfoque y procede a ser evaluado
	$("#nombre").focusout(function() {
		nombre_ok = chkIngresado("#nombre", "Nombre", "#error_nombre");
	});

	// Evento cuando el campo RAZA pierde el enfoque y procede a ser evaluado
	$("#raza").focusout(function() {
		raza_ok = chkIngresado("#raza", "Raza dominante", "#error_raza");
	});

	// Evento cuando el campo DESCRIPCIÓN pierde el enfoque y procede a ser evaluado
	$("#descripcion").focusout(function() {
		descripcion_ok = chkIngresado("#descripcion", "Descripción", "#error_descripcion");
	});

	// Evento para enviar datos del formulario
	$("#reg-mascota").submit(function() {
		// Se llama a cada función para validar campos y se guarda el veredicto en cada
		// variable que representa a todos los campos que existen en el formulario
		nombre_ok = chkIngresado("#nombre", "Nombre", "#error_nombre");
		raza_ok = chkIngresado("#raza", "Raza dominante", "#error_raza");
		descripcion_ok = chkIngresado("#descripcion", "Descripción", "#error_desc");

		// Retorna verdadero si todos los campos están validados, de lo contrario no se procede el registro
		return nombre_ok && raza_ok && descripcion_ok;
	});
	/* * * * Fin de la sección de los eventos * * * */
});
