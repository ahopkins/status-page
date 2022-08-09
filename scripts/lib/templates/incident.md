---
layout: IncidentDetail
permalink: /incident/{{ issue.ident }}.html
id: {{ issue.id }}
ident: {{ issue.ident }}
state: {{ issue.state }}
component: {% if issue.component %}{{issue.component.title}}{% else %}null{% endif %}
created_at: {{ issue.created_at.isoformat() }}
updated_at: {{ issue.updated_at.isoformat() }}
closed_at: {% if issue.closed_at %}{{ issue.closed_at.isoformat() }}{% else %}null{% endif %}
hash: {{ issue.to_hash() }}
managed: true
---

# {{ issue.title }}
{% if issue.component %}<Label color="{{ issue.component.color }}">{{ issue.component.title }}</Label> {% endif %}<Label color="dddddd">{{ issue.state }}</Label>

{{ issue.body }}

{% if comments %}
## Updates
{% for comment in comments %}
{% include "comment.md" with context %}
{% endfor %}
{% endif %}
