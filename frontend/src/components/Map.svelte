<script>
    import { onMount, onDestroy } from 'svelte'
    import { Map, NavigationControl, Marker } from 'maplibre-gl';
    import 'maplibre-gl/dist/maplibre-gl.css';
  
    let map;
    let mapContainer;
    export let x,y;
    onMount(() => {
  
      const apiKey = 'ANx2EYNzbsX387SJBbPe';
  
      
  
      map = new Map({
        container: mapContainer,
        style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${apiKey}`,
        center: [y, x],
        zoom: 14
      });
      map.addControl(new NavigationControl(), 'top-right');
      new Marker({color: "#FF0000"})
        .setLngLat([y,x])
        .addTo(map);
    });
  
    onDestroy(() => {
      map.remove();
    });
  </script>
  
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"><img
      src="https://api.maptiler.com/resources/logo.svg" alt="MapTiler logo"/></a>
    <div class="map" id="map" bind:this={mapContainer}></div>
  </div>
  
  <style>
  
    .map-wrap {
      width: 60vw;
      float: left;
      height: 100vh; /* calculate height of the screen minus the heading */
    }
  
    .map {
      height: 100%;
    }
  
    .watermark {
      position: absolute;
      left: 10px;
      bottom: 10px;
      z-index: 999;
    }
  </style>