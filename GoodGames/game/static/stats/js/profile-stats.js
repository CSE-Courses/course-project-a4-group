const getStats = async () => { 
    const response = await fetch(`/api/data/profile`)
    if (response.status === 200) {
        const data = await response.json()
        return data
    } else {
        throw new Error('Unable to get stats')
    }
 }

 const displayStats = async () => {
    const data = await getStats()
    const table = document.querySelector('#statsTable')
    for(i = 0; i < data.matchHistory.length; i++) {
        let row = document.createElement('tr')

        let game = document.createElement('td')
        game.innerHTML = data.matchHistory[i].game;
        let opponent = document.createElement('td')
        opponent.innerHTML = data.matchHistory[i].opponent;
        let winner = document.createElement('td')
        winner.innerHTML = data.matchHistory[i].winner;
        let wager = document.createElement('td')
        wager.innerHTML = data.matchHistory[i].wager;

        row.appendChild(game);
        row.appendChild(opponent);
        row.appendChild(winner);
        row.appendChild(wager);
        table.appendChild(row);
    }

 }

 displayStats();