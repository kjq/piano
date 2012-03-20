<%inherit file="piano.web.templates:base.mako" />
<%namespace name="menu" file="piano.web.widgets:menu.mako" import="*"/>

<h1 class="title">Welcome to the <code>${page_title}</code> Site</h1>
<p>ID: ${page_id}</p>
<p>Date Created: ${page_created}</p>
<br/>
<p>#Views: ${page_views}</p>
<%menu:widget name="menu"/>
<a href="${add_page_url}">Add a Page</a>
<br/><br/>