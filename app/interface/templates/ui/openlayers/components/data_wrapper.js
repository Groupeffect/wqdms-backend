const MAP_DIV_ID = "{% if ctx.target_id %}{{ ctx.target_id }}{% else %}olmap{% endif %}";
const MAP_CENTER_ARRAY = [0,0];
const MAP_VIEW_ZOOM = 4;
const MAP_DRAW_TYPE = '{{ ctx.draw_type }}';
const GEOJSON = {type:"FeatureCollection",properties:{},geometry:{},features:[]};