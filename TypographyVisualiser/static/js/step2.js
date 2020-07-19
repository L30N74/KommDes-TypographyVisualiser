document.getElementById("rangevalue_low").value = document.getElementById("thresh_low").value;
document.getElementById("rangevalue_high").value = document.getElementById("thresh_high").value;

function render() {
    let range_low = document.getElementById("rangevalue_low").value;
    let range_high = document.getElementById("rangevalue_high").value;

    $.ajax({
        url: "/Contours",
        data: {
            'thresh_low': range_low,
            'thresh_high': range_high
        },
        method: 'POST'
    })
    .done(data => {
        // read imagepaths from data into list
        let stringRep = data
        let parts = stringRep.split("\"");

        let filepaths = [];
        for(let i = 0; i < parts.length; i++){
            if(i % 2 != 0)
                filepaths.push(parts[i]);
        }

        // Ladeanimation abspielen
        $("#image").empty();

        setTimeout(() => {
            for (let path of filepaths){
                let imageSource = `${path}?${(new Date()).getTime()}`;
                let newImage = $("<img />").attr({"src": imageSource, "class": "img-result"});

                $("#image").append(newImage);
            }
        }, 2000)

    })
}

$("#redirect-step-3").on("click", event => {
    color = $('#color-picker').val();
    localStorage.setItem("color", color);
    event.preventDefault();
    window.location.href = "/Finish"
})

$('#color-picker').spectrum({
    type: "color"
});