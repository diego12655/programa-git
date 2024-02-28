<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $servername = "localhost";
    $username = "username";
    $password = "password";
    $dbname = "myDB";

    // Crear conexión
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar conexión
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }

    // Recoger los datos del formulario
    $email = $_POST['new-email'];
    $new_password = $_POST['new-password'];

    // Preparar la consulta SQL
    $stmt = $conn->prepare("INSERT INTO Users (email, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $email, $new_password);

    // Ejecutar la consulta SQL
    if ($stmt->execute()) {
      echo "New record created successfully";
    } else {
      echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Cerrar la conexión
    $stmt->close();
    $conn->close();
}
?>
