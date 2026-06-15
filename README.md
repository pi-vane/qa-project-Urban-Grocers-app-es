# Proyecto Urban Grocers 
# Pruebas para el párametro name en el kit_body para la creación de un Kit nuevo en la aplicación.

__Prerequisitos__
1. Es necesario tener instalados los paquetes __pytest__ y __requests__ antes de iniciar.
2. Ejecuta todas las pruebas con __pytest__.

__Descripción__

 - Se realiza la comproobación de las respuestas API, según la lista de comprobación. Usando como base la versión 1.0.0 de los __API docs__ para la creación de kits. 

 - __Documentación usada (API DOCS, Versión 1.0.0)__: (https://cnt-609a6b00-b7e0-4f8c-9203-d2685239ffe8.containerhub.tripleten-services.com/docs/)

__Lista de comprobación de esta versión__ ( Junio, 2026)

- [x] __KN-1__: El número permitido de carácteres (1): kit_body = { "name": "a"}
- [x] __KN-2__: El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
- [x] __KN-3__: El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
- [x] __KN-4__: El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
- [x] __KN-5__: Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
- [x] __KN-&__: Se permiten espacios: kit_body = { "name": " A Aaa " }
- [x] __KN-7__: Se permiten números: kit_body = { "name": "123" }
- [ ] __KN-8__: El parámetro no se pasa en la solicitud: kit_body = { }
- [ ] __KN-9__: Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
