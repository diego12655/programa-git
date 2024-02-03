package controladores;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Recibedatos extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response, String msg)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>ACCUNTI</title>");
            out.println("<style>");
            out.println("body { background-color: #32CD32; color: #FFFFFF; }"); // CSS for green background and white text
            out.println(".logo { position: absolute; top: 0; right: 0; }"); // CSS for positioning the logo
            out.println("</style>");
            out.println("<script>");
            out.println("function myFunction() { alert('PARA CONTACTARNOS: CELULAR:3125320132"
                    + "EMAIL:diegov889@gmail.com'); }"); // A simple JavaScript function
            out.println("</script>");
            out.println("</head>");
            out.println("<body>");
            out.println("<img src='https://www.dropbox.com/scl/fi/voph3o0ck3bvlbeq06w9x/_d206fcbe-460b-49bc-ba9f-9fa060a8498e.jpg?rlkey=on63oi7ydqngxkaacdf3ez4jf&dl=0' class='logo'>"); // Include the logo
            out.println("<h1>BIENVENIDO A ACCUNTI " + msg + "</h1>");
            out.println("<h1>¿quienes somos?</h1>");
            out.println("<h1>Somos ACCUNTI, una empresa dedicada a proporcionar soluciones de gestión de inventarios eficientes y efectivas. Nuestra misión es ayudar a las empresas a optimizar sus operaciones de inventario, reducir costos y mejorar su eficiencia.\n" +
"\n" +
"<P>Nuestra Historia\n" +
"\n" +
"<P>Fundada en 2024, ACCUNTI comenzó con la visión de simplificar la gestión de inventarios. Nos dimos cuenta de que muchas empresas luchaban con el seguimiento de sus productos, la predicción de la demanda y la minimización de los costos de almacenamiento. Así que nos propusimos crear una solución que pudiera abordar estos desafíos.\n" +
"\n" +
"<P> Nuestro Equipo\n" +
"\n" +
"<P>Nuestro equipo está compuesto por profesionales experimentados en logística, cadena de suministro y tecnología de la información. Nos apasiona lo que hacemos y trabajamos incansablemente para proporcionar a nuestros clientes la mejor solución de gestión de inventarios del mercado.\n" +
"\n" +
"<P>Nuestros Valores\n" +
"\n" +
"<P>Creemos en la innovación constante, la integridad y el servicio al cliente excepcional. Estos valores son la base de nuestra empresa y guían todo lo que hacemos.\n" +
"\n" +
"<P> Nuestro Compromiso\n" +
"<P> MISION\n"+
"<P> Nuestra misión en ACCUNTI es proporcionar soluciones de gestión de inventarios de alta calidad que permitan a las empresas optimizar sus operaciones, reducir costos y mejorar la eficiencia. Nos esforzamos por ofrecer un servicio excepcional a nuestros clientes, ayudándoles a tomar el control de su inventario y a hacer crecer su negocio.\n"+            
"\n" +
"<P> VISION\n"+
"<P> Nuestra visión es ser líderes en el campo de la gestión de inventarios, reconocidos por nuestra innovación, integridad y compromiso con la excelencia del servicio al cliente. Aspiramos a transformar la forma en que las empresas gestionan su inventario, haciendo que el proceso sea más eficiente, rentable y sostenible.\n"+
                    
"<P>Nos comprometemos a proporcionar a nuestros clientes una solución de gestión de inventarios que sea fácil de usar, flexible y potente. Estamos aquí para ayudarte a tomar el control de tu inventario y a hacer crecer tu negocio.");
            out.println(new String (".").toUpperCase());
            out.println("</h1>");
            out.println("la suma de los numero 15+1 es:"+(15+1));
            out.println("Si 12 es mayor que 18 : "+(12>18));
            out.println("<h1>");
            for(int i=0;i<10; i++){
                out.print("<br>Tipos scriplets"+i);            
            }
            out.println("</h1>");
            out.println("<h1>");
            int total;
            out.println("el resultado de la suma es: "+ metodosuma(10,8));
            out.println("</h1>");
            out.println("<button onclick='myFunction()'>CONTACTENOS</button>"); // Button to trigger the JavaScript function
            out.println("</body>");
            out.println("</html>");
        }
    }

    private int metodosuma(int a, int b){
        return a+b;
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String user=request.getParameter("usuario");
        String pass=request.getParameter("clave");
        if("admin".equals(user)&& "1234".equals(pass)){
             processRequest(request, response, "registro exitoso");
        }else{
             processRequest(request, response, "registro invalido");
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String user=request.getParameter("usuario");
        String pass=request.getParameter("clave");
        if("admin".equals(user)&& "1234".equals(pass)){
             processRequest(request, response, "registro exitoso");
        }else{
             processRequest(request, response, "registro invalido");
        }
    }

    @Override
    public String getServletInfo() {
        return "Short description";
    }
}
