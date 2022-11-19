<script>
  import Map from './components/Map.svelte';
  import Card_place from './components/Card_place.svelte';
  import Card_list from './components/Card_list.svelte';
</script>

<div class="app">
  <Map x={"51.107883"} y={"17.038538"}/>
  <Card_place />
  <Card_list />
</div>

<style>
  .app {
    text-align: center;
  }
</style>