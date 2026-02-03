const pptxgen = require('pptxgenjs');
const html2pptx = require('./html2pptx.js');
const path = require('path');

async function generate() {
    const pres = new pptxgen();
    pres.layout = 'LAYOUT_16x9';

    // Slide 1
    console.log("Processing Slide 1...");
    await html2pptx(path.resolve(__dirname, 'slides/slide1.html'), pres);

    // Slide 2
    console.log("Processing Slide 2...");
    await html2pptx(path.resolve(__dirname, 'slides/slide2.html'), pres);

    // Slide 3 + Chart
    console.log("Processing Slide 3...");
    const { slide: slide3, placeholders: ph3 } = await html2pptx(path.resolve(__dirname, 'slides/slide3.html'), pres);

    if (ph3 && ph3.length > 0) {
        const chartPh = ph3.find(p => p.id === 'market_chart') || ph3[0];

        // Customizing chart to match dark theme
        slide3.addChart(pres.charts.BAR, [{
            name: "Market Size ($B)",
            labels: ["2023", "2029 (Est)"],
            values: [394, 887.6]
        }], {
            x: chartPh.x, y: chartPh.y, w: chartPh.w, h: chartPh.h,
            chartColors: ["6B75FF"],
            showTitle: false,
            showLegend: false,
            showValAxisTitle: false,
            valAxisMinVal: 0,
            barDir: 'col',

            // Text Colors for Dark Theme
            dataLabelColor: "FAFAFA",
            catAxisLabelColor: "9496A8",
            valAxisLabelColor: "9496A8",

            dataLabelPosition: 'outEnd',
            showValue: true
        });
    }

    // Slide 4-10
    for (let i = 4; i <= 10; i++) {
        console.log(`Processing Slide ${i}...`);
        await html2pptx(path.resolve(__dirname, 'slides/slide' + i + '.html'), pres);
    }

    console.log("Saving...");
    await pres.writeFile({ fileName: 'Lensmor_Industry_Analysis.pptx' });
    console.log("Done! Saved to Lensmor_Industry_Analysis.pptx");
}

generate().catch(console.error);
