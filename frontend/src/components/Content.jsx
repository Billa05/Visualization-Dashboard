import MyResponsiveChoropleth from "./Choropleth/ChoroplethChart";
import MyResponsiveLine from "./LineChart/LineChart";
import MyResponsivePie from "./PieChart/PieChart";
import MyResponsiveScatterPlot from "./ScatterPlot/ScatterPlot";
import MyResponsiveHeatMap from "./HeatMap/HeatMap";

export default function Content(){
    return(
        <>
            <div className="parent p-3 grid gap-2 grid-cols-4 auto-rows-[minmax(300px,auto)]">
                <div className="p-2 border-2 box1 col-start-1 row-span-2 rounded">
                    {/* <p>Intensity vs. Likelihood, with points colored by Relevance</p> */}
                    <MyResponsiveScatterPlot/>
                </div>
                <div className="p-2 border-2 box2 col-start-4 row-span-2 rounded">
                    {/* <p>Display trends in topics or sectors over the years.</p> */}
                    <MyResponsiveLine/>
                </div>
                <div className="p-2 border-2 box3 col-start-2 col-span-2 row-span-2 rounded">
                    {/* <p> Insights by Region and Country</p> */}
                    <MyResponsiveChoropleth/>
                </div>
                <div className="p-2 border-2 box4 col-start-1 rounded">
                    {/* <p>Visualize the distribution of different topics and sectors.</p> */}
                    <MyResponsivePie/>
                </div>
                <div className="p-2 border-2 box5 col-start-4 rounded">
                    {/* <p>Intensity, Likelihood, Relevance by Year and Country.</p> */}
                    <MyResponsiveHeatMap/>
                </div>
            </div>
        </>
    )
}