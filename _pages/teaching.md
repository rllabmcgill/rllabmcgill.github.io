---
layout: page
permalink: /courses/
title: courses
description: Courses offered by the faculty of Reasoning and Learning Lab
nav: true
---

{% for course in site.data.courses %}

<div id="{{course.name | replace: ' ', '' }}" class="row">
<h4>{{course.name}}</h4>
<div class="col-md-12">
<p class="text-justify">{{course.description | markdownify}}</p>
{% if course.website %}
    <i class="fa fa-globe"></i> <a href= "{{course.website}}" target="_blank">{{course.website}}</a> <br>
{% endif %}
</div>
</div>
<hr>

{% endfor %}

More courses available from the Mila Faculty here: [https://mila.quebec/en/cours/](https://mila.quebec/en/cours/)
