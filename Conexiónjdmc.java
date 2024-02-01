package conexiónjdmc;

import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Conexiónjdmc {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String usuario="root";
        String password="";
        String url="jdbc:mysql://localhost:3306/prueba"; // Asegúrate de que 'prueba' es el nombre de tu base de datos
        Connection conexion;
        Statement statement;
        ResultSet rs;
        
        try {
            // TODO code application logic here
            Class.forName("com.mysql.cj.jdbc.Driver");
            
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Conexiónjdmc.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            conexion = DriverManager.getConnection(url, usuario, password);
            statement = conexion.createStatement();

            // Crear (Create)
            statement.executeUpdate("INSERT INTO USUARIO(USERNAME, USERPASSWORD, NAME, PASSWORD) VALUES('ABC', '123', 'DEF', 'XYZ')");

            // Leer (Read)
            rs=statement.executeQuery("SELECT  * FROM USUARIO");
            while(rs.next()){
                System.out.println(rs.getString("USERNAME")+" : "+rs.getString("USERPASSWORD")+" : "+rs.getString("NAME")+" : "+rs.getString("PASSWORD"));
            }

            // Actualizar (Update)
            statement.executeUpdate("UPDATE USUARIO SET PASSWORD='XYZ123' WHERE USERNAME='ABC'");

            // Eliminar (Delete)
            statement.executeUpdate("DELETE FROM USUARIO WHERE USERNAME='ABC'");

        } catch (SQLException ex) {
            Logger.getLogger(Conexiónjdmc.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
}

