{%- extends 'basic.tpl' -%}

{% block header %}

<style type="text/css">

/* Remove prompts like [1] from output. */
div.prompt {
    display: none;
}

/* Remove indentation of notebook. */
div.cell {
    padding-left: 0px;
}
div.text_cell_render {
    padding: 0px;
}

</style>

{%- endblock header %}
