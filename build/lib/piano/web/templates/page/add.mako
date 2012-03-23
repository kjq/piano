<%inherit file="piano.web.templates:base.mako" />

<form action="${save_page_url}" method="POST">
	Child page name: <input type="text" name="title" />
	<br />
	Child page template:
	<select name="source">
		  <%
		  	  avail_pages = h.available_pages()
		  %>
		  %for p in avail_pages:
		  	<option value="${p[0]}">${p[1]}</option>
		  %endfor
	</select>
	<br/>
	<input type="submit" name="form.submitted" value="Add Child Page" />
</form>