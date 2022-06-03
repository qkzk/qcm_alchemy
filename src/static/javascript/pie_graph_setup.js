
/*  Unescape an HTML escaped string. */
function htmlDecode(input) {
    var doc = new DOMParser().parseFromString(input, "text/html");
    return doc.documentElement.textContent;
}

/* Calculates an interpolation point */
function calculatePoint(i, intervalSize, colorRangeInfo) {
    var { colorStart, colorEnd, useEndAsStart } = colorRangeInfo;
    return (useEndAsStart
        ? (colorEnd - (i * intervalSize))
        : (colorStart + (i * intervalSize)));
}

/* Create a d3 interpolation colors array. */
function interpolateColors(dataLength, colorScale, colorRangeInfo) {
    var { colorStart, colorEnd } = colorRangeInfo;
    var colorRange = colorEnd - colorStart;
    var intervalSize = colorRange / dataLength;
    var i, colorPoint;
    var colorArray = [];

    for (i = 0; i < dataLength; i++) {
        colorPoint = calculatePoint(i, intervalSize, colorRangeInfo);
        colorArray.push(colorScale(colorPoint));
    }

    return colorArray;
}

/* Set up Chart.js Pie Chart */
function createChart(chartId, chartData, colorScale, colorRangeInfo) {
    /* Grab chart element by id */
    const chartElement = document.getElementById(chartId);

    const dataLength = chartData.labels.length;

    /* Create color array */
    var COLORS = interpolateColors(dataLength, colorScale, colorRangeInfo);
    chartData.datasets[0].backgroundColor = COLORS;
    chartData.datasets[0].hoverBackgroundColor = COLORS;


    /* Create chart */
    return new Chart(chartElement, {
        type: 'pie',
        data: chartData,
        options: {
            plugins: {
                legend: {
                    display: true,
                    position: 'right',
                    labels: {
                        color: "#888888",
                        font: {
                            size: 14,
                        }
                    },
                }
            },
            radius: 150,
            hover: {
                onHover: function(e) {
                    var point = this.getElementAtEvent(e);
                    e.target.style.cursor = point.length ? 'pointer' : 'default';
                },
            },
        }
    });

}

const colorScale = d3.interpolateSpectral;

const colorRangeInfo = {
    colorStart: 0.2,
    colorEnd: 0.8,
    useEndAsStart: false,
};
