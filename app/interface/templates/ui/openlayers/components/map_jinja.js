    const map = new ol.Map({
        target: '{% if ctx.target_id %}{{ ctx.target_id }}{% else %}olmap{% endif %}',
        layers: [
            new ol.layer.Tile({ source: new ol.source.OSM() })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat({% if ctx.view_center %}{{ ctx.view_center }}{% else %}[0,0]{% endif %}),
            zoom: {% if ctx.view_zoom %}{{ ctx.view_zoom }}{% else %}3{% endif %}
        })
    });
