---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}


<!--{: .success }
>Welcome to DSC 10! Make sure to read this website thoroughly and complete the items in the [Getting Started](https://dsc10.com/syllabus/#-getting-started) checklist.
-->

<!--{: .warning }
This site is **under construction**. Anything you read here is not finalized. This disclaimer will be removed when the site is ready for Spring 2026.-->

{: .success }
>The Final Exam is **this Saturday, June 6th from 3 to 6PM in Pepper Canyon 106**. See [Campuswire](https://campuswire.com/c/G65427605/feed/211) for more details!
>
>Earn 1 participation point by filling out both [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) and the internal [End-of-Quarter Survey](https://forms.gle/BoRKzpGu7eduDUUT6) before Saturday, June 6th at 8AM.


<!--{: .success }
>**Tip**: When working on assignments, use Ctrl+F on this page to search for a keyword and quickly find the relevant lecture. Click the "✏️ write" button to open a static version of the lecture for reference, which is much faster than loading it on DataHub.
>
>Also, make sure to use the [reference sheet]({{site.urls.reference}}) to quickly look up `babypandas` methods and see examples of how they work.
-->

<!--{: .note }
Quiz 4, coming up on **Wednesday, May 27th** covers Lectures 18 (starting with statistical models) through 22. 
-->


<a id="jump-to-current-week" href="/#{{ site.modules.first.title | slugify }}" class="btn">Jump to the current week</a>
<script>
(function() {
  var weeks = [{% for module in site.modules %}{"slug":"{{ module.title | slugify }}","start":"{{ module.days.first.date | date: '%Y-%m-%d' }}"}{% unless forloop.last %},{% endunless %}{% endfor %}];
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  var target = weeks[0].slug;
  for (var i = 0; i !== weeks.length; i++) {
    if (Math.max(today.valueOf(), new Date(weeks[i].start).valueOf()) === today.valueOf()) target = weeks[i].slug;
  }
  document.getElementById('jump-to-current-week').href = '/#' + target;
})();
</script>

{% for module in site.modules %}
{{ module }}
{% endfor %}
