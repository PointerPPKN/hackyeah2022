<script>
    import { Router, Link, Route } from "svelte-routing";

const goBack = () => {
    return window.location.href='http://127.0.0.1:5137/';
}

</script>
<div class="container">
    <div id="button1"><p><Link to="about">🔙</Link></p></div>

    <form action="http://127.0.0.1:5000/data/create" method="POST" on:submit={() => window.location.href='http://127.0.0.1/'}>
        <div>
          <label for="tag_type">Tag Type</label>
          <input type="text" id="tag_type" name="tag_type" required>
        </div>

        <div>
          <label for="cord_x">cord_x</label>
          <input type="number" id="cord_x" name="cord_x" required>
        </div>

        <div>
          <label for="cord_y">cord_y</label>
          <input type="number" id="cord_y" name="cord_y" required>
        </div>
       <input type=submit value="Add">
      </form>

</div>

<style>

    .create {
        display: grid;
        justify-content: center;
        align-items: center;
        width: 80px;
        height: 200px;
    }
    .container{
        display: grid;
        justify-content: center;
        align-items: center;
        position: relative;
        width: 30vw;
        margin-top: 5.5%;
        margin-right: 3.5%;
        height: 80vh;
        float: right;
        box-sizing: border-box;
        background: #608363;
        border: 4px solid #000000;
        box-shadow: 4px 4px 0px #000000;
    }
    .container > *{
        text-align: left;

    }
    .container > img {
        width: 90%;
        margin-top: 15%;
        border: 2px solid #000000;
        box-shadow: 0px 0px 0px 2px #381C1C, 0px 0px 0px 4px #E79B7B, 0px 0px 0px 6px #FFFFFF;
    }
    #button1{
        padding: 0.5% 3% 0.5% 3%;
        background-color: white;
        float: right;
        margin-bottom: 5%;
        display: inline-block;
        margin-block-end: auto;
        margin-block-start: auto;
        border: 4px solid #000000;
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
        top: 1%;
        position: absolute;
        font-size: 1.5rem;
    }
    #tittle{
        float: left;
        margin-left: 5%;
        margin-top: 5%;
        display: inline-block;
        padding: 2%;
        background-color: red;
        box-sizing: border-box;
        background: #28816F;
        border: 4px solid #000000;
    }
    #tittle>h1,p{
        margin-block-end: auto;
        margin-block-start: auto;
        color: white;
    }
    #button2{
        padding: 2% 8% 2% 8%;
        float: right;
        margin-left: 5%;
        margin-bottom: 5%;
        display: inline-block;
        margin-block-end: auto;
        margin-block-start: auto;
        border: 4px solid #000000;
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
        transform: rotate(-7.14deg);
        bottom: 5%;
        position: absolute;
        left: 50%;
    }

    #button2 > p {
        font-size: 1.4em;
    }
</style>