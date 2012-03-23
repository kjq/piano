<%inherit file="piano.web.templates.widget:base.mako"/>

<%def name="widget()">
	% for link in request.crumb.links:
      	<a href="${link[0]}">${link[1]}</a>&nbsp;&nbsp;/
    % endfor
</%def>
