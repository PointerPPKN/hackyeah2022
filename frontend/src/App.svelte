<script>
  import Map from './components/Map.svelte';
  import Card_place from './components/Card_place.svelte';
  import Card_list from './components/Card_list.svelte';
</script>

<div class="app">
  <Map x={11} y={43}/>
  <Card_place />
  <Card_list />
</div>

<style>
  .app {
    text-align: center;
  }
</style>