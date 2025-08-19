        var base_layer = new ol.layer.Tile({
            // source: map
            // source: new ol.source.XYZ({
            //     attributions: "NASA Worldview",
            //     maxZoom: 8,
            //     url: "https://map1{a-c}.vis.earthdata.nasa.gov/wmts-webmerc/" +
            //             "BlueMarble_ShadedRelief_Bathymetry/default/%7BTime%7D/" +
            //             "GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg"
            // })
        });
        
        var options = {
            base_layer: base_layer,
            geom_name: 'Point',
            id: 'id_point',
            map_id:  '{% if target_id %}{{ target_id }}{% else %}map{% endif %}',
            map_srid: 3857,
            name: 'point'
        };
        
        // var geodjango_point = new MapWidget(options);