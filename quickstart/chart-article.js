        am4core.ready(function () {

            am4core.useTheme(am4themes_animated);

            var chart = am4core.create("chart-article", am4charts.PieChart);

            // Add data
            chart.data = [{
                "article": "Politics",
                "count": 10
            }, {
                "article": "Education",
                "count": 10
            }, {
                "article": "Technology",
                "count": 6
            }, {
                "article": "Environment",
                "count": 9
            }];


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
            colorSet.list = ["#F7CFEB", "#9FD5DD", "#A1EDA5", "#F2F08E"].map(function (color) {
                return new am4core.color(color);
            });
            pieSeries.colors = colorSet;


        });