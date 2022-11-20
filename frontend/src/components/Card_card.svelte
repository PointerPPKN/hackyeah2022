<script>
    export let x,y,tag;
    global.x_var
    global.y_var
</script>

<div class="card">
    <h3>{tag}</h3>
    <p>{x}</p><p>{y}</p>
    <input type="submit" on:click={()=>{global.y_var = x, global.x_var = y}} value="Select">
    <input type="submit" on:click={()=>{}} value="Delete">
</div>
<style>
    .card{
        margin-bottom: 9px;
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