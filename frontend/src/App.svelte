<script>
  import Map from './components/Map.svelte';
  import Card_place from './components/Card_place.svelte';
  import Card_list from './components/Card_list.svelte';
  import Card_generator from './components/Card_generator.svelte';
  import Card_all from './components/Card_all.svelte';
  import { Router, Link, Route } from "svelte-routing";
  import { x_s, y_s } from './components/store';
  export let url = "";
  console.log(x_s,y_s);
</script>
<Router url="{url}">
  <Route path="/">
    <Map x={$y_s.value} y={$x_s.value}/>
    <Card_place />
    <Card_list />
  </Route>
  <Route path="generator">
    <Map x={$y_s.value} y={$x_s.value}/>
    <Card_place />
    <Card_generator/>
  </Route>
  <Route path="all">
    <Map x={$y_s.value} y={$x_s.value}/>
    <Card_place />
    <Card_all />
  </Route>
</Router>


<style>
  .app {
    text-align: center;
  }
</style>