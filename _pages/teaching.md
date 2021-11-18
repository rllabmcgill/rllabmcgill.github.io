---
layout: page
permalink: /courses/
title: courses
description: Courses offered by the faculty of Reasoning and Learning Lab
nav: true
---

{% for course in site.data.courses %}

<div id="{{course.name | replace: ' ', '' }}" class="row">
<h4 class="col-md-12">{{course.name}}</h4>
<br>
<div class="col-md-12">
{{course.description | markdownify}}
{% if course.website %}
    <i class="fa fa-globe"></i> &nbsp; <a href= "{{course.website}}" target="_blank">{{course.website}}</a></div>
{% endif %}
</div>
<hr>

{% endfor %}

More courses available from the Mila Faculty here: [https://mila.quebec/en/cours/](https://mila.quebec/en/cours/)
