import { ResponsiveHeatMap } from "@nivo/heatmap";
import { useContext } from "react";
import { ChartsDataContext } from "../../ChartsContextProvider";
import { useState, useEffect } from "react";
import axios from "axios";
// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.
// website examples showcase many properties,
// you'll often use just a few of them.
const MyResponsiveHeatMap = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/")
      .then((res) => {
        // console.log(res.data);
        setData(res.data);
      })
      .catch((error) => console.error(error));
  }, []);
  //   const { data } = useContext(ChartsDataContext);
  return (
    <>
      {data && (
        <ResponsiveHeatMap
          data={data.heatmap}
          margin={{ top: 60, right: 90, bottom: 60, left: 90 }}
          valueFormat=">-.2s"
          axisTop={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: -90,
            legend: "",
            legendOffset: 46,
            truncateTickAt: 0,
          }}
          axisRight={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "country",
            legendPosition: "middle",
            legendOffset: 70,
            truncateTickAt: 0,
          }}
          axisLeft={{
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "country",
            legendPosition: "middle",
            legendOffset: -72,
            truncateTickAt: 0,
          }}
          colors={{
            type: "sequential",
            scheme: "red_yellow_blue",
            minValue: -100000,
            maxValue: 100000,
          }}
          emptyColor="#555555"
          labelTextColor={{
            from: "color",
            modifiers: [["darker", 2]],
          }}
          legends={[
            {
              anchor: "bottom",
              translateX: 0,
              translateY: 30,
              length: 400,
              thickness: 8,
              direction: "row",
              tickPosition: "after",
              tickSize: 3,
              tickSpacing: 4,
              tickOverlap: false,
              tickFormat: ">-.2s",
              title: "Value →",
              titleAlign: "start",
              titleOffset: 4,
            },
          ]}
        />
      )}
    </>
  );
};

export default MyResponsiveHeatMap;
