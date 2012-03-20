<%inherit file="piano.web.templates.page:base.mako"/>
<%namespace name="vw" module="sample.home.views"/>

<p>This is my home body</p>
------------------------------------------

<p>Code says "${vw.say_hello('world')}"</p>
------------------------------------------

<p>Code returns dict with:</p>
<ul>
	%for k,v in vw.get_some_data().iteritems():
		<li>${k} = ${v}</li>
	%endfor
</ul>
<p>Last value is: ${vw.get_some_data()['key3']}</p>


