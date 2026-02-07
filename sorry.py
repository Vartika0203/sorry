<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>I'm Sorry</title>
<style>
    body{
        margin:0;
        height:100vh;
        display:flex;
        justify-content:center;
        align-items:center;
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        font-family: Arial, sans-serif;
        overflow:hidden;
    }

    .container{
        text-align:center;
        background:white;
        padding:40px;
        border-radius:20px;
        box-shadow:0 10px 30px rgba(0,0,0,0.2);
    }

    h1{
        color:#ff4d6d;
        font-size:40px;
    }

    p{
        font-size:18px;
        margin-bottom:30px;
    }

    button{
        padding:12px 25px;
        margin:10px;
        border:none;
        border-radius:10px;
        font-size:16px;
        cursor:pointer;
        transition:0.3s;
    }

    #yes{
        background:#4CAF50;
        color:white;
    }

    #yes:hover{
        background:#45a049;
        transform:scale(1.1);
    }

    #no{
        background:#ff4d4d;
        color:white;
        position:absolute;
    }

    .message{
        font-size:24px;
        color:#4CAF50;
        margin-top:20px;
        display:none;
    }
</style>
</head>
<body>

<div class="container">
    <h1>Oye I'm genuinely sorry, itna nhi gussa hona chahiye tha i was hungry that time and angry to so yk this deadly combination right? 😔</h1>
    <p>Dekh iss baar jyada kuch bolunga nhi boht roothna manana hua hai dono ke baare mai, abbse i swear gussa ka "g" bhi nhi aane dunga aur agar galti se aaya to tu jo punishment degi wo chalega .<br>iss baar maan jaaa plzz vartikaaa ?</p>

    <button id="yes">Maan gayyiii ❤️</button>
    <button id="no">No 😤</button>

    <div class="message" id="msg">Im telling ki u wont regret this , get ready to see me without gussaaaa , baki yk u matter to me the most , ye gussa vussa sab temporary hota hai, our friendship is permanent!!! 💕</div>
</div>

<script>
const noBtn = document.getElementById('no');
const yesBtn = document.getElementById('yes');
const msg = document.getElementById('msg');

// Make the "No" button run away
noBtn.addEventListener('mouseover', () => {
    const x = Math.random() * (window.innerWidth - 100);
    const y = Math.random() * (window.innerHeight - 50);

    noBtn.style.left = x + "px";
    noBtn.style.top = y + "px";
});

// When forgiven
yesBtn.addEventListener('click', () => {
    msg.style.display = "block";
});
</script>

</body>
</html>
