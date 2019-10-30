// function substitutePdfVariables() {

//     var vars={};
//     var pdf_keys=document.location.search.substring(1).split('&');
//     for(var pdf_key_value in pdf_keys) {var z=pdf_keys[pdf_key_value].split('=',2);vars[z[0]] = unescape(z[1]);}
//     var pdf_keys=['frompage','topage','page','webpage','section','subsection','subsubsection'];
//     for(var pdf_key_value in pdf_keys) {
//         var y = document.getElementsByClassName(pdf_keys[pdf_key_value]);
//         for(var j=0; j<y.length; ++j) y[j].textContent = vars[pdf_keys[pdf_key_value]];
//     }
// }

(function substitutePdfVariables() {
    var vars={};
    var x=document.location.search.substring(1).split('&');
    for(var i in x) {var z=x[i].split('=',2);vars[z[0]] = unescape(z[1]);}
    var x=['frompage','topage','page','webpage','section','subsection','subsubsection'];
    for(var i in x) {
        var y = document.getElementsByName(x[i]);
        for(var j=0; j<y.length; ++j) y[j].textContent = vars[x[i]];
    }
})();