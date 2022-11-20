<script>
  import Map from './components/Map.svelte';
  import Card_place from './components/Card_place.svelte';
  import Card_list from './components/Card_list.svelte';
  import Card_generator from './components/Card_generator.svelte';
  import Card_all from './components/Card_all.svelte';
  import { Router, Link, Route } from "svelte-routing";
  export let url = "";
</script>
<Router url="{url}">
  <Route path="/">
    <Map x={"51.107883"} y={"17.038538"}/>
    <Card_place />
    <Card_list />
  </Route>
  <Route path="generator">
    <Map x={"51.107883"} y={"17.038538"}/>
    <Card_place />
    <Card_generator/>
  </Route>
  <Route path="all">
    <Map x={"51.107883"} y={"17.038538"}/>
    <Card_place />
    <Card_all />
  </Route>
</Router>


<style>
  .app {
    text-align: center;
  }
</style>