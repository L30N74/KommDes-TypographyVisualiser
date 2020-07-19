

$.ajax({
    url: "/Outline",
    data: {'keyword': localStorage.getItem("keyword"),
            'color': localStorage.getItem("color")},
    method: 'POST'
})
    .done(data => {

        setTimeout(() => {

        let resultImage = $("<img>").attr({"class": "img-result", "src": "../static/output/final-result-0.jpg"});
        resultImage.appendTo('#image')
        $(".load-spinner").attr({"style": "display: none"})
        $("#download-button").attr({"style": "display: inline"})
        }, 3000)

    })

    $("#redirect-step-1").on("click", event => {
    event.preventDefault();
    window.location.href = "/Start"
})

