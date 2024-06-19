<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "prueba.users";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST['new-email']) && isset($_POST['new-password'])) {
        // Esto es un registro de usuario
        $email = $_POST['new-email'];
        $password = $_POST['new-password'];

        // Preparar la consulta SQL
        $sql = "INSERT INTO Users (email, password)
        VALUES ('$email', '$password')";

        // Ejecutar la consulta SQL
        if ($conn->query($sql) === TRUE) {
          echo "New record created successfully";
        } else {
          echo "Error: " . $sql . "<br>" . $conn->error;
        }
    } elseif (isset($_POST['email']) && isset($_POST['password'])) {
        // Esto es un inicio de sesión
        $email = $_POST['email'];
        $password = $_POST['password'];

        // Preparar la consulta SQL
        $sql = "SELECT * FROM Users WHERE email = '$email'";

        // Ejecutar la consulta SQL
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            // El usuario existe, verificar la contraseña
            $user = $result->fetch_assoc();
            if ($user['password'] === $password) {
                echo "Inicio de sesión exitoso";
            } else {
                echo "Contraseña incorrecta";
            }
        } else {
            echo "El usuario no existe";
        }
    }
}

// Cerrar la conexión
$conn->close();
?>



<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ACCUNTI</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
  <style>
    body {
        background-image: url('fondo1.jpg');
        background-repeat: no-repeat;
        background-size: cover;
    }
</style>

<div id="login-panel" class="panel">
  <h2>Iniciar Sesión</h2>
  <input type="text" id="email" placeholder="Correo electrónico">
  <input type="password" id="password" placeholder="Contraseña">
  <button onclick="login()">Ingresar</button>
  <button onclick="showRegistrationPanel()">Registrarse</button>
</div>

<div id="app-panel" class="panel" style="display: none;">
  <h2>Panel de Aplicación</h2>
  <button onclick="showInventory()">Inventario</button>
  <button onclick="showSendMessageDialog()">Enviar Mensaje</button>
  <button onclick="showAddUserDialog()">Añadir Usuario</button>
  <button onclick="showCreateProductDialog()">Crear Producto</button>
  <button onclick="showDeleteProductDialog()">Borrar Producto</button>
  <button onclick="showAddProviderDialog()">Añadir Proveedor</button>
  <button onclick="showProviders()">Ver Proveedores</button>
  <button onclick="showMessages()">Ver mensajes</button>
  <button onclick="logout()">Cerrar Sesión</button>
</div>

<div id="registration-panel" class="dialog" style="display: none;">
  <h2>Añadir Usuario</h2>
  <form method="post" action="">
    <input type="text" name="new-email" placeholder="Correo electrónico">
    <input type="password" name="new-password" placeholder="Contraseña">
    <input type="submit" value="Añadir">
  </form>
  <button onclick="closeAddUserDialog()">Cancelar</button>
</div>

<div id="send-message-dialog" class="dialog" style="display: none;">
  <h2>Enviar Mensaje</h2>
  <input type="text" id="recipient" placeholder="Destinatario">
  <textarea id="message" placeholder="Mensaje"></textarea>
  <button onclick="sendMessage()">Enviar</button>
  <button onclick="closeSendMessageDialog()">Cancelar</button>
</div>

<div id="add-user-dialog" class="dialog" style="display: none;">
  <h2>Añadir Usuario</h2>
  <input type="text" id="new-user-email" placeholder="Correo electrónico">
  <input type="password" id="new-user-password" placeholder="Contraseña">
  <button onclick="addUser()">Añadir</button>
  <button onclick="closeAddUserDialog()">Cancelar</button>
</div>

<div id="inventory-panel" class="panel hidden"></div>

<div id="add-provider-dialog" class="dialog" style="display: none;">
  <h2>Añadir Proveedor</h2>
  <input type="text" id="provider-name" placeholder="Nombre del proveedor">
  <input type="text" id="provider-phone" placeholder="Teléfono del proveedor">
  <button onclick="addProvider()">Añadir</button>
  <button onclick="closeAddProviderDialog()">Cancelar</button>
</div>

<script src="script.js"></script>
<a href="https://accunti1.000webhostapp.com/#">visita nuestra Página web</a>

</body>
</html>
