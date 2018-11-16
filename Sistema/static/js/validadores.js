// Función que valida si cada campo que se pase como parámetro esté vacío
function chkIngresado(elemento, nombre, error) {
	var validado = false;

	if ($(elemento).val() == "") {
		// En caso de que el campo esté vacío se despliega este mensaje
		$(error).html("Debe ingresar " + nombre);
		$(error).show();
	} else {
		// De lo contrario el valor del campo está validado
		$(error).hide();
		validado = true;
	}

	return validado;
}

// Función que valida el campo CORREO ELECTRÓNICO
function chkCorreo() {
	var pattern = new RegExp(/^[+a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,4}$/i); // Expresión regular que contiene el formato del CORREO ELECTRÓNICO
	var validado = false;

	// Verifica que el campo no esté vacío
	if (chkIngresado("#correo", "Correo Electrónico", "#error_correo")) {
		if (!pattern.test($("#correo").val())) {
			// En caso de que el valor ingresado no cumpla con la expresión regular establecida se despliega este mensaje
			$("#error_correo").html("El formato del correo que ingresó no es válido.");
			$("#error_correo").show();
		} else {
			// De lo contrario el valor del campo está validado
			$("#error_correo").hide();
			validado = true;
		}
	}

	return validado;
}
