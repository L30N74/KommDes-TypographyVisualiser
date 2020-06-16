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
        //window.location.href = "/Settings";

        // Anzahl an Bildern bekommen wir am Ende des downloads mitgeteilt.
        // Für jedes runtergeladene Bild soll jetzt ein img-tag erstellt
        // und das src-Attribut mit dem Pfad zum Bild gefült werden
        // TODO: Pfad schöner zusammenbinden
        $(".search-result-images").remove();
        $(".checkbox-for-images").remove();
        for (let i = 0; i < amount; i++) {
            let filename = `../static/images/${keyword}/${keyword}-${i.toString()}.jpg`;

            let newImage = $("<img>").attr({"src": filename, "class": "search-result-images img_" + i});

            let checkbox = $("<input>").attr({"type": "checkbox", "class": "checkbox-for-images form-check-input" + i, "value": false})
            newImage.click(event => {
                // Check setzten
                if(checkbox.val() === "true") {
                 checkbox.val(false);
                 checkbox.prop("checked",false);
                } else {
                    checkbox.val(true);
                    checkbox.prop("checked",true);
                }
            })
            checkbox.click( event => {
                console.log(checkbox.val());
                if(checkbox.val() === "true") {
                 checkbox.val(false);
                } else {
                    checkbox.val(true);
                }
            })
            // Zu Liste ausgewählter Bilder hinzufügen
            if(checkbox.checked === true ) {
                chosenImages.push(filename);
            }
            // Auf Webseite darstellen
            $("<div>").attr({"class": "image-container", "id": "image" + i}).appendTo('#images');
            checkbox.appendTo("#image" +i);
            newImage.appendTo("#image" +i);
        }
    })
});

$('#redirect-step-2').on('click', event => {
    event.preventDefault();



    window.location.href = "/Settings";
})