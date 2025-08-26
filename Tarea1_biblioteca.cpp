#include <iostream>
#include <string>
#include <vector>

class Biblioteca { 
public:
    class Libro {
    public:
        std::string titulo;
        std::string autor;
        int anioPublicacion;
        bool disponible = true; //variable que cambiará dependiendo el estado de los libros, true es que esta disponible, y false que no

        void mostrarDetallesCompletos() { 
            std::cout << "---------" << std::endl;
            std::cout << "Titulo: " << titulo << std::endl;
            std::cout << "Autor : " << autor << std::endl;
            std::cout << "Año de Publicación: " << anioPublicacion << std::endl;
            if (disponible){ //Si disponible esta en true
                std::cout << "Disponible : si" << std::endl;
            } else { //Si disponible esta en false
                std::cout << "Disponible : No" << std::endl; 
            }
        }
    
        void prestarLibro() {
            if (disponible) { //Si disponible esta en su valor inicial ( true ) 
                disponible = false;  // aqui cambia a false, ya no se podrá prestar 
                std::cout << "el libro ha sido prestado" << std::endl;
            } else {
                std::cout << "el libro no esta disponible" << std::endl; 
            }  
        }
        void devolverLibro() { //Funcion para Devolver libro, cambiando es estado disponible a false
            if (!disponible) { //si no esta en el estado de disponible, es decir, si dispoible no es true, quiere decir que el libro no esta disponible, entonces lo cambia a true
                disponible = true; //vuelve a estar disponible
                std::cout << "El libro ha sido devuelto" << std::endl; //imprime esto
            } else{
                std::cout << "El libro esta disponible" << std::endl;
            }
        }
    };

    std::vector<Libro> coleccion;

    // Método que busca un libro en la colección por su título.
    Libro*  buscarLibro(const std::string& tituloBuscado) { //
        for (auto& libro : coleccion) {
            if (libro.titulo == tituloBuscado) { //Si existe el libro que introdujo el usuario, en la coleccion, devuelve el libro
                return &libro;
            }
        }
        // Devuelve un puntero al libro si lo encuentra, o nullptr si no existe
    return nullptr;
}
   
    // Método para agregar un nuevo libro a la colección de la biblioteca
    void agregarLibro(const Libro& nuevoLibro) { 
        //recorremos todos los libros en la coleccion
        for (const auto& libro : coleccion) {   
            //comparamos el titulo del nuevo libro con los ya existentes, oara evitar duplicados
            if (libro.titulo == nuevoLibro.titulo) {
                std::cout << "El libro ya existe en la biblioteca" << std::endl;
                return; //salimos del metodo sin agregar el libro
            }
        }
        // Si no se encontró ningún duplicado, agrega el nuevo libro a la colección
        coleccion.push_back(nuevoLibro); //mensaje de confirmacion
       std::cout << "El libro se ha añadido con exito" << std::endl;
    }
        

    void mostrarInventario() {
        for (auto& libro : coleccion) { //aplicamos la funcion mostrar detalles completos a todos los libros en coleccion
            libro.mostrarDetallesCompletos();
        }
    }
       

};
int main() {
    //creamos una instancia de la clase biblioteca para poder gestionar los books
    Biblioteca miBiblioteca;
    int opcion = 0; //declaramos una variable de input

    //creanis seis objetos libro para la biblioteca
    Biblioteca::Libro libro1;
    Biblioteca::Libro libro2;
    Biblioteca::Libro libro3;
    Biblioteca::Libro libro4;
    Biblioteca::Libro libro5;
    Biblioteca::Libro libro6;
    
    //agregamos los libros
    libro1.titulo = "Cien años de soledad";
    libro1.autor = "Gabriel García Márquez";
    libro1.anioPublicacion = 1967;
    libro1.disponible = true;

    libro2.titulo = "El principito";
    libro2.autor = "Saint-Exupéry";
    libro2.anioPublicacion = 1950;
    libro2.disponible = true;
    
    libro3.titulo = "El señor de los anillos";
    libro3.autor = "JRR Tolkien";
    libro3.anioPublicacion = 2005;
    libro3.disponible = true;

    
    libro4.titulo = "Las aventuras de Sherlock Holmes";
    libro4.autor = "Arthur Conan Doyle";
    libro4.anioPublicacion = 1970;
    libro4.disponible = true;

    libro5.titulo = "El temor de un hombre sabio";
    libro5.autor = "Patrick Rothfuss";
    libro5.anioPublicacion = 2006;
    libro5.disponible = true;

    libro6.titulo = "El bosón de Higgs no te hará la cama";
    libro6.autor = "Javier Santaolalla";
    libro6.anioPublicacion = 2010;
    libro6.disponible = true;
    
    //Agrega los libros a la biblioteca usando el metodo de ahrehar
    miBiblioteca.agregarLibro(libro1);
    miBiblioteca.agregarLibro(libro2);
    miBiblioteca.agregarLibro(libro3);
    miBiblioteca.agregarLibro(libro4);
    miBiblioteca.agregarLibro(libro5);
    miBiblioteca.agregarLibro(libro6);


    std::cout << "Información de la biblioteca:" << std::endl;

    while (opcion != 5) {
        std::cout << "\n--- BIBLIOTECA DIGITAL ---" << std::endl;
        std::cout << "1. Anadir libro" << std::endl;
        std::cout << "2. Mostrar inventario" << std::endl;
        std::cout << "3. Prestar libro" << std::endl;
        std::cout << "4. Devolver libro" << std::endl;
        std::cout << "5. Salir" << std::endl;
        std::cout << "Seleccione una opcion: ";
        std::cin >> opcion;
        
        // Limpiar el buffer de entrada para futuras lecturas de texto
        std::cin.ignore();

        // Usar un switch o if-else para manejar la opción del usuario
        if (opcion == 1) {
            Biblioteca::Libro nuevoLibro;
            std::cout << "Ingrese el nombre del libro: ";
            std::getline(std::cin, nuevoLibro.titulo);
            std::cout << "Autor: ";
            std::getline(std::cin, nuevoLibro.autor);
            std::cout << "Ingrese el año de publicación: ";
            std::cin >> nuevoLibro.anioPublicacion;
            std::cin.ignore(); //Limpua el biffer despues de leer el año
            nuevoLibro.disponible=true; //va estar disponible por que a penas lo estas agregando
            miBiblioteca.agregarLibro(nuevoLibro); //se agrega el libro
        }
        else if (opcion == 2) { // se muestran los datos del inventario 
            miBiblioteca.mostrarInventario();
        }
        else if (opcion == 3) {
            std::string titulo;
            std::cout << "Ingrese el titulo del libro a prestar: ";
            std::getline(std::cin, titulo);
            Biblioteca::Libro* libro = miBiblioteca.buscarLibro(titulo);
            if (libro) {
                libro -> prestarLibro(); //si se encuentra el libro se presta
            } else {
                std::cout << " Libro no encontrado" <<std::endl;
            }
        }
        else if (opcion == 4) {
            std::string titulo; //variable titulo
            std::cout << "Ingrese el titulo del libro a devolver: ";
            std::getline(std::cin, titulo); //El getline es para capturar texto hasta que el usuario aprete enter
            Biblioteca::Libro* libro = miBiblioteca.buscarLibro(titulo);
            if (libro) {
                libro -> devolverLibro(); //si se encuentra el libro, se presta
            } else {
                std::cout << " Libro no encontrado" <<std::endl;
            }
        }
    }
    //fin del programa
    return 0;
}

