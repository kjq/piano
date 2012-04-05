<%inherit file="piano.web.templates:base.mako" />

<p>Available Versions...</p>
<table>
    % for v in versions:
        <tr>
        	<td><a href="v/${v[0]}" target="_blank">${v[0]}&nbsp;::&nbsp;${v[1]}</a></td>
    	</tr>
	% endfor
</table>