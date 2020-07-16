$("#redirect-step-1").on("click", event => {
    $.ajax({
    url: "/resetFolders",
    method: 'POST'
})
    event.preventDefault();
    window.location.href = "/Start"
})
$.ajax({
    url: "/Outline",
    method: 'GET'
})
    .done(data => {
        let resultImage = $("<img>").attr({"class": "img-result", "src": "../static/output/final-result-0.jpg"});
        resultImage.appendTo('#image')
        $("<p>Test</p>").appendTo("#image")

    })

