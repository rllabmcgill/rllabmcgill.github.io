---
layout: page
permalink: /team/
title: Team
description:
---

## Core Professors

{% assign coreprofs = site.data.professors | where: "level", "core" | sort: 'name' %}

<div class="row">

{% for person in coreprofs %}

{% include prof.html %}

{% endfor %}

</div>
<hr>

## Affiliate Professors

{% assign afprofs = site.data.professors | where: "level", "affiliate" | sort: 'name' %}

<div class="row">

{% for person in afprofs %}

{% include person.html %}

{% endfor %}

</div>
<hr>

## Postdoctoral Fellows

{% assign postdocs = site.data.students | where: "level", "postdoc" | sort: 'name' %}

<div class="row">

{% for person in postdocs %}

{% include person.html %}

{% endfor %}

</div>
<hr>

## Ph.D. Students

{% assign phds = site.data.students | where: "level", "phd" | sort: 'name' %}

<div class="row">

{% for person in phds %}

{% include person.html %}

{% endfor %}

</div>
<hr>

## M.Sc. Students

{% assign mscs = site.data.students | where: "level", "msc" | sort: 'name' %}

<div class="row">

{% for person in mscs %}

{% include person.html %}

{% endfor %}

</div>
<hr>

## Alumni

{% assign alumnis = site.data.students | where: "level", "alumni" | sort: 'degree_year'  %}

<div class="row">
<ul>

{% for person in alumnis %}

{% include alumni.html %}

{% endfor %}

</ul>
</div>
<hr>
