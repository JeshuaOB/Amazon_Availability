<h1>Amazon_Availability</h1>
<h2>Contenido del repositorio</h2>
<p>El proyecto que contiene este repositorio consiste en un script desarrollado con Python capaz de mostrar la disponibilidad de una lista de productos comercializados en la plataforma Amazon. Cada producto se reconoce por su correspondiente código ASIN, el cual deberá ser indicado en un documento XLSX externo. Los archivos que constituyen este proyecto son:</p>
<ul>
<li>productsAMZ.py</li>
<li>productos.xlsx</li>
</ul>
<h2>Indicaciones</h2>
<p>❗ Para poder utilizar el navegador de Chrome mediante Selenium es necesario instalar el webdriver específico de este navegador, el cual podemos encontrar en la siguiente web: https://chromedriver.chromium.org/downloads. Por otro lado, deberemos indicar en el archivo principal <i>productsAMZ.py</i> la ruta donde se encuentra descargado el webdriver mediante la variable <strong>driver_path</strong>.</p>
<p>❗ Es necesario importar específicamente la versión 1.2.0 de la librería <i>xlrd</i> de Python para poder abrir archivos XLSX. Para ello, podemos aplicar en la consola el siguiente comando: <i>pip install xlrd==1.2.0</i> .</p>
<p>❗ Una vez se haya ejecutado el programa, como resultado generará un archivo XLSX denominado <i>disponibilidad.xlsx</i> donde se muestra la lista de ASIN de todos los productos con su correspondiente estado de disponibilidad.</p>
<h2>Estado</h2>
<p><strong>✔️ FINALIZADO</strong></p>
<p>📅 Ultima modificación: <strong>25/08/2021</strong></p>
