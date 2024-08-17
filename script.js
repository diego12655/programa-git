//document.addEventListener('DOMContentLoaded', (event) => {
// Datos de la aplicación
let proveedores = {};
let mensajes = [];
let inventario = {};
let usuarios = {
    "admin": {"contraseña": "0000"}
};

// Función para mostrar el panel de inicio de sesión
function showLoginPanel() {
    document.getElementById('login-panel').style.display = 'block';
    document.getElementById('app-panel').style.display = 'none';
    document.getElementById('registration-panel').style.display = 'none';
}

// Función para mostrar el panel de la aplicación
function showAppPanel() {
    document.getElementById('login-panel').style.display = 'none';
    document.getElementById('app-panel').style.display = 'block';
    document.getElementById('registration-panel').style.display = 'none';
}

// Función para mostrar el panel de registro
function showRegistrationPanel() {
    document.getElementById('login-panel').style.display = 'none';
    document.getElementById('app-panel').style.display = 'none';
    document.getElementById('registration-panel').style.display = 'block';
}


// Función para registrar un nuevo usuario
function registerUser() {
    const newEmail = document.getElementById('new-email').value;
    const newPassword = document.getElementById('new-password').value;

    if (newEmail && newPassword) {
        // Crear un objeto FormData para almacenar los datos del formulario
        let formData = new FormData();
        formData.append('new-email', newEmail);
        formData.append('new-password', newPassword);

        // Crear una nueva solicitud AJAX
        let xhr = new XMLHttpRequest();

        // Configurar la solicitud
        xhr.open('POST', 'index.php', true);

        // Establecer la función que se ejecutará cuando la solicitud se complete
        xhr.onload = function() {
            if (this.status == 200) {
                // La solicitud se completó con éxito, puedes procesar la respuesta aquí
                console.log(this.responseText);
                alert('Usuario registrado exitosamente. Ahora puedes iniciar sesión.');
                showLoginPanel(); // O cualquier otra acción que desees después del registro exitoso
            } else {
                // Hubo un error con la solicitud
                console.error('AJAX request failed with status ' + this.status);
            }
        };

        // Enviar la solicitud
        xhr.send(formData);
    } else {
        alert('Por favor complete todos los campos.');
    }
}


// Función para iniciar sesión
function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email && password) {
        if (usuarios[email] && usuarios[email]["contraseña"] === password) {
            alert('Inicio de sesión exitoso.');
            showAppPanel();
        } else {
            alert('Correo electrónico o contraseña incorrectos.');
        }
    } else {
        alert('Por favor complete todos los campos.');
    }
}

// Resto de las funciones...


// Función para mostrar el inventario
function showInventory() {
  let inventoryPanel = document.getElementById('inventory-panel');
  let inventoryList = document.createElement('ul');
  
  // Limpiar el contenido anterior
  inventoryPanel.innerHTML = '';

  // Iterar sobre el inventario y agregar cada producto a la lista
  for (let itemName in inventario) {
      let listItem = document.createElement('li');
      listItem.textContent = `${itemName}: ${inventario[itemName]}`;
      inventoryList.appendChild(listItem);
  }

  // Agregar la lista al panel de inventario y mostrarlo
  inventoryPanel.appendChild(inventoryList);
  inventoryPanel.style.display = 'block';
}



function showCreateProductDialog() {
  // Mostrar un cuadro de diálogo para ingresar el nombre del producto y la cantidad
  let productName = prompt("Ingrese el nombre del producto:");
  let quantity = prompt("Ingrese la cantidad:");

  // Verificar si se ingresaron datos válidos
  if (productName && quantity && !isNaN(parseInt(quantity))) {
      // Convertir la cantidad a un número entero
      quantity = parseInt(quantity);

      // Agregar el producto al inventario
      inventario[productName] = quantity;

      // Mostrar un mensaje de éxito
      alert(`Producto "${productName}" creado exitosamente con cantidad ${quantity}.`);
  } else {
      // Mostrar un mensaje de error si los datos no son válidos
      alert("Por favor ingrese un nombre de producto válido y una cantidad numérica.");
  }
}

// Función para cerrar el diálogo de inventario
function closeInventoryDialog() {
    document.getElementById('inventory-dialog').style.display = 'none';
}
//función para crear un producto

// Función para mostrar el diálogo de enviar mensaje
function showSendMessageDialog() {
  document.getElementById('send-message-dialog').style.display = 'block';
}

