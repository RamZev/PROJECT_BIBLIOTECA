# Pasos para instalar el Proyecto Biblioteca 

1.	Acceda al repositorio del Proyecto, con el enlace  
https://github.com/RamZev/PROJECT_BIBLIOTECA
2.	En el repositorio, de click al botón Code  
![image](https://github.com/user-attachments/assets/9e0084da-f07b-41a6-af64-7b493e83e0f3)
3. Luego de click a la opión Download ZIP
4. El archivo ZIP al descargarlo le muestra el nombre:  
PROJECT_BIBLIOTECA-main.zip  
Ubique la unidad o ruta donde desea descargar el archivo y le da click al botón Guardar
5. En este ejemplo lo he descargado en la unidad C:\, ahora me dirijo a la unidad C:\ y ubico el archivo ZIP
![image](https://github.com/user-attachments/assets/e5cd6903-7045-4b4d-bce1-2f8f39fe49c3)
6. Coloque el cursoer del mouse sobre el archivo y de click al botón derecho del mouse, luego de click a la opción Extraer aquí
![image](https://github.com/user-attachments/assets/80f35567-1453-4b29-8e21-1045ca01a154)
7. Ahora verifique si la carpeta PROJECT_BIBLIOTECA-main se creó correctamente
![image](https://github.com/user-attachments/assets/fef59cec-484e-4b7a-ab21-8422e57533bf)
8. Elimine del nombre de la carpeta, la cadena -main
![image](https://github.com/user-attachments/assets/792aa126-ee84-4d91-b107-9493a608d94c)
9. Ahora abra esa carpeta desde Visual Studio Code
![image](https://github.com/user-attachments/assets/4292729b-8c03-44e9-b589-3fe581232987)
En la advertencia, de click al botón **Confiar en la carpeta y continuar**
10. En la pregubnta: **¿Confía en los autores de los archivos de esta carpeta?**
De click al botón **Si, confío en los autores**
11. Cierre la Pestaña de **Bienvenido**
![image](https://github.com/user-attachments/assets/031a2c4f-ba08-489a-9b98-cd35b4556073)
12. En el menú de VSC vaya a la opción **Terminal** y luego seleccione **Nuevo Terminal**
13. En la parte inferior de VSC observará lo siguiente:
![image](https://github.com/user-attachments/assets/df947634-583b-4353-ba25-6ee623b37d2e)
14. En caso no tenga instalado el paquete virtualenv, proceda a instalarlo desde el terminal
con la instrucción: **pip install virtualenv**  
![image](https://github.com/user-attachments/assets/d88e5301-c592-4680-b628-73e2cd5e468e)
15. El paquete **virtualenv** nos permite crear el entorno virtual para el Proyecto.
Es indispensable, tener instalado el lenguaje Python, versión 3.11 o superior, antes de crear el entorno virtual.
Para crear el entorno virtual, escribimos la siguiente instrucción: **python -m virtualenv venv**  
![image](https://github.com/user-attachments/assets/6e771e70-71f4-4a59-9e3d-a9f12d805cab)
16. Ahora procesa a activar el entorno virtual con la instrucción: **venv\Scripts\activate**
![image](https://github.com/user-attachments/assets/0e3b9536-25c4-4660-a98e-adb341e9b548)  
Si la activación fue coorecta, al lado izquierdo del Prompt debe aparecer: **(venv)**
En caso no aparezca, repita la secuencia relativa al entorno virtual.
17. Ahora proceda a instalar las dependencias del Proyecto, identificadas en **requiremets.txt**
Para ello, esciba la instrucción: **pip install -r requirements.txt**
![image](https://github.com/user-attachments/assets/0b793425-885b-4db7-9241-52f122ee1076)
18. Ahora, trasládese a la carpeta del Proyecto:  
![image](https://github.com/user-attachments/assets/218880d0-ef34-48ed-ba97-04a545a4894d)
19. Ahora, levante el servidor de desarrollo de Django con la instrucción: **python manage.py runserver**
![image](https://github.com/user-attachments/assets/dad26fad-c0ee-40ad-9312-849b2553708b)
20. Ahora, presione la tecla CTRL y simultáneamente, de click a la dirección IP mostrada en el Terminal.  
Luego vaya a la pestña de su navegador que está de modo intermitente y le da click, observará:  
![image](https://github.com/user-attachments/assets/dab05264-5eed-488c-a5bc-d5d724fa8be9)

Usuario: adm
Contraseña: adm54321$$

**Autor Principal:**  
**Ricardo Ramos Zevallos - RamZev**  
pythondevs2024@gmail.com  
+51 983981484  
* Ingeniería de Sistemas  
* Ingeniería de Software  
* Análisis de Datos  
* Ciencia de Datos  
* Big Data  
* Inteligencia Artificial  

**Colaboradores:**  
Alejandro Briceño  
Wilber Quillca  
Wadid Castilla












