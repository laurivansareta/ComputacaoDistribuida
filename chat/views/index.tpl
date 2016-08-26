
<html>

<head></head>

<body>

<h1> Conversa </h1>
<ul>
%for (n, m) in messages:
    <li> <b>{{n}}: </b> {{m}} </li>
%end
</ul>

<form action="/send" method=POST>
    <p> Nome <input name="nome" type="text" value="{{nome}}"/> </p>
    <p> Mensagem <input name="message" type="text" /> </p>
    <p> <input value="Enviar" type="submit" /> </p>
</form>

</body>

</html>
