<%inherit file="piano.web.templates:base.mako" />

<form action="${new_site_url}" method="POST">
	Site name: <input type="text" name="site_title" /><br />
	<input type="submit" name="form.submitted" value="Create" />
</form>