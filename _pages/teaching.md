---
layout: page
permalink: /courses/
title: courses
description: Courses offered by the faculty of Reasoning and Learning Lab
nav: true
---

{% assign courses = site.data.courses | where: "active", true | sort: 'semester' %}

{% if courses.size != 0 %}

## Active Courses

{% for course in courses %}

<div id="{{course.name | replace: ' ', '' }}" class="row">
<div class="col-md-12">
<h4>{{course.name}}</h4>
<p>Offered By: <a href="{{course.offered_by | datapage_url: '../people'}}">{{course.offered_by}}</a>, Semester: {{course.semester}}</p>
</div>
<br>
<div class="col-md-12">
{{course.description | markdownify}}
{% if course.website %}
    <i class="fa fa-globe"></i> &nbsp; <a href= "{{course.website}}" target="_blank">{{course.website}}</a></div>
{% endif %}
</div>
<hr>

{% endfor %}

{% endif %}

{% assign courses = site.data.courses | where: "active", false | sort: 'semester' %}

{% if courses.size != 0 %}

## Past Courses

<div class="row">
<ul>
{% for course in courses %}
    <li><a href="{{course.website}}">{{course.name}}</a>, {{course.semester}}</li>
{% endfor %}
</ul>
</div>

{% endif %}

More courses available from the Mila Faculty here: [https://mila.quebec/en/cours/](https://mila.quebec/en/cours/)
