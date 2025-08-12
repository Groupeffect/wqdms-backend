{% load interface %}
username: "{{ request.user.username }}",
response: {{ response.data | to_json }}