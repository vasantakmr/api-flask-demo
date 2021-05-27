var app = document.getElementById('root')
var container = document.createElement('div')
container.setAttribute('class', 'container')
app.appendChild(container)

var request = new XMLHttpRequest()
request.open('GET', 'http://localhost:5000/data')
request.onload = function() {
    var data = JSON.parse(this.response)
    if(request.status<400) {
        data.forEach((repo)=> {
            const card = document.createElement('div')
            card.setAttribute('class', 'card')
            const h1 = document.createElement('h1')
            h1.textContent = repo.name
            const p = document.createElement('p')
            p.textContent = repo.description
            const anchor = document.createElement('a')
            anchor.setAttribute('href', repo.html_url)
            anchor.textContent = 'Link to Repo'
            const ownername = document.createElement('h1')
            ownername.textContent = repo.owner.login
            container.appendChild(card)
            card.appendChild(h1)
            card.appendChild(p)
            card.appendChild(anchor)
        })
    } else {
        const err = document.createElement('h1')
        err.textContent = 'Error'
        app.appendChild(err)
    }
}

request.send()
