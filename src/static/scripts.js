$(document).ready(function () {
    // debugger;
    // let userid=1;
    // let url = '{{ route("getitemqty",":userid") }}'
    // url = url.replace(':userid', userid);
    let url='https://8264-111-119-49-183.ngrok.io'
    
    // $.get(url).then(function(response){
    //     console.log(response,"helllllllllllllllllllllll")
    //     debugger;
    // })

    $.ajax({
        url: url,
        async: true,
        method: "GET",
        headers: {
            "accept": "text/xml",
            "Access-Control-Allow-Origin": "*"
        },
        crossDomain: true,
        success: function (result) {
            debugger
        }
    })
});
