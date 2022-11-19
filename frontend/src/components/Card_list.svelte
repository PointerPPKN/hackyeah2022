<div class="container">
    <img src="https://cdn.cmc-gallery.pl/static/files/gallery/156/699374_1560171715.jpg" alt="">
    <div id="tittle">
        <h1>Empik Wrocław</h1>
        <p>Ul. Króla Janusza</p>
    </div>
    <div id="button"><p>Select</p></div>
</div>

<style>
    .container{
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
        margin-top: 5%;
        border: 2px solid #000000;
        box-shadow: 0px 0px 0px 2px #381C1C, 0px 0px 0px 4px #E79B7B, 0px 0px 0px 6px #FFFFFF;
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
    #button{
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

    #button > p {
        font-size: 1.4em;
    }
</style>