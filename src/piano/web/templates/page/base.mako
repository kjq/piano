<%inherit file="piano.web.templates:base.mako" />
<%namespace name="menu" file="piano.web.widgets:menu.mako" import="*"/>

<h1 class="title">Welcome to a user-defined <code>${page_title}</code> page</h1>
<p>ID:${page_id}</p>

<%menu:widget name="menu" page='${page_slug}'/>

<p>------ Actions for '${page_template}' -----</p>

%if edit_page_url is not None:
	<a href="${edit_page_url}">Edit this Page</a>
%endif

<br/><br/>
<p>------ Body from '${page_template}' -----</p>

<br/>
${next.body()}
<br/>
<p>------Actions for 'this' form -----</p>
<form action="${save_page_url}" method="POST">
	Child page name: <input type="text" name="page_title" />
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
	<input type="submit" name="form.submitted" value="Add child to this Page" />
</form>