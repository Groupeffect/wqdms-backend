
function createMap(mapDiv,mapViewCenter,mapViewZoom){
    const map = new ol.Map({
        target: mapDiv,
        layers: [
            new ol.layer.Tile({ source: new ol.source.OSM() })
        ],
        view: new ol.View({
                center: ol.proj.fromLonLat(mapViewCenter),
                zoom: mapViewZoom
            })
        })
        return map
}

function geoData(){
    console.log(getMapDataAsGeoJSON(map))
}