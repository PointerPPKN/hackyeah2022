<script>
    import 'maplibre-gl/dist/maplibre-gl.css';
    import { x_s, y_s } from './store';
    export let x,y,tag;
</script>

<div class="card">
    <h3>{tag}</h3>
    <p>{x}</p><p>{y}</p>
    <input type="submit" on:click={()=>{$x_s.value=x;$y_s.value=y;console.log($x_s.value);new maplibregl.Marker()
        .setLngLat([12.550343, 55.665957])
        .addTo(map);
    }} value="Select">
    <input type="submit" on:click={()=>{}} value="Delete">
</div>
<style>
    .card{
        margin-bottom: 5%;
        background-color: #28816F;
        border: 4px solid #000000;
        color: white;
        width: 90%;
        height: 13%;
    }
    .card > *{
        margin-block-end: auto;
        margin-block-start: auto;
    }
</style>