class Dashboard {
    createAreaChart(element, pointSize, lineWidth, data, xkey, ykeys, labels, lineColors) {
        Morris.Area({
            element,
            pointSize,
            lineWidth,
            data,
            xkey,
            ykeys,
            labels,
            resize: true,
            gridLineColor: '#eee',
            hideHover: 'auto',
            lineColors,
            fillOpacity: 0.9,
            behaveLikeLine: true,
        });
    }

    createDonutChart(element, data, colors) {
        Morris.Donut({
            element,
            data,
            resize: true,
            colors,
            labelColor: '#666',
            backgroundColor: 'transparent',
            fillOpacity: 0.1,
            formatter: (x) => x + "%"
        });
    }

    createLineChart(element, data, xkey, ykeys, labels, lineColors) {
        Morris.Line({
            element,
            data,
            xkey,
            ykeys,
            labels,
            hideHover: 'auto',
            gridLineColor: '#eee',
            resize: true,
            lineColors
        });
    }

    createBarChart(element, data, xkey, ykeys, labels, lineColors) {
        Morris.Bar({
            element: element,
            data: data,
            xkey: xkey,
            ykeys: ykeys,
            labels: labels,
            barSizeRatio: 0.4,
            resize: true,
            hideHover: 'auto',
            barColors: lineColors,
            gridLineColor:'rgba(135, 135, 135, 0.1)',
            // barRadius: [3, 3, 0, 0],
            barOpacity: 1,
            highlightSpeed: 150,
            barRadius: [5, 5, 0, 0],
            gridTextColor: '#999'
        });
    }

    init() {
        const $areaData = [
            {y: '2007', a: 0, b: 0, c: 0},
            {y: '2008', a: 150, b: 45, c: 15},
            {y: '2009', a: 60, b: 150, c: 195},
            {y: '2010', a: 180, b: 36, c: 21},
            {y: '2011', a: 90, b: 60, c: 360},
            {y: '2012', a: 75, b: 240, c: 120},
            {y: '2013', a: 30, b: 30, c: 30}
        ];
        this.createAreaChart('morris-area-chart', 0, 0, $areaData, 'y', ['a', 'b', 'c'], ['Series A', 'Series B', 'Series C'], ['#ec536c', '#5b6be8', '#59ceb5']);

        const $donutData = [
            {label: "Margin", value: 20},
            {label: "Profit", value: 30},
            {label: "Lost", value: 10},
        ];
        this.createDonutChart('morris-donut-example', $donutData, ['rgba(211, 218, 232,0.8)', 'rgba(64, 164, 241,0.8)', 'rgba(236, 83, 108,0.8)']);

        const $data = [
            {y: '2012', a: 0, b: 0},
            {y: '2013', a: 50, b: 30},
            {y: '2014', a: 50, b: 30},
            {y: '2015', a: 120, b: 100},
            {y: '2016', a: 60, b: 40},
            {y: '2017', a: 140, b: 120},
            {y: '2018', a: 180, b: 200}
        ];
        this.createLineChart('multi-line-chart', $data, 'y', ['a', 'b'], ['Dom', 'Int'], ['#59ceb5', '#ec536c']);

        const $barData = [
            {y: '2009', a: 100, b: 90},
            {y: '2010', a: 75, b: 65},
            {y: '2011', a: 50, b: 40},
            {y: '2012', a: 75, b: 65},
            {y: '2013', a: 50, b: 40},
            {y: '2014', a: 75, b: 65},
            {y: '2015', a: 100, b: 90},
            {y: '2016', a: 90, b: 75}
        ];
        this.createBarChart('morris-bar-example', $barData, 'y', ['a', 'b'], ['Series A', 'Series B'], ['#365d6e', '#59ceb5']);
    }
}

function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

(() => {
    const dashboard = new Dashboard();
    // dashboard.init();
    $.ajax({
        url: '/api/expense/',
        type: 'GET',
        success: function (data) {
            $('#budget').prepend(data.budget);
            $('#consumption').prepend(data.consumption);
            $('#expense-this-month').prepend(data.expense_this_month);
            $('#total-expense').prepend(data.total_expense);
            dashboard.createDonutChart('morris-donut-example',
                data.donut_chart_data,
                data.donut_chart_data.map(() => getRandomColor())
            );
            dashboard.createLineChart('multi-line-chart', data.line_chart_data, 'y', ['a'], ['Expense'], ['#59ceb5']);
            dashboard.createBarChart(
                'morris-bar-example',
                data.bar_chart_data,
                'label', ['value'],
                ['Expense'],
                ['#365d6e']
            );
            dashboard.createAreaChart('morris-area-chart', 0, 0, data.area_chart_data, 'y', ['a'], ['Expense'], ['#365d6e'])
        }
    })
})();
