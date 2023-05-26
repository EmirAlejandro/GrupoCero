
function validar(){
    let valida;
    valida=validarRut();
    if(valida==false){
        return false;
    }
    valida=validarEdad();
    if(valida==false){
        return false;
    }
    valida=validarPassword();
    if(valida==false){
        return false;
    }
    return true;

}

function validarRut(){
    let rut=document.getElementById('rut').value;
    let largo= rut.trim().length;
    if(largo>10 || largo<10){
        Swal.fire({
            icon: 'error',
            title: 'Ha ocurrido un problema.',
            text: 'Largo del rut incorrecto.'
        })
        //alert('Largo del rut incorrecto')
        return false;
    }
    let num=3;
    let suma=0;
    for (let index = 0; index < 8; index++) {
        let caracter=rut.trim().slice(index,index+1);
        console.log('caracter:'+caracter+" x "+num);
        suma=suma+(caracter*num);
        num=num-1;
        if (num==1) {
            num=7;
        }
    }
    let resto= suma % 11;
    let dv = 11 - resto;
    let digito;
    if (dv>9) {
        if (dv==10) {
            digito='k';
        } else {
            digito=0;
        }
    }else{
        digito=dv;
    }
    console.log('DV:'+digito);
    let ultimo=rut.trim().slice(9,10);
    console.log('El digito escrito:'+ultimo);
    if (ultimo==digito) {
        Swal.fire('correcto');
        return true;
    }else{
        Swal.fire({
            icon: 'error',
            title: 'Ha ocurrido un problema.',
            text: 'El dv es incorrecto.'
        });
        return false;
    }

}

function validarEdad(){
    let mi_fecha= document.getElementById("fecha").value;
    let fecha_actual=new Date();
    console.log('Mi Fecha:'+mi_fecha);
    console.log('Fecha Actual:'+fecha_actual);
    let ano=mi_fecha.slice(0,4);
    let mes=mi_fecha.slice(5,7);
    let dia=mi_fecha.slice(8,10);
    let fecha_comparar=new Date(ano,(mes-1),dia);
    if(fecha_comparar>fecha_actual) {
        Swal.fire({
            icon: 'error',
            title: 'Ha ocurrido un problema.',
            text: 'Fecha ingresada es mayor a la fecha actual.'
        })
        //alert('Fecha ingresada mayor a la fecha actual');
        return false;
    }
    let dia_mili = 1000*60*60*24;
    console.log('dia en milisengudos:'+dia_mili);
    let dias_vividos=(fecha_actual.getTime()-fecha_comparar.getTime())/dia_mili;
    console.log('Dias Vividos:'+Math.trunc(dias_vividos));
    let anos_vividos= Math.trunc(dias_vividos/365);
    console.log('Años;'+anos_vividos);
    if(anos_vividos<18){
        Swal.fire({
            icon: 'error',
            title: 'Ha ocurrido un problema.',
            text: 'Eres menor edad para poder registrarte en nuestra pagina.'
        })
        //alert('eres menor edad para poder registrarte en nuestra pagina');
        return false;
    }
    return true;
}

function validarPassword() {
    var pass1= document.getElementById("txtPass1").value;
    var pass2= document.getElementById("txtPass2").value;
    if (pass1 == pass2) {
        //alert('OK');
        let largo= pass1.length;
        let largo2=pass2.length;
        if(largo<5) {
            Swal.alert('El largo de la contraseña 1 deber ser mayor a 5.');
            return false;
        }
        if(largo2<5) {
            Swal.alert('El largo de la contraseña 2 deber ser mayor a 5.');
            return false;
        }
        console.log('OK')
        return true;
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Ha ocurrido un problema.',
            text: 'Las Contraseñas no son iguales.'
        })
        console.log('Pass no son iguales')
        return false;
    }
}

  

