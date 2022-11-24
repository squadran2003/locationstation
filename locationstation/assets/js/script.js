const outcode = document.querySelector("#outcode")
const outcodeSubmitButton = document.querySelector("#outcode-button")
const outcodeCard = document.querySelector("#outcode-card")
const outcodeCardTitle = document.querySelector("#outcode-card-title")
const outcodeCardBody = document.querySelector("#outcode-card-body")


outcodeCard.style.display='none';

outcodeSubmitButton.addEventListener('click', function(){
    fetch(`/api/outcode/${outcode.value}`)
    .then((response) => {
        if (response.status !== 404) {
            // Success: convert data received & run callback
            return response.text()
        }
        else {
            outcodeCardTitle.textContent=`there are no listings in ${outcode.value}`;
            outcodeCardBody.textContent = `No average daily price for ${outcode.value}`;
        }
    })
    .then((data) => {
        outcodeCard.style.display='';
        var xml = data,
            xmlDoc = $.parseXML(xml),
            $xml = $(xmlDoc),
            $listingCount = $xml.find("listing_count");
            $average_daily_price = $xml.find("average_daily_price");
            outcodeCardTitle.textContent=`${$listingCount.text()} listings in ${outcode.value}`;
            outcodeCardBody.textContent = `Average daily price of ${ $average_daily_price.text()}`;
      
    })
})