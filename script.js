const parts=[
"THÔNG ĐIỆP GỬI VỢ HỒNG PHƯƠNG ❤",
"I love you",
"Vợ của anh nha\nHồng Phương\nNay là ngày đầu tiên",
"Bước qua tháng 8\nChúc vợ may mắn\nTrong tháng này nha!",
"Yêu em nhiều lắm! 💕"];
let i=0,t=document.getElementById('text');
function show(){t.style.animation='none';void t.offsetWidth;t.textContent=parts[i];t.style.animation='move 2s forwards';i=(i+1)%parts.length;}
show();setInterval(show,2500);