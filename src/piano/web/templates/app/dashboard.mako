<%inherit file="piano.web.templates:base.mako" />

<h1 class="title">Welcome to the <code>${app_title}</code> Dashboard</h1>
<br/>
<a href="${new_site_url}">Create a Site</a>
<br/><br/>
<p>Available Sites...</p>
<table>
    % for site in sites:
        <tr>
        	<td><a href="${site.slug}">${site.title}</a></td>
        	<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        	<td><a href="${site.slug}/delete-site">Delete</a></td>
    	</tr>
	% endfor
</table>