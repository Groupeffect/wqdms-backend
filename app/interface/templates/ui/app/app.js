{% load interface %}

{% if response.data.vueTop %}
{% include response.data.vueTop %}
{% endif %}

import { createApp } from 'vue';
const app = createApp({
    delimiters: [`[[`, `]]`],
    data(){
        {% if response.data.vueData %}
        return{
{% include response.data.vueData %}
        }
        {% endif %}
    },
    mounted(){
        {% if response.data.vueMounted %}
{% include response.data.vueMounted %}
        {% endif %}
    },
    created(){
        {% if response.data.vueCreated %}
{% include response.data.vueCreated %}
        {% endif %}
    },
    computed:{
        {% if response.data.vueComputed %}
{% include response.data.vueComputed %}
        {% endif %}
        
    },
    methods: {
        {% if response.data.vueMethods %}
{% include response.data.vueMethods %}
        {% endif %}
        
    },
    template: `{% include response.data.template %}`
})
// app.config.compilerOptions.delimiters = ['[[', ']]']
app.mount('#app')
{% if response.data.vueBottom %}
{% include response.data.vueBottom %}
{% endif %}