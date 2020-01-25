"use strict";
var request = new XMLHttpRequest();

$(document).ready(()=>{
    $('#submitButton').click(()=>{
        let input = '';
        input = $('#inputText').val();
        request.open("POST", "http://localhost:8088", true);
        request.setRequestHeader("Content-type", "text/plain");
        request.send(input);
    });

    request.onreadystatechange = () => {
        if (request.readyState == XMLHttpRequest.DONE && request.status == 200){
            $('#result').text(request.responseText);
        }
    }
});