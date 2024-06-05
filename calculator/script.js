let display = document.getElementById('input');
let buttons = document.querySelectorAll('button');
console.log(buttons)
let btnArray = Array.from(buttons);
let str = '';

btnArray.forEach( btn => {
    btn.addEventListener( 'click', (e) => {
        if(e.target.innerHTML == 'DEL') {
            str = str.substring(0, str.length-1);
            display.value = str;
        }else if(e.target.innerHTML == 'AC') {
            str = '';
            display.value = str;
        }else if(e.target.innerHTML == '=') {
            if(str.includes('^')) { 
                let strArray = str.split("^")
                console.log(str)
                str= strArray[0]+ '**' +strArray[1];
                console.log(str)
                str = eval(str);
                display.value = str; 
            }
            str = eval(str);
            display.value = str;
        }else {
            str += e.target.innerHTML;
            display.value = str;
        }
    });
});

