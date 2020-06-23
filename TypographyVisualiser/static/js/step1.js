let chosenImages = [];
let keyword = "";
let amount;

$('#form').on('submit', event => {
    keyword = $('#searchbar').val();                                        // Inhalte der Eingabefelder zwischenspeichern
    amount = $('#imageAmount').val();
    //let color = $('#colorPicker').val();
    event.preventDefault();
    // Standard HTML form-post unterbrechen, da wir ajax nutzen
    $.ajax({
        url: "/DownloadImages",                                             // Ziel festlegen (in main.py als app.route gesetzt)
        data: {'keyword': keyword, 'amount': amount},                       // Nutzereingabe einpacken
        method: 'POST'
    })
    .done(data => {                                                         // Was soll passieren, wenn search() zuende ist

        $(".search-result-images").remove();
        $(".checkbox-for-images").remove();
        $(".image-container").remove();
        $(".text").remove();
        $(".done-icon").remove();

        for (let i = 0; i < amount; i++) {
            let filename = `../static/images/${keyword}-${i.toString()}.jpg`;

            let newImage = $("<img>").attr({"src": filename, "class": "search-result-images img_" + i});
            newImage.click(event => {
                // Check setzen
                if(checkbox.val() === "true") {
                 checkbox.val(false);
                 checkbox.prop("checked",false);
                 addOrRemoveImageSelection(filename, false);
                 $("<img>").attr({"class":"selected-done-icon", "src": "../static/icons/done_green.svg"}).appendTo('#text' +i);
                } else {
                    checkbox.val(true);
                    checkbox.prop("checked",true);
                    addOrRemoveImageSelection(filename, true);
                    $(".selected-done-icon").remove();
                }
            })
            //$("#text"+i).attr({"style":"opacity:1;"});
            //let checkbox = $("<input>").attr({"type": "checkbox", "class": "checkbox-for-images form-check-input" + i, "value": false})
            let checkbox = $("<input>").attr( {"id": "checkbox-as-image" + i, "type": "checkbox", "value":"false", "name":"test"});
            let imageContainer = $("<div>").attr({"class": "image-container", "id": "image" + i});
            imageContainer.click( event => {
                if(checkbox.val() === "true") {
                 checkbox.val(false);
                 $("#text"+i).attr({"style":"opacity:0;"});
                 addOrRemoveImageSelection(filename, false);
                } else {
                    checkbox.val(true);
                    $("#text"+i).attr({"style":"opacity:1;"});
                    addOrRemoveImageSelection(filename, true);
                }
            })
            // Auf Webseite darstellen
            imageContainer.appendTo('#images');
            newImage.appendTo("#image" +i);
            checkbox.appendTo("#image"+i);
            $("<div>").attr({"class": "hover-text", "id": "text" + i}).appendTo('#image' + i);
            $("<img>").attr({"class":"done-icon", "src": "../static/icons/done_green.svg"}).appendTo('#text' +i);
            // $("<label>").attr( {"for": "checkbox-as-image" + i, "style":"background-image: url('" + filename + "'); background-repeat: no-repeat;"}).insertAfter('#checkbox-as-image' +i);
            $("<label>").attr( {"for": "checkbox-as-image" + i}).insertAfter('#checkbox-as-image' +i);

        }
    })
});

$('#redirect-step-2').on('click', event => {
    event.preventDefault();

    location.href = "/Settings"
    
    $.ajax({
        url: "/delete",
        data: {'query': keyword, 'wantedImages': JSON.stringify(chosenImages)},
        method: 'POST'
    })
})


function addOrRemoveImageSelection(filename, add){
    if(add){
        chosenImages.push(filename);
    }
    else {
        //Filter das Bild mit dem mitgelieferten filename aus
        chosenImages = chosenImages.filter(value => value !== filename);

    }
}