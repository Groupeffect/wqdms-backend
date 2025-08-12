{% load interface %}
username: "{{ request.user.username }}",
response: {{ response.data | to_json }},
pages: {% get_page_urls %},
host: "{% get_host %}"