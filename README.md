<h1>Selenium-Practical-Project</h1>


<p>Selenium Webdriver: Manipula navegadores Web nativamente, suportando varias linguagens de programação. (popular)</p>
<p>**Selenium IDE:** Extensão do Chrome, Firefox e Edge. Gravar e reproduzir interações com o navegador.</p>
<p>Selenium Grid: Usa o selenium webdriver para rodar testes em varias maquinas ao mesmo tempo.</p>

<h2>Selenium Webdriver</h2>

<li>É uma biblioteca /Modulo para interagir com navegadores</li>
<li>Também pode ser considerado uma API (interface de comunicação entre dois sistemas “codigo ↔ navegador”)</li>
<li>Usado para automatizar testes de GUI</li>

## Mapeando Elementos da tela

<h2>Tipos de Locators</h2>

<strong>Selenium WebDriver:</strong>

<strong>Locators:</strong>
<ul>
  <li>ID</li>
  <li>NAME</li>
  <li>LINK_TEXT</li>
  <li>Class_Name</li>
  <li>TAG_NAME</li>
  <li>PARTIAL_LINK_TEXT</li>
</ul>

<strong>Locators customizáveis:</strong>
<ul>
  <li>CSS_SELECTOR</li>
  <li>XPATH (mais utilizado na automação de testes)</li>
</ul>

<h2>XPath - O que é?</h2>
<ul>
  <li>É uma sintaxe para definir partes de um documento XML</li>
  <li>Xpath pode ser usado para navegar por elementos e atributos em um documento XML</li>
  <li>XPath usa expressões de caminho para navegar em documentos XML</li>
  <li>XPath contém uma biblioteca de funções padrão</li>
  <li>Xpath é usado para localizar elementos em uma página web por meio do DOM</li>
  <li>XPath é o endereço do elemento em uma página</li>
</ul>

<p>Absolute/Full Xpath → /html/body/main/div/form/div/div[2]/button</p>
<p>Relative/Partial Xpath → <code>"//button[@class='btn btn-outline-primary mt-3']"</code> (mais utilizado)</p>

<h3>Funções no XPath</h3>
<ul>
  <li>Contains()</li>
</ul>

<h2>Comandos do Selenium WebDriver</h2>

<h3>Comandos de navegação</h3>
<ul>
  <li>get()</li>
  <li>maximize_window()</li>
  <li>refresh()</li>
  <li>back()</li>
  <li>forward()</li>
  <li>close()</li>
  <li>quit()</li>
</ul>

<h3>Comandos da aplicação</h3>
<ul>
  <li><strong>browser.</strong></li>
  <li>title</li>
  <li>current_url</li>
  <li>page_source (código-fonte)</li>
</ul>

<h3>Comandos para localizar elementos</h3>
<ul>
  <li><strong>browser.</strong></li>
  <li>find_element()</li>
  <li>find_elements()</li>
</ul>

