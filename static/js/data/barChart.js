// https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/column-drilldown/
function createBarChart(chartUnit) {
    let dataKbps = lookUpData("graph2");
    var data = [dataKbps.length];
    
    if(chartUnit === 'Mbps'){
        for (var i = 0; i < dataKbps.length; i++) {
            data[i] = {"name": String(dataKbps[i].name), "y": dataKbps[i].y / 1000};
        }
    }else if(chartUnit === 'MBps'){
        for (var i = 0; i < dataKbps.length; i++) {
            data[i] = {"name": String(dataKbps[i].name), "y": dataKbps[i].y / 1000 / 8};
        }
    }
    else{
        data = dataKbps;
    }

    let axisTitle = lookUpAxisLabel("graph2") + " (" + chartUnit + ")";
    
    Highcharts.chart('thru-by-app', {
        chart: {
            type: 'column'
        },
        credits: {
            enabled: false
        },
        title: {
            text: lookUpTitle("graph2")
        },
        xAxis: {
            type: 'category'
        },
        yAxis: {
            title: {
                text: axisTitle
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                }
            }
        },

        tooltip: {
            pointFormat: '{point.y:.2f}'
        },

        series: [
            {
                name: "Applications",
                colorByPoint: true,
                data: data
            }
        ],
    });
}

$("#thru-by-app-unit").change(function() {
    chartUnit = $("#thru-by-app-unit option:selected").val();
    console.log(chartUnit);
    createBarChart(chartUnit);
});

$( document ).ready(function() {
     createBarChart('KBps');
 });