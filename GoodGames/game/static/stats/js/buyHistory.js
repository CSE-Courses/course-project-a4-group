const getBuys = async () => { 
    const response = await fetch(`/api/data/profile`)
    if (response.status === 200) {
        const data = await response.json()
        return data
    } else {
        throw new Error('Unable to get buys')
    }
 }

 const displayBuys = async () => {
    const data = await getBuys()
    const table = document.querySelector('#buysTable')
    for(i = 0; i < data.buyNow.length; i++) {
        let row = document.createElement('tr')

        let item = document.createElement('td')
        item.innerHTML = data.buyNow[i].item;
        let price = document.createElement('td')
        price.innerHTML = data.buyNow[i].price;
        let date = document.createElement('td')
        let dateString = data.buyNow[i].date
        dateString = dateString.toString()
        dateString = dateString.split('-')
        let dayString = dateString[2]
        dayString = dayString.split('T')
        dayString = dayString[0]
        if(dayString[0] == '0'){
            dayString = dayString[1]
        }
        dateString = dateString[1] + '/' + dayString + '/' + dateString[0]
        date.innerHTML = dateString;
        
        row.appendChild(item);
        row.appendChild(price);
        row.appendChild(date);
        table.appendChild(row);
    }

 }

 displayBuys();