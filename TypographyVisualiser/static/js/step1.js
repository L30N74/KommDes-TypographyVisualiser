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

            let checkbox = $("<input>").attr({"type": "checkbox", "class": "checkbox-for-images form-check-input" + i, "value": false})
            checkbox.click( event => {
                if(checkbox.val() === "true") {
                 checkbox.val(false);
                 addOrRemoveImageSelection(filename, false)
                } else {
                    checkbox.val(true);
                    addOrRemoveImageSelection(filename, true)
                }
            })

            // Auf Webseite darstellen
            $("<div>").attr({"class": "image-container", "id": "image" + i}).appendTo('#images');
            // checkbox.appendTo("#image" +i);
            newImage.appendTo("#image" +i);
            $("<div>").attr({"class": "hover-text", "id": "text" + i}).appendTo('#image' + i);
            $("<img>").attr({"class":"done-icon", "src": "../static/icons/done_green.svg"}).appendTo('#text' +i);
            //$("<input>").attr( {"id": "checkbox", "type": "checkbox", "value":"false"}).appendTo('#text' +i);;
            //$("<label>").attr( {"for": "checkbox"}).appendTo('#text' +i);
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