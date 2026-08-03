const parts=[
"Chút người tôi thương",
"Luôn luôn hạnh phúc",
"Và tràn đầy sức khỏe",
"Và luôn tươi cười nha",
"I love you ❤️"
];
let i=0,t=document.getElementById('text');
function show(){
t.style.animation='none';void t.offsetWidth;
t.textContent=parts[i];
t.style.animation='move 2s forwards';
i=(i+1)%parts.length;
}
show();
setInterval(show,2500);
