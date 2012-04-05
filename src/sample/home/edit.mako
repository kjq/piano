<%inherit file="piano.web.templates.page:base.mako"/>
<%namespace name="vw" module="sample.home.views"/>

<p>This is my <b>EDITABLE</b> home body</p>
------------------------------------------

<form action="${save_page_url}" method="POST">
	Page name: <input type="text" name="page_title" value="${page_title}"/>
	<br/>
	Page slug: <input type="text" name="page_slug" value="${page_slug}"/>
	<br/>
	Intro Message: <input type="text" name="data_intro_message" value="${page_data['intro_message']}"/>
	<br />
	Intro Image: <input type="text" name="data_intro_image" value="${page_data['intro_image']}"/>
	<br />
	<input type="submit" name="form.submitted" value="Save Changes" />
</form>

