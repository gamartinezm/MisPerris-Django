// Cuando se termine de cargar la página web se cargarán todas las
// sentencias y funciones que se encuentran en el siguiente bloque
$(document).ready(function() {
	// Variables que verifican a cada campo si están validados o no
	var run_ok;
	var nombres_ok;
	var appat_ok;
	var apmat_ok;
	var fecnac_ok;
	var correo_ok;
	var tel_ok;

	$(".error").hide(); // Oculta los mensajes de error de cada campo

	// Función que cumple un algoritmo que autentica 
	function validaRun(run) {
		// Variables que se utilizarán para la validación del RUN
		var dvRun = run.substring(run.indexOf('-') + 1);
		var aux = Number(run.substring(0, run.indexOf('-')));

		// Variables que se utilizarán para el cálculo
		var serie = 2;
		var calculo = 0;
		var dvRunCalculado;

		// Operación
		while (aux != 0) {
			if (serie > 7) {
				serie = 2;
			}
			calculo += aux % 10 * serie;
			aux = Math.trunc(aux / 10);
			serie++;
		}

		calculo = 11 - (calculo % 11);

		// Evalúa el cálculo final para determinar el dígito verificador
		switch (calculo) {
			case 10:
				dvRunCalculado = 'K';
				break;
			case 11:
				dvRunCalculado = '0';
				break;
			default:
				dvRunCalculado = calculo.toString();
		}

		// Retorna un valor booleano si el dígito verificador ingresado es igual al que se ha calculado
		return (dvRun == dvRunCalculado);
	}

	/* * * * Comienza sección de funciones de validación * * * */
	// Función que valida el campo RUN
	function chkRun() {
		var pattern = new RegExp(/^[0-9]{7,8}-[0-9k]$/i); // Expresión regular que contiene el formato del RUN
		var run = $("#run").val(); // Obtiene el valor del campo RUN
		var validado = false;

		// Verifica que el campo no esté vacío
		if (chkIngresado("#run", "RUN", "#error_run")) {
			if ((run.length >= 9 && run.length <= 10) && !pattern.test(run)) {
				// En caso de que el RUN no tenga un largo de 9 o 10 caracteres y que no cumpla con el
				// patrón de expresión regular se despliega este mensaje
				$("#error_run").html("El formato del RUN que ingresó no es válido.");
				$("#error_run").show();
			} else if (!validaRun(run)) {
				// En caso de que el RUN no sea válido se despliega este mensaje
				$("#error_run").html("El RUN que ingresó no es válido.");
				$("#error_run").show();
			} else {
				// De lo contrario el valor del campo está validado
				$("#error_run").hide();
				validado = true;
			}
		}

		return validado;
	}

	// Función que valida cada parte del nombre completo del adoptante
	function chkNombres(elemento, nombre, error) {
		var pattern = new RegExp(/^[a-z\s]+$/i); // Expresión regular que permitirá sólo letras
		var nombres = $(elemento).val(); // Obtiene el valor del campo de cada parte del nombre completo
		var validado = false;

		// Verifica que el campo no esté vacío
		if (chkIngresado(elemento, nombre, error)) {
			if (!pattern.test(nombres)) {
				// En caso de que el campo tenga caracteres que no sean letras se despliega este mensaje
				$(error).html("El campo " + nombre + " sólo acepta letras.");
				$(error).show();
			} else {
				// De lo contrario el valor del campo está validado
				$(error).hide();
				validado = true;
			}
		}

		return validado;
	}

	// Función que valida el campo FECHA DE NACIMIENTO
	function chkFecNac() {
		var hoyFull = new Date(); // Obtiene la fecha completa de hoy
		var hoyShort = new Date(hoyFull.getFullYear(), hoyFull.getMonth(), hoyFull.getDate()); // Se instancia la fecha de hoy pero solo día, mes y año
		var edad;
		var validado = false;

		// Verifica que el campo no esté vacío
		if (chkIngresado("#fecnac", "Fecha de nacimiento", "#error_fecnac")) {
			// Si se ha establecido una fecha se ejecuta estas instrucciones
			edad = Math.trunc((hoyShort - new Date($("#fecnac").val())) / 31557600000); // Diferencia entre la fecha de nacimiento y la de hoy para obtener la edad
			if (edad < 18) {
				// En caso de que la edad sea menor a 18 años se despliega este mensaje
				$("#error_fecnac").html("Debe tener como mínimo 18 años.");
				$("#error_fecnac").show();
			} else {
				// De lo contrario el valor del campo está validado
				$("#error_fecnac").hide();
				validado = true;
			}
		}

		return validado;
	}

	// Función que valida el campo TELÉFONO
	function chkTelefono() {
		var pattern = new RegExp(/(^[0-9]+$)/); // Expresión regular que contiene sólo números
		var telefono = $("#telefono").val(); // Obtiene el valor del campo TELÉFONO
		var validado = true;

		if (chkIngresado("#telefono", "Telefono", "#error_telefono")) {
			// En caso de que el campo tenga valor se procede a ser evaluado
			if (!pattern.test(telefono)) {
				// En caso de que el valor tenga caracteres que no sean números se despliega este mensaje
				$("#error_telefono").html("El campo teléfono sólo admite números.");
				$("#error_telefono").show();
				validado = false;
			} else {
				// De lo contrario el valor del campo está validado
				$("#error_telefono").hide();
			}
		} else {
			// Aunque esté vacío se valida ya que el campo es opcional
			$("#error_telefono").hide();
		}
		
		return validado;
	}
	/* * * * Fin de la sección de funciones de validación * * * */

	/* * * * Comienza la sección de los eventos * * * */
	// Evento cuando el campo RUN pierde el enfoque y procede a ser evaluado
	$("#run").focusout(function() {
		run_ok = chkRun(); // Se evalúa el campo
	});

	// Evento cuando el campo NOMBRES pierde el enfoque y procede a ser evaluado
	$("#nombres").focusout(function() {
		nombres_ok = chkNombres("#nombres", "Nombres", "#error_nombres");
	});

	// Evento cuando el campo APELLIDO PATERNO pierde el enfoque y procede a ser evaluado
	$("#appaterno").focusout(function() {
		appat_ok = chkNombres("#appaterno", "Apellido paterno", "#error_appaterno");
	});
	// Evento cuando el campo APELLIDO PATERNO pierde el enfoque y procede a ser evaluado
	$("#apmaterno").focusout(function() {
		apmat_ok = chkNombres("#apmaterno", "Apellido materno", "#error_apmaterno");
	});

	// Evento cuando el campo FECHA DE NACIMIENTO pierde el enfoque y procede a ser evaluado
	$("#fecnac").focusout(function() {
		fecnac_ok = chkFecNac(); // Se evalúa el campo
	});

	// Evento cuando el campo CORREO ELECTRÓNICO pierde el enfoque y procede a ser evaluado
	$("#correo").focusout(function() {
		correo_ok = chkCorreo(); // Se evalúa el campo
	});

	// Evento cuando el campo TELÉFONO pierde el enfoque y procede a ser evaluado
	$("#telefono").focusout(function() {
		tel_ok = chkTelefono(); // Se evalúa el campo
	});

	// Evento para cada cambio de valor en el campo REGIÓN
	/*$("#region").change(function() {
		var region = $(this).val(); // Obtiene el valor seleccionado en el campo REGIÓN
		if (region == "none") {
			// En caso de que no esté seleccionada una región se mostrarán todas las ciudades de
			// todas las regiones existentes
			$(".region").show();
		} else {
			// Si se haya seleccionado una región se mostrará las ciudades de la respectiva misma
			$(".region").not("." + region).hide(); // Todos los que no sean de la región seleccionada se ocultarán
			$(".region").filter("." + region).show(); // Se mostrarán las ciudades de la región seleccionada
		}
	});*/

	// Evento para enviar datos del formulario
	$("#reg-adoptante").submit(function() {
		// Se llama a cada función para validar campos y se guarda el veredicto en cada
		// variable que representa a todos los campos que existen en el formulario
		run_ok = chkRun();
		nombres_ok = chkNombres("#nombres", "Nombres", "#error_nombres");
		appat_ok = chkNombres("#appaterno", "Apellido paterno", "#error_appaterno");
		apmat_ok = chkNombres("#apmaterno", "Apellido materno", "#error_apmaterno");
		fecnac_ok = chkFecNac();
		correo_ok = chkCorreo();
		tel_ok = chkTelefono();

		// Retorna verdadero si todos los campos están validados, de lo contrario no se procede el registro
		return run_ok && nombres_ok && appat_ok && apmat_ok && fecnac_ok && correo_ok && tel_ok;
	});
	/* * * * Fin de la sección de los eventos * * * */
});
