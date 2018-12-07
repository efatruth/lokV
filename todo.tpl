<!DOCTYPE html>
<html>
<head>
	<title> Todo-ify </title>
	<link rel="stylesheet" href="/static/normalize.css">
	<link rel="stylesheet" type="text/css" href="./static/todostylesheet.css">
</head>
<body>

  <script type="text/javascript">
  function showDiv() {
   document.getElementById('toggle').style.display = "block";
}
  </script>

    <header class="group">
        <a href="/"><h2 class="col1-4 flotV h2change">Todo-ify</h2></a>
        <nav class="navigation middle">
        <a href="/signout"><h3 id="logoutbutton">Log out</h3></a>
      </nav>
  </header>  

<section>

	<article>
	    <table class="box">
        <tr>
          <th>Þú ert skráður sem: {{ display_name }}</th>
        </tr>
        <tr>
          <th>Things to do</th>
        </tr>
        % for i in data_1:
          <tr>
            <td>{{i[0]}}</td>
            <form method="post" action="/delete">
            <td>
              <input type="radio" name="deltodo" value="{{i[1]}}" onclick="showDiv()" />
            </td>
          </tr>
        % end
        <tr>
          <td>
            <input id="toggle" style="display:none" type="submit" name="clickdel" value="Delete">
          </td> 
        </tr>
        </form>
      </table>
    </article>

    <aside>
      
    <form method="post" action="/add">
          <h3>Add to your To-Do-List</h3>
          <textarea rows="1" cols="40" name="adding"></textarea><br>
          <input type="submit" name="chore" value="SAVE">
        </form>
    </aside>
</section>

</body>
</html>