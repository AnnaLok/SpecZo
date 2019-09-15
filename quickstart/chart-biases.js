        am4core.ready(function () {

            am4core.useTheme(am4themes_animated);

            var chart = am4core.create("chart-biases", am4charts.PieChart);

            // Add data
            chart.data = [{
                "biases": "Extremely Bias",
                "count": 10
            }, {
                "biases": "Moderately Bias",
                "count": 10
            }, {
                "biases": "Slightly Bias",
                "count": 6
            }, {
                "biases": "Not Bias",
                "count": 9
            }];


            chart.innerRadius = am4core.percent(35);

            // Add and configure Series
            var pieSeries = chart.series.push(new am4charts.PieSeries());
            pieSeries.dataFields.value = "count";
            pieSeries.dataFields.category = "biases";
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
