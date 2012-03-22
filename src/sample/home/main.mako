<%inherit file="piano.web.templates.page:base.mako"/>
<%namespace name="vw" module="sample.home.views"/>

<p>This is my home body</p>
------------------------------------------

<p>From my model:</p>
<ul>
	<li>intro_message = ${page_data['intro_message']}</li>
	<li>intro_image = ${page_data['intro_image']}</li>
</ul>
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


