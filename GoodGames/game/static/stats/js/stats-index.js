const getStats = async () => { 
    const response = await fetch(`/api/data`)
    if (response.status === 200) {
    const data = await response.json()
    return data
    } else {
    throw new Error('Unable to get stats')
    } }

    /*getStats().then((data) => { 
        console.log(data)
    }).catch((err) => { console.log(`Error: ${err}`)
    })
*/
const displayStats = async () => {
    const data = await getStats()
    console.log(data.username)
    const username = document.querySelector('#username')
    const wins = document.querySelector('#wins')
    const losses = document.querySelector('#losses')
    const gamesPlayed = document.querySelector('#gamesPlayed')
    const ggPoints = document.querySelector('#ggPoints')
    username.textContent = username.textContent + data.username
    wins.textContent = wins.textContent + data.wins
    losses.textContent = losses.textContent + data.losses
    gamesPlayed.textContent = gamesPlayed.textContent + data.gamesPlayed
    ggPoints.textContent = ggPoints.textContent + data.ggPoints[data.ggPoints.length - 1]
    let loopExit = -1
    if(data.matchHistory.length > 6){
        loopExit= 6
    }else{
        loopExit = data.matchHistory.length + 1 
    }
    for(i = 1; i < loopExit; i++){
    let matchHistorySection = document.getElementById('match-history-section')

    let matchElement = document.createElement('div')
    let game = document.createElement('div')
    let opponent = document.createElement('div')
    let winner = document.createElement('div')
    let wager = document.createElement('div')
    
    matchElement.className = "match-element"
    game.className = "match-first-fourth"
    opponent.className = "match-second-fourth"
    winner.className = "match-third-fourth"
    wager.className = "match-fourth-fourth"

    game.textContent = "Game: \r\n" + data.matchHistory[data.matchHistory.length - i].game
    opponent.textContent = "Opponent: \r\n" + data.matchHistory[data.matchHistory.length - i].opponent
    winner.textContent = "Winner: \r\n" + data.matchHistory[data.matchHistory.length - i].winner
    wager.textContent = "Wager: \r\n" + data.matchHistory[data.matchHistory.length - i].wager

    matchElement.appendChild(game)
    matchElement.appendChild(opponent)
    matchElement.appendChild(winner)
    matchElement.appendChild(wager)
    
    matchHistorySection.appendChild(matchElement)
    }
    
}

const displayCharts = async () => {
    const data = await getStats()
    var emptyArray = new Array(data.ggPoints.length);
for(var i=0;i<emptyArray.length;i++){
    emptyArray[i] = '';
}
var ctx = document.getElementById('myChart').getContext('2d');
var linear = document.getElementById('lineChart').getContext('2d');

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Madden21', 'Nba2k21', 'Fifa21', 'Nhl21', 'Valorant'],
        datasets: [{
            label: 'Games Played ',
            data: [data.madden, data.nba2k21, data.fifa21, data.nhl21, data.valorant],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }], xAxes: [{
                ticks: {
                    autoSkip: false,
                    maxRotation: 45,
                    minRotation: 45
                }
            }]
        }
    }
});

var lineChart = new Chart(linear, {
    type: 'line',
    data: {
        labels: emptyArray,
        datasets: [{
            label: 'GG Points after transactions',
            data: data.ggPoints,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],xAxes: [{
                ticks: {
                    autoSkip: false,
                    maxRotation: 90,
                    minRotation: 90
                }
            }]
        }
    }
});
}

displayStats()
displayCharts()