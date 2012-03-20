<%namespace name="crumb" file="piano.web.widgets:crumb.mako" import="*"/>
<html>
	<head>
		<title>NGDS ${'| ' + page_title}</title>
		<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
		<meta name="keywords" content="python web application" />
		<meta name="description" content="pyramid web application" />
		<link rel="shortcut icon" href="${request.static_url('piano:static/favicon.ico')}" />
		<link rel="stylesheet" href="${request.static_url('piano:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />
	</head>
   	<body>
		<%crumb:widget/>
      	${next.body()}
   	</body>
 </html>