$("#redirect-step-1").on("click", event => {
    event.preventDefault();
    window.location.href = "/Start"

    $.ajax({
        url: "/resetFolders",
        method: 'POST'
    })
})