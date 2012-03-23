<%inherit file="piano.web.templates.widget:base.mako"/>

<%def name="widget(name, page='')">
	<%
		data = rest.invoke('http://localhost:8080/services/menu?url=' + request.path + '&page=' + page)
	%>
	<ul>
		% for item in data:
			<li>
				<a href="${item['url']}">${item['title']}</a>
			</li>
		% endfor
	</ul>
</%def>