// Función para enviar un mensaje
function sendMessage() {
  const recipient = document.getElementById('recipient').value;
  const message = document.getElementById('message').value;

  if (recipient && message) {
      // Aquí puedes implementar el código para enviar el mensaje, como almacenarlo en una estructura de datos o enviarlo a través de una solicitud HTTP a un servidor
      alert(`Mensaje enviado a ${recipient}: ${message}`);
      // Cerrar el diálogo después de enviar el mensaje
      closeSendMessageDialog();
  } else {
      alert('Por favor complete todos los campos.');
  }
}

// Función para cerrar el diálogo de enviar mensaje
function closeSendMessageDialog() {
  document.getElementById('send-message-dialog').style.display = 'none';
}

// Función para mostrar el diálogo de añadir usuario
function showAddUserDialog() {
  document.getElementById('add-user-dialog').style.display = 'block';
}

// Función para agregar un nuevo usuario
function addUser() {
  const newUserEmail = document.getElementById('new-user-email').value;
  const newUserPassword = document.getElementById('new-user-password').value;

  if (newUserEmail && newUserPassword) {
      // Aquí puedes implementar la lógica para agregar el nuevo usuario a tu sistema
      alert('Usuario agregado exitosamente.');
      // Cerrar el diálogo después de agregar el usuario
      closeAddUserDialog();
  } else {
      alert('Por favor complete todos los campos.');
  }
}

// Función para cerrar el diálogo de añadir usuario
function closeAddUserDialog() {
  document.getElementById('add-user-dialog').style.display = 'none';
}

// Función para borrar un producto
function showDeleteProductDialog() {
  let productName = prompt("Ingrese el nombre del producto que desea borrar:");

  if (productName && inventario.hasOwnProperty(productName)) {
      delete inventario[productName];
      alert(`Producto "${productName}" borrado exitosamente.`);
  } else {
      alert("El producto no existe en el inventario.");
  }
}


// Función para mostrar el diálogo de añadir proveedor
function showAddProviderDialog() {
  document.getElementById('add-provider-dialog').style.display = 'block';
}

// Función para agregar un nuevo proveedor
function addProvider() {
  const providerName = document.getElementById('provider-name').value;
  const providerPhone = document.getElementById('provider-phone').value;

  if (providerName && providerPhone) {
      // Aquí puedes implementar la lógica para agregar el nuevo proveedor a tu sistema
      proveedores[providerName] = providerPhone; // Añadimos el proveedor al objeto proveedores
      alert('Proveedor agregado exitosamente.');
      // Cerrar el diálogo después de agregar el proveedor
      closeAddProviderDialog();
  } else {
      alert('Por favor complete todos los campos.');
  }
}

// Función para mostrar proveedores
function showProviders() {
  let providersList = "Proveedores:\n";

  // Verificar si hay proveedores
  if (Object.keys(proveedores).length === 0) {
      providersList += "No hay proveedores registrados.";
  } else {
      for (let provider in proveedores) {
          providersList += `Nombre: ${provider}, Teléfono: ${proveedores[provider]}\n`;
      }
  }

  // Mostrar la lista de proveedores
  alert(providersList);
}
// Función para cerrar la sesión
function logout() {
  // Aquí puedes implementar la lógica para borrar los datos de la sesión actual
  // Por ejemplo, podrías borrar el email del usuario actual de alguna variable global

  // Mostrar la pantalla de inicio de sesión
  showLoginPanel();
}
function sendMessage() {
  const message = document.getElementById('message').value;

  if (message) {
      // Aquí puedes implementar el código para enviar el mensaje, como almacenarlo en una estructura de datos o enviarlo a través de una solicitud HTTP a un servidor
      mensajes.push(message); // Añadimos el mensaje a la lista de mensajes
      alert(`Mensaje enviado: ${message}`);
      // Cerrar el diálogo después de enviar el mensaje
      closeSendMessageDialog();
  } else {
      alert('Por favor complete todos los campos.');
  }
}

// Función para mostrar los mensajes
function showMessages() {
  let messagesList = "Mensajes:\n";

  // Verificar si hay mensajes
  if (mensajes.length === 0) {
      messagesList += "No hay mensajes.";
  } else {
      for (let i = 0; i < mensajes.length; i++) {
          messagesList += `${i+1}. ${mensajes[i]}\n`;
      }
  }

  // Mostrar la lista de mensajes
  alert(messagesList);
}
//});