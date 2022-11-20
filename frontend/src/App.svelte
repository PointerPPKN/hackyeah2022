<script>
  import { Router, Link, Route } from "svelte-routing";
  import Map from './components/Map.svelte';
  import Card_place from './components/Card_place.svelte';
  import Card_list from './components/Card_list.svelte';
  import Card_generator from './components/Card_generator.svelte';
  export let url = "";
</script>

<Router url="{url}">
    <Route path="about">
      <div class="app">
        <Map x={"56.107883"} y={"27.038538"}/>
        <Card_place />
        <Card_list />
      </div>
    </Route>

    <Route path="/">
      <div class="app">
        <Map x={"51.107883"} y={"17.038538"}/>
        <Card_place />
        <Card_generator />
      </div>
    </Route>
</Router>

<style>
  .app {
    text-align: center;
  }
</style>