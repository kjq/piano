<%inherit file="piano.web.templates:base.mako" />
<%namespace name="menu" file="piano.web.widgets:menu.mako" import="*"/>

<h1 class="title">Welcome to a user-defined <code>${page_title}</code> page</h1>
<p>ID:${page_id}</p>

<%menu:widget name="menu" page='${page_slug}'/>

<p>------ Body from '${page_template}' -----</p>

<br/>
${next.body()}
<br/>
<p>------Actions for 'this' form -----</p>

%if new_page_url:
	<form action="${new_page_url}" method="POST">
		<a href="${edit_page_url}">Edit this Page</a>
		<br/><br/>
		Child page name: <input type="text" name="page_title" />
		<br />
		Child page template:
		<select name="page_source">
			  <%
			  	  avail_pages = h.available_pages()
			  %>
			  %for p in avail_pages:
			  	<option value="${p[0]}">${p[1]}</option>
			  %endfor
		</select>
		<br/>
		<input type="submit" name="form.submitted" value="Add child to this Page" />
	</form>
%endif