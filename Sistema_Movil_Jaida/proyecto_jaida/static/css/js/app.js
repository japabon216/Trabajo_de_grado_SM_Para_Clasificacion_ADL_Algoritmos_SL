function mostrarConfirmacion() {
    // Mostrar el mensaje de carga
    var loadingMessage = document.getElementById('loading-message');
    loadingMessage.style.display = 'block';

    if (confirm("¿Deseas extraer las características?")) {
        // Si el usuario hace clic en "Sí"
        if (confirm("¿Deseas subir un archivo CSV?\n\nEl archivo debe tener las columnas Activity, X_Acc, Y_Acc, Z_Acc, X_Gyro, Y_Gyro, Z_Gyro para poder procesarse.")) {
            var input = document.createElement('input');
            input.type = 'file';
            input.accept = '.csv';
            input.onchange = function() {
                var file = input.files[0];
                if (file) {
                    var formData = new FormData();
                    formData.append('file', file);

                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/subir_archivo_csv', true);
                    xhr.onreadystatechange = function () {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            // Ocultar el mensaje de carga
                            loadingMessage.style.display = 'none';

                            alert(xhr.responseText); // Mostrar respuesta del servidor como pop-up
                        }
                    };
                    xhr.send(formData);
                }
            };
            input.click();
        }
    } else {
        // Si el usuario hace clic en "No, deseo continuar"
        alert("Vamos bien");
    }
}
