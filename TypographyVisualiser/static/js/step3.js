$.ajax({
            url: "/Outline",
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

$("#redirect-step-1").on("click", event => {
    event.preventDefault();
    window.location.href = "/Start"
 }
    $.ajax({
        url: "/resetFolders",
        method: 'POST'
    })
})