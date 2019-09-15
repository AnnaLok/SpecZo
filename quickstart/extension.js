
let container = document.getElementById('stat-bar')


console.log('in extension file')
console.log(container)
console.log(JSON.stringify(container))



function createProgressBar(title, percentage, colour) {
  let li = document.createElement('li')

  let statBarTitle = document.createElement('div')
  statBarTitle.className = 'stat-bar-title'
  statBarTitle.textContent = title

  li.appendChild(statBarTitle)

  let progressContainer = document.createElement('div')
  progressContainer.className = "progress md-progress"

  let progressBar = document.createElement('div')
  progressBar.className = `progress-bar ${colour}`
  progressBar.role = 'progressbar'
  // add aria values
  progressBar.textContent = `${percentage}%`

  progressContainer.appendChild(progressBar)

  li.appendChild(progressContainer)

  console.log(li)

  return li
}

fetch('http://localhost:8000/analysis').then(response => {
  return response.json()
}).then(data => {
  console.log(JSON.stringify(data, 0, 2))

  Object.keys(data).forEach((key, i) => {

    console.log('test')

    container.appendChild(createProgressBar(key, data[key], colours[i]))
  })
})

colours = ['bg-success', 'bg-warning', 'bg-danger', 'bg-info']