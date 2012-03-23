<%inherit file="piano.web.templates:base.mako" />

<form action="${save_site_url}" method="POST">
	Site name: <input type="text" name="title" /><br />
	<input type="submit" name="form.submitted" value="Create" />
</form>