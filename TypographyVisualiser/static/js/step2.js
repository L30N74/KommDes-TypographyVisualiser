document.getElementById("rangevalue_low").value = document.getElementById("thresh_low").value;
document.getElementById("rangevalue_high").value = document.getElementById("thresh_high").value;

function render() {
    let range_low = document.getElementById("rangevalue_low").value;
    let range_high = document.getElementById("rangevalue_high").value;

    $.ajax({
        url: "/Contours",
        data: {
            'imagePath': 'static/images/kitten/kitten-2.jpg',
            'thresh_low': range_low,
            'thresh_high': range_high
        },
        method: 'POST'
    })
    .done(() => {
        // Ladeanimation abspielen
        $("#outlined_image").attr("src", "");

        setTimeout(() => {
            let source = "../static/output/result.jpg?" + (new Date()).getTime();   // Um caching des Bildes zu verhindern, wird ein timestamp mitgegeben
            $("#outlined_image").attr({"src": source, "class": "img_result"});
        }, 2000)

    })
}

$("#redirect-step-3").on("click", event => {
    event.preventDefault();
    window.location.href = "/Finish"
})
$('#color-picker').spectrum({
    type: "color"
});