function addGeoJSONTileWithEditor(map, geojsonData, draw_type='Point' ) {
  const vectorSource = new ol.source.Vector({
    features: new ol.format.GeoJSON().readFeatures(geojsonData, {
      featureProjection: map.getView().getProjection()
    })
  });

  const vectorLayer = new ol.layer.Vector({
    source: vectorSource
  });

  map.addLayer(vectorLayer);

  const modify = new ol.interaction.Modify({ source: vectorSource });
  map.addInteraction(modify);

  const draw = new ol.interaction.Draw({
    source: vectorSource,
    type: draw_type // Change to 'Point', 'LineString', etc. as needed
  });
  map.addInteraction(draw);

  const snap = new ol.interaction.Snap({ source: vectorSource });
  map.addInteraction(snap);
}


function getMapDataAsGeoJSON(map) {
  const geojsonFormat = new ol.format.GeoJSON();
  const features = [];

  map.getLayers().forEach(layer => {
    if (layer instanceof ol.layer.Vector) {
      const source = layer.getSource();
      if (source) {
        features.push(...source.getFeatures());
      }
    }
  });

  return geojsonFormat.writeFeaturesObject(features, {
    featureProjection: map.getView().getProjection()
  });
}


function clearAllLayers(map) {
  const layers = map.getLayers().getArray();
  layers.forEach(layer => {
    map.removeLayer(layer);
  });
}

function resetMap(map,) {
  // Remove all layers
  map.getLayers().clear();

  // Remove all interactions
  map.getInteractions().clear();

  // Remove all overlays
  map.getOverlays().clear();

  // Dispose the current map instance
  map.setTarget(null);
}

