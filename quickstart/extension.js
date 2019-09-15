
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

    container.appendChild(createProgressBar(key, data[key].bias, colours[i]))
  })

  registerPieChart(data)
})

colours = ['bg-success', 'bg-warning', 'bg-danger', 'bg-info']


function registerPieChart(data) {
  am4core.ready(function () {

    am4core.useTheme(am4themes_animated);

    var chart = am4core.create("chart-article", am4charts.PieChart);

    // Add data
    chart.data = Object.keys(data).map((key, i) => {
      return {
        "article": key,
        "count": data[key].count
      }
    });



    //   [{
    //     "article": "Politics",
    //     "count": 10
    // }, {
    //     "article": "Education",
    //     "count": 10
    // }, {
    //     "article": "Technology",
    //     "count": 6
    // }, {
    //     "article": "Environment",
    //     "count": 9
    // }];


    chart.innerRadius = am4core.percent(35);

    // Add and configure Series
    var pieSeries = chart.series.push(new am4charts.PieSeries());
    pieSeries.dataFields.value = "count";
    pieSeries.dataFields.category = "article";
    pieSeries.slices.template.stroke = am4core.color("#fff");
    pieSeries.slices.template.strokeWidth = 2;
    pieSeries.slices.template.strokeOpacity = 1;

    // This creates initial animation
    pieSeries.hiddenState.properties.opacity = 1;
    pieSeries.hiddenState.properties.endAngle = -90;
    pieSeries.hiddenState.properties.startAngle = -90;

    var colorSet = new am4core.ColorSet();
    colorSet.list = ["#5cb85c", "#5bc0de", "#f0ad4e", "#d9534f"].map(function (color) {
        return new am4core.color(color);
    });
    pieSeries.colors = colorSet;





});
}