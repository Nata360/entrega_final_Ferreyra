# entrega_final_Ferreyra

Ultima entrega para el curso de introducción a Python de Coderhouse

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
 Para correr el proyecto es necesario instalar los requerimientos que figuran en el archivo - requirements.txt -
 
 Este proyecto simula una pagina simil blog para poder subir imagenes
 El enlace de la vista inicial es http://127.0.0.1:8000/
 

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

 En la esquina superior derecha está el boton "Home", para poder redirigirse a la pagina principal desde cualquier otro apartado, 
 y dentro de la misma sección se encuentra el botón para crear un blog.
 

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

 En los botones de la esquina superior derecha se encuentra el apartado que redirige a la sección About, en donde se explica un poco sobre el creador de la página. Ésta también cuenta con un sistema para poder registrarse, iniciar sesión, acceder al listado de los blogs y en caso de ya estar ingresado, se puede editar los datos de perfil. Si el usuario registra un avatar, éste se visualiza al lado del nombre de usuario en la ezquina superior derecha.

 -----------------------------------------------------------------------------
 -----------------------------------------------------------------------------

 Para la lista de blogs se encuentra un modelo de búsqueda para clases basadas en vista que filtra a los blogs en función del nombre, en caso de contener la letra que se introduce ya aparecen resultados. Si no se encuentran resultados o no 

 -----------------------------------------------------------------------------
 -----------------------------------------------------------------------------

 Dentro de los blogs se pueden crear albunes y cada uno de ellos puede registrar imagenes con sus respectivos campos (titulo, autor, descripción, etc).
 En caso de querer borrar o editar los albunes o imágenes, sólo se puede llevar a cabo por el usuario autor de estos campos, debido a la relación ForeingKey establecida entre los modelos.

 -----------------------------------------------------------------------------
 -----------------------------------------------------------------------------

El VIDEO con la explicación y muestra de las funciones de la página se accede mediante este link: https://youtu.be/nq1KxIdI7gU

 -----------------------------------------------------------------------------
 -----------------------------------------------------------------------------

 Actualización de correcciones:

 ♠ Se ha mejorado el recorrido para crear un albun y subir una imagen:
    * Se ha corregido el error que permitía a cualquier usuario subir imagenes en albunes y blogs ajenos.

 ♠ Se añadió una pantalla para consultar la información del usuario creador del blog y del albún
    * Se ha añadido un campo "biografía" con texto enriquecido al modelo "InfoExtra".
    * Se ha añadido una plantilla con la información del usuario ingresado en la sección de edición de usuario.
 ♠ Se ha corregido el problema para cambiar la contraseña en la sección de edición de usuario.
    * Se agregó el botón para hacerlo
 ♠ Se ha agregado un sistema de mensajería mediante una nueva aplicación:
    * Para acceder a la bandeja de entrada se agregó el apartado "mensajes" en la parte superior derecha.
    * Se puede envíar un mensaje al ingresar a un blog, albun o a la información de usuario.
 ♠ Hubo algunos cambios estéticos menores.

 -----------------------------------------------------------------------------
 -----------------------------------------------------------------------------

Gracias por la paciencia, todo esto es muy nuevo para mi :D


